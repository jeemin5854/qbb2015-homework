#!/usr/bin/env python
from __future__ import division
import sys
import chrombits

arr = chrombits.ChromosomeLocationBitArray(fname = sys.argv[1])

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file(sys.argv[2])
beats.set_bits_from_file(sys.argv[3])

intersect (beaf and complement (ctcf))




