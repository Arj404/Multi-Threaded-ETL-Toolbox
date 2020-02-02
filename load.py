import time
start_time = time.time()
import sqlite3
import pandas as pd

# .open cars-database.db
connection = sqlite3.connect("cars-database.db")
crsr = connection.cursor()

sql = """DROP TABLE IF EXISTS cars_new;"""
crsr.execute(sql)

sql = """CREATE TABLE cars_new (  
mpg INTEGER,  
cylinders INTEGER,  
displacement INTEGER,  
horsepower INTEGER,  
weight INTEGER,
acceleration INTEGER,
modelyear INTEGER,
origin INTEGER,
carname TEXT);"""
crsr.execute(sql)

df = pd.read_csv("data-import.csv")
n,m = df.shape
for i in range(n):
	sql = """INSERT INTO cars_new (
   		mpg, cylinders, displacement, horsepower, weight, acceleration, modelyear, origin, carname) VALUES 
   		({},{},{},{},{},{},{},{},"{}");""".format(df.iloc[i,0], df.iloc[i,1], df.iloc[i,2], df.iloc[i,3], df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,7], df.iloc[i,8])
	crsr.execute(sql)

connection.commit()
connection.close()
print("--- %s seconds ---" % (time.time() - start_time))
import os
os.system('say "Data Loaded"')