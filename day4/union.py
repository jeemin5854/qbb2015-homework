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

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )
su.set_bits_from_file( sys.argv[4])

#union of two circles
U_CTCF_BEAF = beaf.intersect( ctcf)
U_BEAF_SU = su.intersect( beaf )
U_SU_CTCF = ctcf.intersect( su )

#How to go from ChromosomeLocationBitrrays( dicts=rval to numbers???
three_overlap = ctcf.intersect(U_BEAF_SU) 
CTCF_only = ctcf  + U_CTCF_BEAF - U_SU_CTCF + beaf.complement
BEAF_only = beaf - (U_BEAF_SU + U_CTCF_BEAF - su.complement)
CTCF_BEAF_overlap = U_CTCF_BEAF - su.complement
SU_only = su - (U_SU_CTCF + U_BEAF_SU - ctcf.complement)
CTCF_SU_overlap = U_SU_CTCF - beaf.complement
BEAF_SU_overlap = U_BEAF_SU - ctcf.complement

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