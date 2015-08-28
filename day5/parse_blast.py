#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt


reader = open(sys.argv[1])

line = reader.readline()

l = []
ident = []
gap =[]
for line in reader:    
    if "> " in line:
        l.append(line.strip("\n""> "))
    if " Identities =" in line:
        ident.append(line[14:25])
    if "Gaps =" in line:
        gap.append(line.split(", ")[1])
column =[ l, ident , gap]

#for i in range(len(column[0])):
#    print column[0][i], column[1][i], column[2][i]

reader = open(sys.argv[1])
line = reader.readline()

score = []
escore = []
for line in reader:  
    if "  N"
    fields = line.split()
    score = float(fields[11])
    escore =float(fields[10])
    score.append(score)
    escore.append(escore)


plt.figure()
plt.hist(score, escore, color = 'blue', bins =100)
plt.title("scores vs. e-values")
plt.xlabel("score")
plt.ylabel("e-scores")
plt.savefig("histogram.png")

