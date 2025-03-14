/*
 * International Chemical Identifier (InChI)
 * Version 1
 * Software version 1.07
 * April 30, 2024
 *
 * MIT License
 *
 * Copyright (c) 2024 IUPAC and InChI Trust
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
*
* The InChI library and programs are free software developed under the
 * auspices of the International Union of Pure and Applied Chemistry (IUPAC).
 * Originally developed at NIST.
 * Modifications and additions by IUPAC and the InChI Trust.
 * Some portions of code were developed/changed by external contributors
 * (either contractor or volunteer) which are listed in the file
 * 'External-contributors' included in this distribution.
 *
 * info@inchi-trust.org
 *
*/


#ifndef _E__ICHITIME_H_
#define _E__ICHITIME_H_

#ifdef COMPILE_ANSI_ONLY

#ifdef __FreeBSD__
#include <sys/time.h>
#endif

/* get times() */
#ifdef INCHI_USETIMES
#include <sys/times.h>
#endif

/*#include <sys/timeb.h>*/

#include <time.h>

typedef struct e_tagInchiTime {
    clock_t clockTime;
} e_inchiTime;

#else

/* Win32 _ftime(): */
#include <sys/timeb.h>

typedef struct e_tagInchiTime {
    unsigned long  clockTime; /* Time in seconds since midnight (00:00:00), January 1, 1970;
                                 signed long overflow expected in 2038 */
    long           millitime; /* milliseconds */
} e_inchiTime;

#endif


unsigned long e_ulMyGetTickCount( int bStart );
unsigned long e_ulMyTickCountDiff( unsigned long ulTickEnd, unsigned long ulTickStart );

void e_inchiTimeGet( e_inchiTime *TickEnd );
long e_inchiTimeMsecDiff( e_inchiTime *TickEnd, e_inchiTime *TickStart );
void e_inchiTimeAddMsec( e_inchiTime *TickEnd, unsigned long nNumMsec );
int  bInchiTimeIsOver( e_inchiTime *TickEnd );
long e_inchiTimeElapsed( e_inchiTime *TickStart );


#ifndef COMPILE_ALL_CPP
#ifdef __cplusplus
extern "C" {
#endif
#endif



#ifndef COMPILE_ALL_CPP
#ifdef __cplusplus
}
#endif
#endif



#endif    /* _E__ICHITIME_H_ */
