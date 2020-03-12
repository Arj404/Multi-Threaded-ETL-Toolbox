import time
start_time = time.time()
import pandas as pd

df = pd.read_csv("data-export.csv",header=[0,20])
n,m = df.shape
t = n/100
c=0
# for i in range(n):
# 	df.iloc[i,0] = 0.4251*df.iloc[i,0]
# 	df.iloc[i,2] = 0.393700*df.iloc[i,2]
# 	df.iloc[i,3] = 745.7*df.iloc[i,3]
# 	df.iloc[i,4] = 2.20462*df.iloc[i,4]
# 	df.iloc[i,6] = 1900+df.iloc[i,6]
# 	df.iloc[i,8] = df.iloc[i,8].upper()
# 	if(i%100==0):
# 		c=c+1
# 		print("-----process {} out of {} is completed-----".format(c,t))

#df.to_csv('data-import.csv',index = False)
print(df)
print("--- %s seconds ---" % (time.time() - start_time))
import os
#os.system('say "transforming data finished"')