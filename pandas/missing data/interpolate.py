""" interpolate method fill out numerical values of rows and columns with
best estimation, it works only with numerical data
it contains methods 
the most common ones are: linear,polynomial and other"""
import pandas as pd
dic = {
    "friends": ["friendA", "friendB", None, "friendD", "friendE"],
    "money": [100000, None, 150000, None, 500000],
    "time taken": ["2 years", "5 years", None, "3 years", None],
    "age": [21, None, 19, 23, None],
    "projects completed": [5, 2, None, None, 8]
}
data = pd.DataFrame(dic)
data["money"] = data["money"].interpolate(method = "linear")
data["age"] = data["age"].interpolate(method="linear")
print(data)