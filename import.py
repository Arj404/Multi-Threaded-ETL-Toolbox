import sqlite3
connection = sqlite3.connect("cars-database.db")
crsr = connection.cursor()
sql_command = """"""
sql_command = """CREATE TABLE cars (  
mpg INTEGER PRIMARY KEY,  
cylinders VARCHAR(20),  
displacement INTEGER,  
horsepower INTEGER,  
weight INTEGER,
acceleration INTEGER,
modelyear INTEGER,
origin INTEGER,
carname TEXT);"""

crsr.execute(sql_command)
