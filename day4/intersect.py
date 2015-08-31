#!/usr/bin/env python
from __future__ import division
"""
DNase: regions that are not histone associated (starts from the end)

phastCons: regions of the DNA that seem to be evolutionarily constrained [chr, start, end logOdd score]

dm3.len: (chr, size)


1. unzip the file
2. BED files


sudo pip install matplotlib-venn
"""


""""
1. Count intersection of two Bed files

"""


import sys
import numpy

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

arrays = arrays_from_len_file (sys.argv[1])
#set_bits_from_file (arrays, sys.argv[2]) #don't need to set this to any variable, cuz it's set in the previous line


for key, value in arrays.iteritems(): #[1]: len file [2],[3],[4]: three insulators
    if x in sys.argv[2], sys.argv[3], sys.argv[4]:
        set_bits_from_file (arrays, x)
        print key, numpy.sum(value)

##for key, value in arrays.iteritems():
##    print key, type (value), value.shape, numpy.sum(value) #numpy.sum is the overlapping region size cuz we set the second definition as 1

"""

total = 0
any_overlap= 0
all_overlap = 0
half_overlap = 0
for line in open (sys.argv[3]):
    fields = line.split()
    #parse fields
    chrom =fields[0]
    start = int(fields[1])
    end = int(fields[2])
    #Get Slice
    sl = arrays[chrom][start:end]
    #Aggregate
    total += 1
    any_overlap += sl.any() #any:ANY of the two is true
    all_overlap += sl.all() #all:all the sl are overlapped
    #Half or 50% overlap
    half_overlap += (numpy.sum(sl) / len(sl) > 0.5)
    

print "Total: %d, Any overlap: %d, All overlap: %d, half overlapping: %d" % (total, any_overlap, all_overlap, half_overlap)  #%s: string, %d: decimal,integer, %f: float


    

"""





def intersect(arrays1, arrays2):
    rval={}
    for chrom in arrays1:
        rval[chrom] = arrays1[chrom] & arrays2[chrom]
    return rval

def union(arrays1, arrays2):
    rval={}
    for chrom in arrays1:
        rval[chrom] = arrays1[chrom] | arrays2[chrom]
    return rval       

def complement(arrays1):
    rval={}
    for chrom in arrays1:
        rval[chrom] =~ arrays1[chrom]
    return rval
    
arr = arrays_from_len_file(sys.argv[1])

ctcf = copy.deepcopy(arr)
beaf = copy.deepcopy(arr)

set_bits_from_file(ctcf, sys.argv[2])
set_bits_from_file(ctcf, sys.argv[3])

intersect (beaf and complement (ctcf))




