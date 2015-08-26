#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

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


replicdata = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

FemRep = []
MaleRep = []
for sample in replicdata[replicdata["sex"]== "female"]["sample"]:
    rep = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = rep["t_name"].str.contains("FBtr0331261")
    FemRep.append(rep[roi]["FPKM"].values)
for sample in replicdata[replicdata["sex"]== "male"]["sample"]:
    rep = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = rep["t_name"].str.contains("FBtr0331261")
    MaleRep.append(rep[roi]["FPKM"].values)     

XVal = [4, 5, 6, 7]
D = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

plt.figure()
plt.plot(FemSxl, 'r', label="Female")
plt.plot(MaleSxl, 'b', label = "Male")
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.xticks(range(0,8), D)
plt.title("Sxl")
plt.scatter(XVal, FemRep, c='r', label = "Female Rep")
plt.scatter(XVal, MaleRep, c='b', label = "Male Rep")
plt.legend(bbox_to_anchor=(0.1, 1), loc=2, borderaxespad=0.)
plt.savefig("plot1.png")

