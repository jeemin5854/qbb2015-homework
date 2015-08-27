#!/usr/bin/env python
from __future__ import division
import sys
import numpy
from matplotlib_venn import venn3, venn3_circles
import pandas as pd
import matplotlib.pyplot as plt


def arrays_from_len_file (fname):
    arrays = {}
    for line in open (fname):
        fields = line.split()
        name = fields[0]
        size = int (fields[1])
        arrays[name] = numpy.zeros(size, dtype =bool) #for dtype, we only need the info whether we have the region of interest or NOt => Boolean
    return arrays

def set_bits_from_file (arrays, fname): #Arrays is passed on to this def from the first one (so we don't need to return arrays)
    for line in open (fname):
        fields = line.split()
        #Parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[chrom][start:end] = 1
        


CTCF = arrays_from_len_file (sys.argv[1])
set_bits_from_file (CTCF, sys.argv[2]) 

BEAF = arrays_from_len_file (sys.argv[1])
set_bits_from_file (BEAF, sys.argv[3]) 

SU = arrays_from_len_file (sys.argv[1])
set_bits_from_file (SU, sys.argv[4]) 


CTCF_only= 0
BEAF_only = 0
SU_only =0
three_overlap = 0
CTCF_SU_overlap= 0
CTCF_BEAF_overlap = 0
BEAF_SU_overlap = 0


for filename in sys.argv[2:]:
    for line in open (filename):
        fields = line.split()
        #parse fields
        chrom =fields[0]
        start = int(fields[1])
        end = int(fields[2])
        #Get Slice
        #Aggregate
        sl_CTCF = CTCF[chrom][start:end]
        sl_BEAF = BEAF[chrom][start:end]
        sl_SU = SU[chrom][start:end]
        if sl_CTCF.any() > 0 and sl_BEAF.any() > 0 and sl_SU.any() > 0:
            three_overlap += 1
        elif sl_CTCF.any() > 0 and sl_BEAF.any() > 0 and not sl_SU.any() > 0:
            CTCF_BEAF_overlap += 1
        elif sl_CTCF.any() > 0 and not sl_BEAF.any() > 0 and sl_SU.any() > 0:
            CTCF_SU_overlap += 1
        elif not sl_CTCF.any() > 0 and sl_BEAF.any() > 0 and sl_SU.any() > 0:
            BEAF_SU_overlap +=1
        elif sl_SU.any() > 0:
            SU_only +=1
        elif sl_BEAF.any() > 0:
            BEAF_only +=1
        elif sl_CTCF.any() > 0 :
            CTCF_only += 1
                            
#sl1 sl2 sl3 
# sl1 &sl2 & sl3 



s = (
    CTCF_only,    # Abc
    BEAF_only,    # aBc
    CTCF_BEAF_overlap,    # ABc
    SU_only,    # abC
    CTCF_SU_overlap,    # AbC
    BEAF_SU_overlap,  # aBC
    three_overlap,    # ABC)
    )
v= venn3(subsets=s, set_labels=('CTCF', 'BEAF', 'SuHW'))
# Subset labels
v.get_label_by_id('100').set_text(CTCF_only)
v.get_label_by_id('010').set_text(BEAF_only)
v.get_label_by_id('110').set_text(int(CTCF_BEAF_overlap / 2) )
v.get_label_by_id('001').set_text(SU_only)
v.get_label_by_id('101').set_text(int(CTCF_SU_overlap/ 2))
v.get_label_by_id('011').set_text(int(BEAF_SU_overlap /2))
v.get_label_by_id('111').set_text(int(three_overlap /3))
#Colors
v.get_patch_by_id('100').set_color('c')
v.get_patch_by_id('010').set_color('#993333')
v.get_patch_by_id('110').set_color('blue')
plt.savefig("Venn.png")












