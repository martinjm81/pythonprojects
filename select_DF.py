import sqlite3
import pandas as pd
data = pd.read_csv("bmi.csv", sep="\t"
print(data)

import sqlite3
connection = sqlite3.connect("gta.db")
gta_data = pd.read_sql("select * from gta", connection)  #table
print(gta_data)