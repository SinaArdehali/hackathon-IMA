import pandas as pd
import phonem_to_lpc  as lpc

df = pd.read_csv('assets/fra.txt', sep='\t', names=["us", "fr"], chunksize=500, skiprows=80000)
for chunk in df:
    chunk.drop(["us"], axis=1,  inplace=True)
    chunk['cued'] = chunk['fr'].apply(lpc.code)
    chunk.to_csv("assets/test.csv", mode="a", header=False, index=False,  sep="\t")