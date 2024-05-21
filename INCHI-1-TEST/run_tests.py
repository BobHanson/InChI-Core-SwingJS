import subprocess
import logging
from functools import partial
from datetime import datetime
from sdf_pipeline import drivers
from .consumers import regression_consumer, invariance_consumer
from .config import (
    get_args,
    get_current_time,
    get_progress,
    DATASETS,
    N_PROCESSES,
    INCHI_LIB_PATH,
    INCHI_REFERENCE_LIB_PATH,
    TEST_PATH,
)


if __name__ == "__main__":
    test, dataset = get_args()

    if test == "regression-reference":
        subprocess.run(f"{TEST_PATH}/compile_inchi_reference_lib.sh", check=True)
    else:
        subprocess.run(f"{TEST_PATH}/compile_inchi_lib.sh", check=True)

    exit_code = 0
    sdf_paths = DATASETS[dataset]["sdf_paths"]
    n_sdf = len(sdf_paths)
    log_path = DATASETS[dataset]["log_path"].joinpath(
        f"{datetime.now().strftime('%Y%m%dT%H%M%S')}_{test}_{dataset}.log"
    )
    logging.basicConfig(filename=log_path, encoding="utf-8", level=logging.INFO)

    logging.info(
        f"{get_current_time()}: Starting to process {n_sdf} SDFs on {N_PROCESSES} cores."
    )

    for i, sdf_path in enumerate(sdf_paths):
        try:
            match test:
                case "regression":
                    exit_code = max(
                        exit_code,
                        drivers.regression(
                            sdf_path=sdf_path,
                            reference_path=DATASETS[dataset]["log_path"].joinpath(
                                f"{sdf_path.stem}.regression_reference.sqlite"
                            ),
                            consumer_function=partial(
                                regression_consumer, inchi_lib_path=INCHI_LIB_PATH
                            ),
                            get_molfile_id=DATASETS[dataset]["molfile_id"],
                            number_of_consumer_processes=N_PROCESSES,
                        ),
                    )

                case "regression-reference":
                    reference_path = DATASETS[dataset]["log_path"].joinpath(
                        f"{sdf_path.stem}.regression_reference.sqlite"
                    )
                    if reference_path.exists():
                        logging.info(f"Not re-computing reference for {sdf_path.name}.")

                        continue

                    exit_code = max(
                        exit_code,
                        drivers.regression_reference(
                            sdf_path=sdf_path,
                            reference_path=reference_path,
                            consumer_function=partial(
                                regression_consumer,
                                inchi_lib_path=INCHI_REFERENCE_LIB_PATH,
                            ),
                            get_molfile_id=DATASETS[dataset]["molfile_id"],
                            number_of_consumer_processes=N_PROCESSES,
                        ),
                    )

                case "invariance":
                    exit_code = max(
                        exit_code,
                        drivers.invariance(
                            sdf_path=sdf_path,
                            consumer_function=partial(
                                invariance_consumer, inchi_lib_path=INCHI_LIB_PATH
                            ),
                            get_molfile_id=DATASETS[dataset]["molfile_id"],
                            number_of_consumer_processes=N_PROCESSES,
                        ),
                    )

            logging.info(
                f"{get_progress(i + 1, n_sdf)}; Ran {test} on {sdf_path.name}."
            )

        except Exception as exception:
            logging.error(
                f"{get_progress(i + 1, n_sdf)}; Aborted {test} on {sdf_path.name} due to {type(exception).__name__}; {exception}."
            )

    raise SystemExit(exit_code)
