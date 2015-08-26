#!/usr/bin/env python

import sys

#open using arguments:
#print sys.argv
#filename = sys.argv[1] 

#for filename in sys.argv[1:]:
#	f = open (filename)
#	name_counts= {}



f = sys.stdin	

name_counts = {}
for line_count, data in enumerate(f): #line_count is incrementing in terms of 1 from 0 (0, 1, 2, 3)
    fields = data.split()
    gene_name = fields [9]
    if gene_name not in name_counts:
    	name_counts[gene_name] = 1
    else:
        name_counts[gene_name] += 1

#Iterate key, value pairs from the name counts dictionary
for key, value in name_counts.iteritems():
    # print the key and value
    print key,"","", value
    
        
    
    