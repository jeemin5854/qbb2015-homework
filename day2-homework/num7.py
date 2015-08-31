#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open (filename)


counter_2L = 0

for line in f:
    field = line.split()
    if line.startswith("@"):
        pass
    if field[2] =="2L" and 10000<=int(field[3])<=20000:
        counter_2L += 1
print counter_2L