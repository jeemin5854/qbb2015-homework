#!/usr/bin/env python


import matplotlib.pyplot as plt
import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df= pd.read_table(annotation, comment ='#', header = None) 

df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

roi = df["attributes"].str.contains("Sxl")
roi2= df["type"].str.contains("transcript")

plt.figure()
plt.plot(df[roi][roi2]["start"])
plt.xlabel("gene")
plt.ylabel("start position")
plt.title("Sxl and transcript")
plt.savefig("plot2.png")


