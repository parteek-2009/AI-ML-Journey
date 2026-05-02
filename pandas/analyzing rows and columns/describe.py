"""It shows basic stats for numerical columns:

count (non-null values)
mean (average)
std (standard deviation)
min (smallest value)
25% (1st quartile)
50% (median)
75% (3rd quartile)
max (largest value)"""

import pandas as pd
data = {
    "name" : ["ram","shyam","rakesh","mukesh"],
    "age" : [20, 30, 40, 32],
    "job" : ["peon" , "teacher", "cleaner", "gym-trainer"]
}
dataf = pd.DataFrame(data)
print(dataf.describe())