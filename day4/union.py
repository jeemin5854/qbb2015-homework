#!/usr/bin/env python

"""
Create the set of intervals resulting from the union of CTCF, BEAF, and SuHW; generate another venn diagram using this set of intervals
"""

from __future__ import division

import sys

import chrombits


arr = chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()
su = arr.copy()

ctcf2=ctcf.set_bits_from_file( sys.argv[2] )
beaf2=beaf.set_bits_from_file( sys.argv[3] )
su2 =su.set_bits_from_file( sys.argv[4])

#union of two circles
U_CTCF_BEAF = beaf.intersect( ctcf)
U_BEAF_SU = su.intersect( beaf )
U_SU_CTCF = ctcf.intersect( su )

#How to go from ChromosomeLocationBitrrays( dicts=rval to numbers???

three_overlap = 0 #ctcf.intersect(U_BEAF_SU) 
CTCF_only = 0 #ctcf  + U_CTCF_BEAF - U_SU_CTCF + beaf.complement
BEAF_only = 0 #beaf - (U_BEAF_SU + U_CTCF_BEAF - su.complement)
CTCF_BEAF_overlap = 0 #U_CTCF_BEAF - su.complement
SU_only = 0 #su - (U_SU_CTCF + U_BEAF_SU - ctcf.complement)
CTCF_SU_overlap = 0 #U_SU_CTCF - beaf.complement
BEAF_SU_overlap = 0 #U_BEAF_SU - ctcf.complement


for filename in sys.argv[2:]:
    for line in open(filename):
        field = line.split()
        chrom = field[0]
        startpos = int (field[1])
        endpos = int ( field[2])
        C = ctcf2[chrom][start:end]
        B = beaf2[chrom][start:end]
        S = su2[chrom][start:end]
        if C.any() == True and B.any()==False and S.any()==False:
            CTCF_only += 1 
        elif B.any()==True and C.any() == False and S.any()==False:
            BEAF_only += 1 
        elif S.any()==True and B.any()==False and C.any() == False:
            SU_only += 1 
        elif C.any() == True and B.any()==True and S.any()==False:
            CTCF_BEAF_overlap += 1
        elif C.any() == True and S.any()==True and B.any()==False: 
            CTCF_SU_overlap += 1 
        elif B.any()==True and S.any() == True and C.any()==False:
            count_aBC += 1 
        else: 
            count_ABC += 1
        total += 1
        

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