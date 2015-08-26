#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from numpy.lib.scimath import logn
from math import e
import numpy as np
from scipy import stats


origin = "~/qbb2015/stringtie/SRR072893/t_data.ctab"

df893 = pd.read_table(origin)

df= []
for item in df893["FPKM"]:
    if item > 0:
        item = logn(e, item)
        df.append(item)


gkde=stats.gaussian_kde(df)
ind = np.linspace(-7,7,101)
kdepdf = gkde.evaluate(ind)

alpha = 0.6 #weight for (prob of) lower distribution
mlow, mhigh = (0,4)  #mean locations for gaussian mixture


plt.figure()
plt.plot(ind, stats.norm.pdf(ind), color="r", label='DGP normal')
plt.xlabel("Value")
plt.ylabel("ln(FPKM)")
plt.title("ln(FPKM) of SRR072893")
plt.savefig("realplot3.png")



