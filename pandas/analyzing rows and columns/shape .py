"""we will see how to get a shape of a dataset """
import pandas as pd
data = {
    "name" : ["ram","shyam","rakesh","mukesh"],
    "age" : [20, 30, 40, 32],
    "job" : ["peon" , "teacher", "cleaner", "gym-trainer"]
}
dataf = pd.DataFrame(data)
print(f"shape:" ,dataf.shape)