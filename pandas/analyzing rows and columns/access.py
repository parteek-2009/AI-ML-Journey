"""with this we can access data inside specific rows and perform operations"""
import pandas as pd
every_project_granted = {
    "projects": ["chatbot","automating systems","agent","workflow"],
    "money": [1000000, 2000000, 1500000, 2400000],
    "time taken": ["1 week" , "1.5 weeks" , "2 weeks" , "2 weeks"]
}
data = pd.DataFrame(every_project_granted)
moneyy = data["money"]#accessing single column
both = data[["money","projects"]]#accessing multiple columns
print(both)