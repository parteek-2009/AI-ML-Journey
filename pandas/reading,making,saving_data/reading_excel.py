"""in excel or json files this we dont need encoding """
import pandas as pd
df = pd.read_excel("SampleSuperstore.xlsx")
print(df)