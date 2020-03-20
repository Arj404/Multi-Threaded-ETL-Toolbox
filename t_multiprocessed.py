from multiprocessing import  Pool
import time
start_time = time.time()
import pandas as pd
import numpy as np

df = pd.read_csv("data-export.csv",names=['a','b','c','d','e','f','g','h','i'])
data = []
n,m = df.shape
t = n/100
size = n/50
s = 100
c=0
print(df.head())

def fun(df):
	df['a'] = 0.4251*df['a']
	df['c'] = 0.393700*df['c']
	df['d'] = 745.7*df['d']
	df['e'] = 2.20462*df['e']
	df['g'] = 1900+df['g']
	df['i'] = df['i'].str.upper()
	return df

def parallelize_dataframe(df, func, n_cores=int(50)):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df
df = parallelize_dataframe(df, fun)

df.to_csv('data-import.csv',header=False)
print("--- %s seconds ---" % (time.time() - start_time))
import os
os.system('say "transforming data finished"')