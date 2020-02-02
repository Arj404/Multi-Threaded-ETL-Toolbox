import pandas as pd

df = pd.read_csv("data-export.csv",header=None)
n,m = df.shape
for i in range(n):
	df.iloc[i,0] = 0.4251*df.iloc[i,0]
	df.iloc[i,2] = 0.393700*df.iloc[i,2]
	df.iloc[i,3] = 745.7*df.iloc[i,3]
	df.iloc[i,4] = 2.20462*df.iloc[i,4]
	df.iloc[i,5] = 0.393700*df.iloc[i,5]
	df.iloc[i,6] = 0.393700*df.iloc[i,6]
	
	


df.to_csv('data-import.csv')