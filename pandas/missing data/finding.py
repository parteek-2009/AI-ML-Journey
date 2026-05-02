"""there are two things in it
NaN = for missing numbers(not a number)
none = for missing objects
"""
import pandas as pd
dic = {
    "friends": ["friendA", "friendB", None, "friendD", "friendE"],
    "money": [1000000, None, 150000, None, 500000],
    "time taken": ["2 years", "5 years", None, "3 years", None],
    "age": [21, None, 19, 23, None],
    "projects completed": [5, 2, None, None, 8]
}

data = pd.DataFrame(dic)
#using isnull method to find where are the missing values
print(data.isnull())#False means no missing value, True means missing value
#finding number of missing values
print(data.isnull().sum())