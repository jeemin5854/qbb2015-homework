#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"

df= pd.read_table(annotation, sep=',') 

roi = df["sample"]

for i in roi:
    var = "/Users/cmdb/qbb2015/stringtie/" + i +  "/t_data.ctab"
    df2 = pd.read_table(var)
    roi2 = df2["t_name"].str.contains("FBtr0331261")
    print df2[roi2]

