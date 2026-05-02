"""
In this we have two methods to add columns
1. Assinging method
2. Inserting method
"""

import pandas as pd
dic = {
    "friends" : ["friendA", "friendB", "friendC"],
    "money" : [10000000 , 100000, 100000]
}
data = pd.DataFrame(dic)


"""Assinging method"""
data["time taken"] = ["2 years", "5 years", "3 years"]
print(data)

"""Inserting method"""
data.insert(2,"happiness",[100,45,50])
print(data)