import pandas as pd 
import xlrd
import os
data = pd.read_csv("rep_candidates.csv", encoding='cp1252')
trumpendorsed = data.loc[data["Trump Endorsed?"] == "Yes"]
trumpendorsed.to_csv("trump_endorsed.csv")
trumpnotendorsed = data.loc[data["Trump Endorsed?"] == "No"]
trumpnotendorsed.to_csv("trump_not_endorsed.csv")
print(os.getcwd())