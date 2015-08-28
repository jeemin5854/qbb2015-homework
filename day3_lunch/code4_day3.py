#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")


FemSxl = []
MaleSxl =[]
for sample in metadata[metadata["sex"]== "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    #roi = df["t_name"].str.contains("FBtr0331261") 	-too little data comes out by filtering
    FemSxl.append(df["FPKM"].values)
for sample in metadata[metadata["sex"]== "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    #roi = df["t_name"].str.contains("FBtr0331261") 	-too little data comes out by this filtering
    MaleSxl.append(df["FPKM"].values)

print len(FemSxl)
print len(MaleSxl)

    
M = np.log2(FemSxl) - np.log2(MaleSxl)
A = 0.5 * (np.log2(FemSxl) + np.log2(MaleSxl))

plt.figure()
plt.scatter(A, M)
plt.xlabel("A")
plt.ylabel("M")
plt.title("Norm of FPKM values: Male vs. Female")
plt.savefig("plot4.png")
