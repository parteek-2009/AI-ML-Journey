"""we can access a particular data by giving applying filteration method"""
import pandas as pd

every_project_granted = {
    "projects": ["chatbot","automating systems","agent","workflow"],
    "money": [100, 200, 150, 250],
    "time taken": [1 , 1.5 , 2 , 2]
}
data = pd.DataFrame(every_project_granted)
huge = data[data["money"] > 230]#single condition


"""now lets put multiple conditions"""
big = data[(data["money"] > 150) & (data["time taken"] >1.5)]#multiple conditions
# print(big)

"""using OR in dataset"""
dataset_or = data[(data["money"]>150) | (data["time taken"]>1.5)]
print(dataset_or)
