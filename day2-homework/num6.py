#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open (filename)


total_MAPQ = 0
counter_var = 0 

for line in f:
    if line.startswith("@"):
        pass
    else:
        fields = line.split()
        total_MAPQ += int(fields[4])
        counter_var += 1
        
print total_MAPQ/counter_var