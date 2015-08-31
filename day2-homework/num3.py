#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open (filename)

counter_var = 0

for line in f:
    if "NH:i:1" in line:
        counter_var += 1
print counter_var