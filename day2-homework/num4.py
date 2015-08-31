#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open (filename)

counter_var = 0

for line in f:
    if "@" not in line[0]:
        line = line.split()
        counter_var += 1
        print line [2]
    if counter_var >= 10:
         break
