"""we will create a dataframe and save it into
csv,json and excel"""
import pandas as pd
every_project_granted = {
    "projects": ["chatbot","automating systems","agent","workflow"],
    "money": [1000000, 2000000, 1500000, 2400000],
    "time taken": ["1 week" , "1.5 weeks" , "2 weeks" , "2 weeks"]
}
data = pd.DataFrame(every_project_granted)
# data.to_csv("project_details.csv", index=False)
# data.to_json("project_details.json", index=False)
data.to_excel("project.xlsx", index=False)
