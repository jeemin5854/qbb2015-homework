#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df= pd.read_table(annotation, comment ='#', header = None) #"dataframe"

#print df

#print df.head() # first 5 lines

#print df.describe() #number stats

#print df.info() #describes each column as number, string, etc.

#print "\n this is what happens with [1:5]\n"
#print df[1:5] #prints row #2 to row #5

#Show rows 10 thru 15
#print df[9:16]
#print df[19:25]

#print df.info
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]
#print df.sort("type", ascending=False)
#print df[["chromosome","start","end"]]

#print df["start"][9:15]

#print df.shape #how many rows and columns
#df2 = df["start"]

#print df2.shape

#df2.to_csv("startColumn.txt", sep='\t', index=False)

#dataframe that has start codon less than 10

roi = df["start"] < 10 #region of interest
#print roi
#print type(roi)

print df[roi] # === print roi
#df[~roi].shape
print roi

