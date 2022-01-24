import sqlite3
import pandas as pd
data = pd.read_csv("bmi.csv", sep="\t"
print(data)

import sqlite3
connection = sqlite3.connect("gta.db")
gta_data = pd.read_sql("select * from gta", connection)  #table
print(gta_data)

print(gta_data.head(2))
print(gta_data.tail(2))

filtered_row  = gta_data[ gta_data["city"] =="Liberty City"]
print(filtered_row)

replace_city = gta_data.replace("Liberty City", "New York")
print(replaced_city)

#eliminar datos
remove_column=gta_data.drop("city", axis=1)
print(remove_column)

remove_column = gta_data.drop(["city","release_year"], axis=1)
print(remove_column)

remove_row = gta_data.iloc[1:4]
print(remove_row)

#agregar filas
row = {"release_year": "2021",
        "release_name": "Natural Vision Evolved",
        "city": "Los Angeles"}
new_row_data = gta_data.append(row, ignore_index=True)
print(new_row_data)

