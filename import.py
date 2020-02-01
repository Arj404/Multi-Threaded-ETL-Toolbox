import sqlite3
connection = sqlite3.connect("cars-database.db")
crsr = connection.cursor()
sql_command = """"""
sql_command = """CREATE TABLE newcars (  
staff_number INTEGER PRIMARY KEY,  
fname VARCHAR(20),  
lname VARCHAR(30),  
gender CHAR(1),  
joining DATE);"""
  
crsr.execute(sql_command) 