#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open (filename)

count = 0

for line in f:
    if "NM:i:0" in line:
        count += 1
print count 
