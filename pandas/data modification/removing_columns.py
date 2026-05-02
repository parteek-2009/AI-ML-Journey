"""we will use drop function here to remove a specific rows"""

import pandas as pd
data = pd.read_csv(r"C:\Users\PARTEEK\OneDrive\Desktop\pandas\files for practice\sales_data_sample.csv",encoding="latin1")
working_data = data.head(10)
print(working_data.columns)
"""we have two methods to delete the data here
1. updating the original data
2. making new variable and storing that data inside that leaving the original data untouched"""
#making new data

new_data = working_data.drop(columns=['ORDERLINENUMBER','SALES',
       'ORDERDATE', 'STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID',
       'PRODUCTLINE', 'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'PHONE',
       'ADDRESSLINE1', 'ADDRESSLINE2', 'CITY', 'STATE', 'POSTALCODE',
       'COUNTRY', 'TERRITORY', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME',
       'DEALSIZE'], inplace=False)
print(new_data)#inplace has to be false if its true the original data will get updated and storing no data inside new vairable

#updating the original data
working_data.drop(columns=['ORDERLINENUMBER','SALES',
       'ORDERDATE', 'STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID',
       'PRODUCTLINE', 'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'PHONE',
       'ADDRESSLINE1', 'ADDRESSLINE2', 'CITY', 'STATE', 'POSTALCODE',
       'COUNTRY', 'TERRITORY', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME',
       'DEALSIZE'], inplace=True)
print(working_data)