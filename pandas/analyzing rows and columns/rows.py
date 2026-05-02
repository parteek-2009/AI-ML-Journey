"we will see how to access a specific number of rows from top or bottom"
import pandas as pd
data = pd.read_csv(r"C:\Users\PARTEEK\OneDrive\Desktop\pandas\files for practice\sales_data_sample.csv",encoding="latin1")
print("first 5 rows of data are:")
print(data.head(5))#default value is 5
print("last 5 rows of data are:")
print(data.tail(5))#default value is 5