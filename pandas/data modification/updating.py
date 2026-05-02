"""we will update existing values using loc method"""
import pandas as pd

every_project_granted = {
    "projects": ["chatbot","automating systems","agent","workflow"],
    "money": [100, 200, 150, 250],
    "time taken": [1 , 1.5 , 2 , 2]
}
data = pd.DataFrame(every_project_granted)

"""updating single row and column value"""
data.loc[0,"time taken"] = 1.5

"""udating all values in a specific column
we will not use loc here"""
data["time taken"] = data["time taken"] + 1

"""making a new column with same method"""
data["time taken2"] = data["time taken"] + 1
print(data)