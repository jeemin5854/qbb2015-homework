#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy.lib.scimath 



reader = open(sys.argv[1])

line = reader.readline()
"""
l = []
ident = []
gap =[]

for line in reader:    
    if "> " in line:
        l.append(line.strip("\n""> "))
    if " Identities =" in line:
        ident.append(line[14:25])
    if "Gaps =" in line:
        line = line.split(" ")[7:]
        gap.append(line)
    column = [l , ident , gap]

print column
"""
#for i in range(len(column[0])):
#    print column[0][i], column[1][i], column[2][i]

reader = open(sys.argv[1])
line = reader.readline()

score = []
escore = []
for line in reader:  
    if "  NM" in line or "  NR" in line:    
        fields = line.split()
        scorev = float(fields[2])
        escorev = float(fields[3])
        score.append(scorev)
        escore.append(escorev)





#hist- scores
plt.figure()
plt.hist(score, bins= 100)
plt.title("score histogram")
plt.xlabel("sample")
plt.ylabel("scores")
plt.savefig("histogram-score.png")



#hist-escores
plt.figure()
plt.hist(escore, bins = 100)
plt.title("e-score histogram")
plt.xlabel("sample")
plt.ylabel("e-scores")
plt.savefig("histogram-escores.png")


print len(score), len(escore)
#hist-escores
plt.figure()
plt.scatter(score, escore)
plt.xlabel("score")
plt.ylabel("escore")
plt.title("Score vs. Escore")
plt.savefig("scatterplot.png")
