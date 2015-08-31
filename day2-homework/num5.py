#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.SAM"
f = open (filename)

counter_var = 0


Loc2L= 0
Loc2R = 0
Loc3R = 0
Loc4 = 0
LocX = 0
    
for line in f:
    fields = line.split()
    if line.startswith("@"):
        pass
    if "2L" in fields[2]:
        Loc2L += 1
    if "2R" in fields[2]:
        Loc2R += 1
    if "3R" in fields[2]:
        Loc3R += 1
    if "4" in fields[2]:
        Loc4 += 1
    if "X" in fields[2]:
        LocX += 1

print "2L = ", Loc2L
print "2R = ", Loc2R
print "3R = ", Loc3R
print "4 = ", Loc4
print "X = ", LocX