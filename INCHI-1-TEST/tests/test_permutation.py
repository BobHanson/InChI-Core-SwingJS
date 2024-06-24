import pytest
import random
from sdf_pipeline.utils import permute_molblock
from rdkit import Chem

molblocks = [
    """
102195623
  -OEChem-04092319443D

 80 85  0     1  0  0  0  0  0999 V2000
   -0.4382    0.5917   -0.5552 C   0  0  1  0  0  0  0  0  0  0  0  0
    0.3973   -0.4373    0.2996 C   0  0  2  0  0  0  0  0  0  0  0  0
   -1.9287    0.4759   -0.1618 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8720   -0.3673   -0.1288 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.1486    1.9872   -0.3453 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.2354   -1.8235    0.1170 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.3699    0.3087   -2.0933 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.3602   -0.1387    1.8348 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.4390   -0.7514    0.1089 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.4139    0.9936   -0.2843 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.6062    2.0742   -0.3469 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5784   -1.9324    0.0505 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.6829    1.7241   -0.1128 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5764   -1.4980   -0.3323 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6434    3.0594   -0.1767 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.6541   -2.9625    0.0014 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0906    2.9328   -0.1421 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9779   -2.8172   -0.1883 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.8713    4.2119   -0.0894 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.9041   -3.9895   -0.3146 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.4930    5.0009    1.1747 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.3767    3.9020   -0.0571 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.5495    5.0545   -1.3331 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.1153   -5.2973   -0.1387 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.5650   -3.9837   -1.7026 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.9897   -3.8979    0.7686 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.8080   -0.9610    0.4443 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.8256    1.1990   -0.3159 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.9613   -1.1377    0.7269 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.0134    1.3720   -0.3424 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.3662   -1.3529    1.0711 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.4601    1.5825   -0.3747 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.8114   -2.7364    0.6791 C   0  0  0  0  0  0  0  0  0  0  0  0
   -7.2661   -0.4900    0.2276 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.9428    2.2060    0.9074 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.1960    0.2695   -0.3739 C   0  0  0  0  0  0  0  0  0  0  0  0
   -7.7864   -2.6519   -0.2378 C   0  0  0  0  0  0  0  0  0  0  0  0
   -8.0666   -1.2676   -0.5159 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.7941    1.3710    1.5209 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.9502    0.1774    0.7311 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7626   -0.6790   -2.3582 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.6504    0.3593   -2.4887 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.9613    1.0437   -2.6549 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.7801    0.8407    2.0879 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.9420   -0.8839    2.3932 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6556   -0.1607    2.2442 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.0330    3.0741   -0.4012 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0567   -2.9003   -0.0747 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.7556    1.6018   -0.0414 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.6156   -1.4383   -0.6351 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.1919    4.0362   -0.0395 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.1563   -3.9230    0.0615 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.1374    5.8813    1.2863 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.6164    4.3918    2.0783 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.4627    5.3715    1.1590 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.7166    3.3608   -0.9485 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.6774    3.3540    0.8441 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.9498    4.8385   -0.0404 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.7433    4.4950   -2.2563 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5087    5.3951   -1.3614 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.1748    5.9551   -1.3618 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.7959   -6.1561   -0.2082 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.3651   -5.4480   -0.9244 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.6378   -5.3737    0.8458 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.2531   -3.1447   -1.8491 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.8155   -3.9462   -2.5025 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.1538   -4.8969   -1.8524 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.5499   -3.8296    1.7710 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.6265   -4.7907    0.7536 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.6547   -3.0373    0.6366 H   0  0  0  0  0  0  0  0  0  0  0  0
   -6.5521   -1.1765    2.1356 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.7601    2.1906   -1.2345 H   0  0  0  0  0  0  0  0  0  0  0  0
   -6.4130   -3.6573    1.0795 H   0  0  0  0  0  0  0  0  0  0  0  0
   -7.2720    0.5904    0.2254 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.6546    3.1801    1.2752 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.1325   -0.4823   -1.1473 H   0  0  0  0  0  0  0  0  0  0  0  0
   -8.2992   -3.4804   -0.6988 H   0  0  0  0  0  0  0  0  0  0  0  0
   -8.8157   -0.9271   -1.2122 H   0  0  0  0  0  0  0  0  0  0  0  0
    8.3001    1.5519    2.4553 H   0  0  0  0  0  0  0  0  0  0  0  0
    8.5875   -0.6496    0.9990 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  1  3  1  0  0  0  0
  1  5  1  0  0  0  0
  1  7  1  0  0  0  0
  2  4  1  0  0  0  0
  2  6  1  0  0  0  0
  2  8  1  0  0  0  0
  3  9  2  0  0  0  0
  3 13  1  0  0  0  0
  4 10  1  0  0  0  0
  4 14  2  0  0  0  0
  5 11  1  0  0  0  0
  5 15  2  0  0  0  0
  6 12  2  0  0  0  0
  6 16  1  0  0  0  0
  7 41  1  0  0  0  0
  7 42  1  0  0  0  0
  7 43  1  0  0  0  0
  8 44  1  0  0  0  0
  8 45  1  0  0  0  0
  8 46  1  0  0  0  0
  9 12  1  0  0  0  0
  9 27  1  0  0  0  0
 10 11  2  0  0  0  0
 10 28  1  0  0  0  0
 11 47  1  0  0  0  0
 12 48  1  0  0  0  0
 13 17  2  0  0  0  0
 13 49  1  0  0  0  0
 14 18  1  0  0  0  0
 14 50  1  0  0  0  0
 15 17  1  0  0  0  0
 15 51  1  0  0  0  0
 16 18  2  0  0  0  0
 16 52  1  0  0  0  0
 17 19  1  0  0  0  0
 18 20  1  0  0  0  0
 19 21  1  0  0  0  0
 19 22  1  0  0  0  0
 19 23  1  0  0  0  0
 20 24  1  0  0  0  0
 20 25  1  0  0  0  0
 20 26  1  0  0  0  0
 21 53  1  0  0  0  0
 21 54  1  0  0  0  0
 21 55  1  0  0  0  0
 22 56  1  0  0  0  0
 22 57  1  0  0  0  0
 22 58  1  0  0  0  0
 23 59  1  0  0  0  0
 23 60  1  0  0  0  0
 23 61  1  0  0  0  0
 24 62  1  0  0  0  0
 24 63  1  0  0  0  0
 24 64  1  0  0  0  0
 25 65  1  0  0  0  0
 25 66  1  0  0  0  0
 25 67  1  0  0  0  0
 26 68  1  0  0  0  0
 26 69  1  0  0  0  0
 26 70  1  0  0  0  0
 27 29  3  0  0  0  0
 28 30  3  0  0  0  0
 29 31  1  0  0  0  0
 30 32  1  0  0  0  0
 31 33  1  0  0  0  0
 31 34  1  0  0  0  0
 31 71  1  0  0  0  0
 32 35  1  0  0  0  0
 32 36  1  0  0  0  0
 32 72  1  0  0  0  0
 33 37  2  0  0  0  0
 33 73  1  0  0  0  0
 34 38  2  0  0  0  0
 34 74  1  0  0  0  0
 35 39  2  0  0  0  0
 35 75  1  0  0  0  0
 36 40  2  0  0  0  0
 36 76  1  0  0  0  0
 37 38  1  0  0  0  0
 37 77  1  0  0  0  0
 38 78  1  0  0  0  0
 39 40  1  0  0  0  0
 39 79  1  0  0  0  0
 40 80  1  0  0  0  0
M  END
""",
    """
102157914
  -OEChem-04092319283D

 54 54  0     1  0  0  0  0  0999 V2000
    2.0355    0.7861   -1.5209 S   0  0  0  0  0  0  0  0  0  0  0  0
    1.4543   -3.6596    0.2681 O   0  0  0  0  0  0  0  0  0  0  0  0
   -2.6975   -4.8653   -0.3245 O   0  0  0  0  0  0  0  0  0  0  0  0
   -4.0350   -3.4470    0.8373 O   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0050   -0.8538   -1.4528 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.2537    0.0113    1.4482 O   0  0  0  0  0  0  0  0  0  0  0  0
   -5.5884    0.8874   -2.0606 O   0  0  0  0  0  0  0  0  0  0  0  0
   -4.0049   -0.7925   -1.8190 O   0  5  0  0  0  0  0  0  0  0  0  0
    5.4474    1.9273   -1.3202 O   0  0  0  0  0  0  0  0  0  0  0  0
    7.5119    2.4169   -0.5167 O   0  0  0  0  0  0  0  0  0  0  0  0
   -2.1094   -1.5041    0.4960 N   0  0  0  0  0  0  0  0  0  0  0  0
    2.1339   -1.4972    0.7704 N   0  0  0  0  0  0  0  0  0  0  0  0
    5.4381   -0.5419   -0.4683 N   0  0  0  0  0  0  0  0  0  0  0  0
   -4.3553    0.3990   -1.5629 N   0  3  0  0  0  0  0  0  0  0  0  0
   -1.2780    3.7858    1.4188 N   0  0  0  0  0  0  0  0  0  0  0  0
   -1.9012    5.0908    1.5668 N   0  3  0  0  0  0  0  0  0  0  0  0
   -2.3572    6.0711    1.6846 N   0  0  0  0  0  0  0  0  0  0  0  0
   -0.9627   -3.2438    1.8235 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.6858   -2.8809    0.5236 C   0  0  1  0  0  0  0  0  0  0  0  0
    0.3288   -2.4534    2.0415 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.1949   -1.4141   -0.2060 C   0  0  1  0  0  0  0  0  0  0  0  0
    1.3450   -2.6278    0.9250 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.9380   -3.7208    0.3678 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.6987   -0.9111   -1.5640 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.7289   -0.6147   -0.4926 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.3339   -0.5761    0.3713 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.2949    0.7328   -0.2969 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.5932    1.1823   -0.8454 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5508    1.5736    0.4321 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.6332    0.2054   -0.1532 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.0396    2.5614   -0.5717 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.9875    2.9620    0.7148 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.2897    3.3908    0.1562 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.5939    1.6204   -0.6702 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.6258   -3.0744    2.6818 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7339   -4.3173    1.8196 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0499   -3.0707   -0.3478 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.0896   -1.3913    2.1698 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.8069   -2.7877    2.9698 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.5931   -2.4277   -0.3474 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.7398   -1.1893    1.2289 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.9597   -0.6840    1.3542 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.4965   -0.9322   -2.3125 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.8981   -1.5624   -1.9318 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.4295   -1.0711   -1.3346 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.5941    1.2743    0.8504 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.4729   -0.3143   -0.6230 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.7667    0.2342    0.9322 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.9871    2.9131   -0.9631 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.5031   -5.4192   -0.4056 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.6913    0.8472   -2.8156 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.6831    4.3855    0.3141 H   0  0  0  0  0  0  0  0  0  0  0  0
   -5.9271    0.1127   -2.5402 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.4460    2.8525   -1.6462 H   0  0  0  0  0  0  0  0  0  0  0  0
  1 24  1  0  0  0  0
  1 51  1  0  0  0  0
  2 22  2  0  0  0  0
  3 23  1  0  0  0  0
  3 50  1  0  0  0  0
  4 23  2  0  0  0  0
  5 25  2  0  0  0  0
  6 26  2  0  0  0  0
  7 14  1  0  0  0  0
  7 53  1  0  0  0  0
  8 14  1  0  0  0  0
  9 34  1  0  0  0  0
  9 54  1  0  0  0  0
 10 34  2  0  0  0  0
 11 19  1  0  0  0  0
 11 25  1  0  0  0  0
 11 41  1  0  0  0  0
 12 21  1  0  0  0  0
 12 22  1  0  0  0  0
 12 42  1  0  0  0  0
 13 26  1  0  0  0  0
 13 30  1  0  0  0  0
 13 45  1  0  0  0  0
 14 28  2  3  0  0  0
 15 16  1  0  0  0  0
 15 32  2  3  0  0  0
 16 17  3  0  0  0  0
 18 19  1  0  0  0  0
 18 20  1  0  0  0  0
 18 35  1  0  0  0  0
 18 36  1  0  0  0  0
 19 23  1  0  0  0  0
 19 37  1  0  0  0  0
 20 22  1  0  0  0  0
 20 38  1  0  0  0  0
 20 39  1  0  0  0  0
 21 24  1  0  0  0  0
 21 26  1  0  0  0  0
 21 40  1  0  0  0  0
 24 43  1  0  0  0  0
 24 44  1  0  0  0  0
 25 27  1  0  0  0  0
 27 28  1  0  0  0  0
 27 29  2  0  0  0  0
 28 31  1  0  0  0  0
 29 32  1  0  0  0  0
 29 46  1  0  0  0  0
 30 34  1  0  0  0  0
 30 47  1  0  0  0  0
 30 48  1  0  0  0  0
 31 33  2  0  0  0  0
 31 49  1  0  0  0  0
 32 33  1  0  0  0  0
 33 52  1  0  0  0  0
M  CHG  3   8  -1  14   1  16   1
M  END
""",
    """
101777188
  -OEChem-04092318473D

 59 61  0     1  0  0  0  0  0999 V2000
   -2.4676    2.7108   -0.5986 S   0  0  0  0  0  0  0  0  0  0  0  0
    2.4921    0.2958    3.2586 O   0  0  0  0  0  0  0  0  0  0  0  0
   -0.5008    0.7626    3.5373 O   0  0  0  0  0  0  0  0  0  0  0  0
    3.5183   -3.0642   -2.1522 O   0  0  0  0  0  0  0  0  0  0  0  0
   -3.2213   -1.0019   -0.8271 O   0  0  0  0  0  0  0  0  0  0  0  0
   -5.8405    1.4081   -1.1685 O   0  0  0  0  0  0  0  0  0  0  0  0
   -7.5556   -0.0171   -1.5868 O   0  0  0  0  0  0  0  0  0  0  0  0
    2.2442   -0.4988    0.1518 N   0  0  3  0  0  0  0  0  0  0  0  0
   -1.0768    0.0167    0.4552 N   0  0  0  0  0  0  0  0  0  0  0  0
    2.9905    4.2689   -0.9170 N   0  3  0  0  0  0  0  0  0  0  0  0
   -4.7348   -0.0808    0.6711 N   0  0  0  0  0  0  0  0  0  0  0  0
    1.3675   -0.1458    1.0464 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0196    0.0644    1.1718 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.2690    0.1056   -1.1836 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.0820   -1.6899    0.3211 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.6029    0.1982    2.4538 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.1569    0.4236    2.5884 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.3781    0.3773    0.9787 C   0  0  1  0  0  0  0  0  0  0  0  0
    2.5242    1.5842   -1.0884 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.3260   -2.9272   -0.0769 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.5393    1.8992    1.0328 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.4651   -0.3141    0.1623 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.6852    2.0527   -0.4805 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.6014    2.4867   -1.6089 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5800   -3.5565   -1.2955 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.3615   -3.4447    0.7876 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.8957    3.4224   -0.4076 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8646    3.8453   -1.5073 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8693   -4.7033   -1.6497 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.6508   -4.5916    0.4335 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.9046   -5.2209   -0.7851 C   0  0  0  0  0  0  0  0  0  0  0  0
   -5.9306   -0.6338    0.0787 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.2387    5.7049   -0.8246 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.5345    0.2633   -0.9709 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.3207   -0.1020   -1.6962 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.0549   -0.3283   -1.8144 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.4015   -1.7886    1.3680 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.0201   -1.5871   -0.2380 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.4884   -0.0237    1.9958 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0493   -0.2169   -0.5349 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.4949    2.1769    1.4882 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.7569    2.3535    1.6489 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.4235    1.3711   -0.0700 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.6885    2.1479   -2.0878 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.1595   -2.9780    1.7476 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.7765    3.8490    0.0567 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.1834    4.5971   -1.8871 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.8454    0.4832    1.5080 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.0567   -5.2039   -2.5959 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.0981   -4.9963    1.1080 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.3516   -6.1142   -1.0604 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.6260    3.9649   -0.1510 H   0  0  0  0  0  0  0  0  0  0  0  0
   -6.6584   -0.7681    0.8838 H   0  0  0  0  0  0  0  0  0  0  0  0
   -5.6934   -1.5978   -0.3810 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.7943    6.0582    0.1096 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.3158    5.8932   -0.8335 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.7860    6.2110   -1.6818 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.5533   -3.6287   -2.9434 H   0  0  0  0  0  0  0  0  0  0  0  0
   -6.2527    1.9738   -1.8557 H   0  0  0  0  0  0  0  0  0  0  0  0
  1 21  1  0  0  0  0
  1 52  1  0  0  0  0
  2 16  2  0  0  0  0
  3 17  2  0  0  0  0
  4 25  1  0  0  0  0
  4 58  1  0  0  0  0
  5 22  2  0  0  0  0
  6 34  1  0  0  0  0
  6 59  1  0  0  0  0
  7 34  2  0  0  0  0
  8 12  1  0  0  0  0
  8 14  1  0  0  0  0
  8 15  1  0  0  0  0
  9 13  1  0  0  0  0
  9 18  1  0  0  0  0
  9 40  1  0  0  0  0
 10 27  2  0  0  0  0
 10 28  1  0  0  0  0
 10 33  1  0  0  0  0
 11 22  1  0  0  0  0
 11 32  1  0  0  0  0
 11 48  1  0  0  0  0
 12 13  2  0  0  0  0
 12 16  1  0  0  0  0
 13 17  1  0  0  0  0
 14 19  1  0  0  0  0
 14 35  1  0  0  0  0
 14 36  1  0  0  0  0
 15 20  1  0  0  0  0
 15 37  1  0  0  0  0
 15 38  1  0  0  0  0
 16 17  1  0  0  0  0
 18 21  1  0  0  0  0
 18 22  1  0  0  0  0
 18 39  1  0  0  0  0
 19 23  2  0  0  0  0
 19 24  1  0  0  0  0
 20 25  1  0  0  0  0
 20 26  2  0  0  0  0
 21 41  1  0  0  0  0
 21 42  1  0  0  0  0
 23 27  1  0  0  0  0
 23 43  1  0  0  0  0
 24 28  2  0  0  0  0
 24 44  1  0  0  0  0
 25 29  2  0  0  0  0
 26 30  1  0  0  0  0
 26 45  1  0  0  0  0
 27 46  1  0  0  0  0
 28 47  1  0  0  0  0
 29 31  1  0  0  0  0
 29 49  1  0  0  0  0
 30 31  2  0  0  0  0
 30 50  1  0  0  0  0
 31 51  1  0  0  0  0
 32 34  1  0  0  0  0
 32 53  1  0  0  0  0
 32 54  1  0  0  0  0
 33 55  1  0  0  0  0
 33 56  1  0  0  0  0
 33 57  1  0  0  0  0
M  CHG  1  10   1
M  END
""",
    """
6401426
  -OEChem-04092309003D

 32 33  0     0  0  0  0  0  0999 V2000
    0.0377    1.5842    0.9749 O   0  5  0  0  0  0  0  0  0  0  0  0
   -2.6786    0.2376   -1.3710 O   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0778   -1.0469    0.4817 N   0  0  0  0  0  0  0  0  0  0  0  0
    0.9518   -1.6028   -0.1207 N   0  3  0  0  0  0  0  0  0  0  0  0
    2.2335   -1.5716   -0.3938 N   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1637   -2.3696    0.1292 N   0  0  0  0  0  0  0  0  0  0  0  0
   -4.1684    0.9272    0.2742 N   0  0  0  0  0  0  0  0  0  0  0  0
   -4.9958    1.5700   -0.6233 N   0  0  0  0  0  0  0  0  0  0  0  0
    0.2156   -0.6005    0.3228 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.1548    0.7408    0.2719 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.7917    0.6516    0.5472 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.8260   -0.3790   -0.1896 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.8958    2.0271    0.4692 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.2621   -0.3595    0.9346 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0988   -2.6704   -0.2328 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.2864   -0.3204   -0.4941 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.8871    2.8933   -0.7849 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.0327    0.2890   -0.1956 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.4638    2.5985    1.3007 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.9296    1.8528    0.7869 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0134    0.3602    1.7161 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.9112   -1.1116    1.4013 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.3749   -3.6575   -0.5708 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.8684   -0.1420    0.4155 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.6281   -1.2758   -0.9090 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.5142    0.4465   -1.2389 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.3440    2.3840   -1.6387 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.4456    3.8179   -0.6061 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.8665    3.1690   -1.0712 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.4218    0.9419    1.2572 H   0  0  0  0  0  0  0  0  0  0  0  0
   -5.9250    1.1669   -0.5100 H   0  0  0  0  0  0  0  0  0  0  0  0
   -5.0700    2.5387   -0.3157 H   0  0  0  0  0  0  0  0  0  0  0  0
  1 11  1  0  0  0  0
  2 18  2  0  0  0  0
  3  6  1  0  0  0  0
  3  9  1  0  0  0  0
  3 14  1  0  0  0  0
  4  5  2  0  0  0  0
  4  9  1  0  0  0  0
  4 15  1  0  0  0  0
  5 12  1  0  0  0  0
  6 15  2  0  0  0  0
  7  8  1  0  0  0  0
  7 18  1  0  0  0  0
  7 30  1  0  0  0  0
  8 31  1  0  0  0  0
  8 32  1  0  0  0  0
  9 11  2  0  0  0  0
 10 11  1  0  0  0  0
 10 12  2  0  0  0  0
 10 13  1  0  0  0  0
 12 16  1  0  0  0  0
 13 17  1  0  0  0  0
 13 19  1  0  0  0  0
 13 20  1  0  0  0  0
 14 18  1  0  0  0  0
 14 21  1  0  0  0  0
 14 22  1  0  0  0  0
 15 23  1  0  0  0  0
 16 24  1  0  0  0  0
 16 25  1  0  0  0  0
 16 26  1  0  0  0  0
 17 27  1  0  0  0  0
 17 28  1  0  0  0  0
 17 29  1  0  0  0  0
M  CHG  2   1  -1   4   1
M  END
""",
    """
6337844
  -OEChem-04092308513D

 29 28  0     1  0  0  0  0  0999 V2000
    3.4014    0.0732    2.3464 S   0  0  0  0  0  0  0  0  0  0  0  0
   -2.9952    0.7315   -0.0895 O   0  0  0  0  0  0  0  0  0  0  0  0
    3.2484   -1.0084   -1.2560 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.4631    0.9038   -1.1621 O   0  0  0  0  0  0  0  0  0  0  0  0
   -0.4890    1.5694   -0.1545 O   0  0  0  0  0  0  0  0  0  0  0  0
   -3.3219   -1.6371    0.0876 O   0  0  0  0  0  0  0  0  0  0  0  0
    1.1630   -0.0462   -0.0405 N   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6188   -2.1028    0.1156 N   0  3  0  0  0  0  0  0  0  0  0  0
   -0.2417   -3.1072    0.1893 N   0  0  0  0  0  0  0  0  0  0  0  0
    2.2792    0.8670   -0.1090 C   0  0  1  0  0  0  0  0  0  0  0  0
    2.6940    1.3693    1.2762 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.4465    0.2789   -0.8843 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.1499    0.3932   -0.0698 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1315   -0.7348    0.0158 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.4646   -0.5461    0.0052 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.4177    0.7765   -0.0891 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.8654    2.2197   -0.1813 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9465    1.7308   -0.6994 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.8366    1.8053    1.7998 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.4530    2.1528    1.1768 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.3588   -1.0395    0.0471 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.8117    0.2218   -0.9491 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.8086    0.3389    0.8374 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.6381    0.8630    3.4040 H   0  0  0  0  0  0  0  0  0  0  0  0
   -5.9566    2.2917   -0.1835 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.4747    2.7992    0.6617 H   0  0  0  0  0  0  0  0  0  0  0  0
   -4.4786    2.6858   -1.0937 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.0100   -1.3659   -1.7604 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.7784   -2.4421    0.1464 H   0  0  0  0  0  0  0  0  0  0  0  0
  1 11  1  0  0  0  0
  1 24  1  0  0  0  0
  2 15  1  0  0  0  0
  2 16  1  0  0  0  0
  3 12  1  0  0  0  0
  3 28  1  0  0  0  0
  4 12  2  0  0  0  0
  5 13  2  0  0  0  0
  6 15  1  0  0  0  0
  6 29  1  0  0  0  0
  7 10  1  0  0  0  0
  7 13  1  0  0  0  0
  7 21  1  0  0  0  0
  8  9  3  0  0  0  0
  8 14  1  0  0  0  0
 10 11  1  0  0  0  0
 10 12  1  0  0  0  0
 10 18  1  0  0  0  0
 11 19  1  0  0  0  0
 11 20  1  0  0  0  0
 13 14  1  0  0  0  0
 14 15  2  0  0  0  0
 16 17  1  0  0  0  0
 16 22  1  0  0  0  0
 16 23  1  0  0  0  0
 17 25  1  0  0  0  0
 17 26  1  0  0  0  0
 17 27  1  0  0  0  0
M  CHG  1   8   1
M  END
""",
    """
5150642
  -OEChem-04092306033D

 66 71  0     0  0  0  0  0  0999 V2000
   -5.4497    1.5081    2.1469 S   0  0  0  0  0  0  0  0  0  0  0  0
    5.4676    1.5125   -2.1271 S   0  0  0  0  0  0  0  0  0  0  0  0
   -4.8157    1.8148    3.4155 O   0  0  0  0  0  0  0  0  0  0  0  0
   -6.8960    1.4408    2.0619 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.8415    1.8515   -3.3957 O   0  0  0  0  0  0  0  0  0  0  0  0
    6.9177    1.4406   -2.0465 O   0  0  0  0  0  0  0  0  0  0  0  0
   -4.6476   -3.7310   -1.4148 O   0  5  0  0  0  0  0  0  0  0  0  0
    4.6052   -3.7547    1.3785 O   0  5  0  0  0  0  0  0  0  0  0  0
   -4.8368    2.5750    0.9411 N   0  0  0  0  0  0  0  0  0  0  0  0
    4.8676    2.5845   -0.9226 N   0  0  0  0  0  0  0  0  0  0  0  0
   -6.6136   -2.6538   -2.9920 N   0  3  0  0  0  0  0  0  0  0  0  0
    6.5738   -2.7106    2.9745 N   0  3  0  0  0  0  0  0  0  0  0  0
   -6.9824   -3.1376   -3.8911 N   0  0  0  0  0  0  0  0  0  0  0  0
    6.9350   -3.2069    3.8698 N   0  0  0  0  0  0  0  0  0  0  0  0
   -4.8040   -0.0516    1.6149 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.8108   -0.0358   -1.6172 C   0  0  0  0  0  0  0  0  0  0  0  0
   -5.2607   -0.6972    0.4624 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.2523   -0.7077   -0.4657 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.6886   -1.9410    0.1045 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.6680   -1.9501   -0.1227 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.4347    2.5765    0.6718 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.4552    2.5830   -0.6514 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.8068   -0.6025    2.4106 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.8075   -0.5809   -2.4189 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6950    2.5791    0.1457 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.7257    2.5803   -0.1271 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.2677   -0.1462   -0.3466 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.2607   -0.1736    0.3529 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.6814   -2.4920    0.9134 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.6593   -2.4840   -0.9411 C   0  0  0  0  0  0  0  0  0  0  0  0
   -5.1407   -2.5976   -1.0517 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.1095   -2.6221    1.0287 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.2443   -1.8258    2.0587 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.2328   -1.8027   -2.0815 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.5299    2.8911    1.6858 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.0008    2.2712    0.6244 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.9695    2.2630   -0.6054 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5601    2.8937   -1.6681 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1601    2.8926    1.4227 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.6310    2.2698    0.8874 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5996    2.2643   -0.8684 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.1902    2.8924   -1.4049 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.7046   -0.8122   -1.4920 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.6870   -0.8549    1.4933 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.1422   -2.0357   -1.8438 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.1126   -2.0769    1.8306 C   0  0  0  0  0  0  0  0  0  0  0  0
   -5.4376    2.7336    0.1221 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.4660    2.7321   -0.0997 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.4337   -0.1176    3.3068 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.4419   -0.0846   -3.3124 H   0  0  0  0  0  0  0  0  0  0  0  0
   -6.7344    0.8127   -0.1610 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.7367    0.7826    0.1770 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.2068   -3.4439    0.6859 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.1754   -3.4340   -0.7251 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.4633   -2.2620    2.6749 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.4507   -2.2259   -2.7052 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.8654    3.1762    2.6780 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.6982    2.0201    1.4191 H   0  0  0  0  0  0  0  0  0  0  0  0
   -3.6651    2.0083   -1.4009 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.8950    3.1800   -2.6595 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.4958    3.1800    2.2330 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.3150    1.9902    1.8887 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.2828    1.9834   -1.8690 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.5251    3.1772   -2.2156 H   0  0  0  0  0  0  0  0  0  0  0  0
   -7.4806   -0.3639   -2.1072 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.4645   -0.4196    2.1161 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  3  2  0  0  0  0
  1  4  2  0  0  0  0
  1  9  1  0  0  0  0
  1 15  1  0  0  0  0
  2  5  2  0  0  0  0
  2  6  2  0  0  0  0
  2 10  1  0  0  0  0
  2 16  1  0  0  0  0
  7 31  1  0  0  0  0
  8 32  1  0  0  0  0
  9 21  1  0  0  0  0
  9 47  1  0  0  0  0
 10 22  1  0  0  0  0
 10 48  1  0  0  0  0
 11 13  3  0  0  0  0
 11 45  1  0  0  0  0
 12 14  3  0  0  0  0
 12 46  1  0  0  0  0
 15 17  1  0  0  0  0
 15 23  2  0  0  0  0
 16 18  1  0  0  0  0
 16 24  2  0  0  0  0
 17 19  2  0  0  0  0
 17 27  1  0  0  0  0
 18 20  2  0  0  0  0
 18 28  1  0  0  0  0
 19 29  1  0  0  0  0
 19 31  1  0  0  0  0
 20 30  1  0  0  0  0
 20 32  1  0  0  0  0
 21 35  2  0  0  0  0
 21 37  1  0  0  0  0
 22 36  2  0  0  0  0
 22 38  1  0  0  0  0
 23 33  1  0  0  0  0
 23 49  1  0  0  0  0
 24 34  1  0  0  0  0
 24 50  1  0  0  0  0
 25 26  1  0  0  0  0
 25 39  2  0  0  0  0
 25 41  1  0  0  0  0
 26 40  2  0  0  0  0
 26 42  1  0  0  0  0
 27 43  2  0  0  0  0
 27 51  1  0  0  0  0
 28 44  2  0  0  0  0
 28 52  1  0  0  0  0
 29 33  2  0  0  0  0
 29 53  1  0  0  0  0
 30 34  2  0  0  0  0
 30 54  1  0  0  0  0
 31 45  2  0  0  0  0
 32 46  2  0  0  0  0
 33 55  1  0  0  0  0
 34 56  1  0  0  0  0
 35 39  1  0  0  0  0
 35 57  1  0  0  0  0
 36 40  1  0  0  0  0
 36 58  1  0  0  0  0
 37 41  2  0  0  0  0
 37 59  1  0  0  0  0
 38 42  2  0  0  0  0
 38 60  1  0  0  0  0
 39 61  1  0  0  0  0
 40 62  1  0  0  0  0
 41 63  1  0  0  0  0
 42 64  1  0  0  0  0
 43 45  1  0  0  0  0
 43 65  1  0  0  0  0
 44 46  1  0  0  0  0
 44 66  1  0  0  0  0
M  CHG  4   7  -1   8  -1  11   1  12   1
M  END
""",
]


def get_molblock_id(val):
    return val.split()[0].strip()


@pytest.mark.parametrize("molblock", molblocks, ids=get_molblock_id)
def test_permutation_integrity(molblock):
    random.seed(42)
    unique_smiles = set()

    for _ in range(10):
        permuted_molblock = permute_molblock(molblock.strip())
        permuted_mol = Chem.MolFromMolBlock(
            permuted_molblock, sanitize=False, removeHs=False, strictParsing=False
        )
        canonical_smiles = Chem.MolToCXSmiles(permuted_mol)
        unique_smiles.add(canonical_smiles)

    assert len(unique_smiles) == 1
