import sqlite3
import pandas as pd

# .open cars-database.db
connection = sqlite3.connect("cars-database.db")
crsr = connection.cursor()


sql = """SELECT * from cars"""
crsr.execute(sql)
data = crsr.fetchall();
df = pd.DataFrame(data)
df.to_csv('data-export.csv')
connection.commit()
connection.close()