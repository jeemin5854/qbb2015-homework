#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df= pd.read_table(annotation)
order = df.sort(columns="FPKM",ascending=True)
roi = order["FPKM"] >0


count = 0
for x in df["FPKM"]:
    if x >0:
        count += 1
print count #=9548
print order[roi]["FPKM"]


top= order[roi]["FPKM"][0:3182]
middle= order[roi]["FPKM"][3182:6365]
bottom= order[roi]["FPKM"][6365:9549]


top = np.log(top)
middle = np.log(middle)
bottom = np.log(bottom)
#It is good idea to log the y values to get more spread out graph.

plt.figure()
plt.title("boxplot")
plt.boxplot([top, middle, bottom])
plt.xlabel("gene")
plt.ylabel("FPKM")
plt.savefig("plot4_ln.png")