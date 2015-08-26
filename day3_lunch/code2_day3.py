#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from numpy.lib.scimath import logn
from math import e

origin = "~/qbb2015/stringtie/SRR072893/t_data.ctab"

df893 = pd.read_table(origin)

df= []
for item in df893["FPKM"]:
    if item > 0:
        item = logn(e, item)
        df.append(item)


plt.figure()
plt.hist(df)
plt.title("ln(FPKM) of SRR072893")
plt.xlabel("Value")
plt.ylabel("ln(FPKM)")
plt.savefig("plot3.png")



