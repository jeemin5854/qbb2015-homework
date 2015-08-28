#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys

import chrombits


arr = chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )

new = beaf.intersect( ctcf.complement() ) # chrom, dtype

bed = new.bed_from_bit()
print I, II, III

