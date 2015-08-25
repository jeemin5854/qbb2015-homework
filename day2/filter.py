#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

#for line in f: #for loop from a file always returns in terms of lines 
    #return line #comma will get rid of the line between each line printed
    
#for data in f:
    #fields = data.split() #makes a list with each column as item
    #print fields,
    
#for data in f
    #if "tRNA" in data:
    #    print data, 
    
for data in f :
    fields = data.split()
    if "tRNA" in fields[9]:
        print data,