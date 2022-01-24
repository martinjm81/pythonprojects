import pandas as pd
jam_data = pd.read_csv("jamData.csv")
print("number of participants: ", len(jam_data))

jam_data = jam_data.drop_duplicates(subset=["name / nickname (optional)"])
print("number of participants: ", len(jam_data))
