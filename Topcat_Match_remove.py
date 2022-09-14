#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
import os
from astropy.io import fits
#########################################################################

def skymatch_remove(file_1, values_1,
             file_2, values_2,
             output=None,
             join='2not1', find='all',
             java="java -jar",
             topcat_loc=r"/Users/Astro/Documents/Software/",
             topcat="topcat-full.jar",
             ext=1, header=False
             ):
    if output is None:
        out = 'tempcat.fits'
    else:
        out = output

    topcat = " ".join([java, topcat_loc+topcat, "-stilts"])
    string = " ".join([topcat,
                       "tmatch2 matcher=exact",
                       "join=%s" % join,
                       "find=%s" % find,
                       "in1=%s" % file_1,
                       "in2=%s" % file_2,
                       "out=%s" % out,
                       "values1=%s" % values_1, 
                       "values2=%s" % values_2  ]) 
                       
    print('\n' + 'PERFORMING THE REMOVE-MATCH\n' + string + '\n')
    #print('Matching fields:' + file_1 + ' with ' + file_2)
    #print('MATCHING_RADIUS = ', err)
    #print('MATCHING_TYPE   = ',find)
    print('(Possible Matching types include: all|best|best1|best2.)')
    print('(See TOPCAT for details.) \n')
    os.system(string)
    data = fits.getdata(out, ext=ext)
    if output is None:
        os.remove(out)
    if header:
        head = fits.getheader(string, ext=ext)
        return data, head
    else:
        return data

#########################################################################
# Example usage
"""
skymatch(
    "/Users/kresimirtisanic/topcattest/detections_at_3_and_1.4_GHz.fits",
    ["RA_1", "DEC_1"],
    "/Users/kresimirtisanic/topcattest/vla_1.4ghz_dp_sin_10.fix_blobs.fits",
    ["RA_wc", "Dec_wc"],
    1.17, "/Users/kresimirtisanic/topcattest/test2.fits")
"""
#########################################################################
# End of code
