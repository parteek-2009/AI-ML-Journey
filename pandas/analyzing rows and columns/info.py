""" with info we will find the information related to the dataset"""
import pandas as pd 
data = pd.read_json(r"C:\Users\PARTEEK\OneDrive\Desktop\pandas\files for practice\sample_Data.json")
print(data.info())