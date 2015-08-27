#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from numpy.lib.scimath import logn
from math import e
import numpy as np


metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")


FemSxl = []
MaleSxl =[]
for sample in metadata[metadata["sex"]== "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261") 
    FemSxl.append(df[roi]["FPKM"].values)
for sample in metadata[metadata["sex"]== "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261") 
    MaleSxl.append(df[roi]["FPKM"].values)

#Errormessage:
M =[]
for i in (0,len(FemSxl)):
    M.append(logn(2, FemSxl[i]) - logn(2, MaleSxl[i]))
    
"""   
A = []
for i in len(MaleSxl):
    A.append(0.5 * logn(2, FemSxl[i]) + (0.5 * logn(2, MaleSxl)[i])
    


plt.figure()
plt.plot(M,A)
plt.xlabel("A")
plt.ylabel("M")
plt.title("Norm of FPKM values: Male vs. Female")
plt.savefig("plot4.png")
"""