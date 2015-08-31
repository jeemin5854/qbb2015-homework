#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open(filename)

#1a
#for line in f:
#    print line
    
    
#1
counter_var = 0

for line in f:
    if "@SQ" in line:
        pass
    else:
        counter_var += 1    
# Because there is a header in the front
print counter_var