"""now"""
import pandas as pd
dic = {
    "friends": ["friendA", "friendB", None, "friendD", "friendE"],
    "money": [1000000, 10000, 150000, 100000, 500000],
    "time taken": ["2 years", "5 years", "5 years", "3 years", "5year"],
    "age": [21, 25, 19, 23, 25],
    "projects completed": [5, 2, 3, 2, 8]
}

data = pd.DataFrame(dic)
print(data)
#removing whole columns
data.dropna(axis=0,inplace=True)
#removing whole rows
data.dropna(axis=1,inplace=True)

"""if none is very frequent then you cant do this
due to huge data lose"""