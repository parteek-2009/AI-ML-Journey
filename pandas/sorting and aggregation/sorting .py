import pandas as pd 
df = pd.DataFrame({
    "employee": ["Aman", "Riya", "Karan", "Neha", "Aman", "Riya", "Karan", "Neha"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "salary": [50000, 62000, 48000, 71000, 54000, 60000, 75000, 58000],
    "experience": [2, 5, 1, 7, 3, 4, 8, 2],
    "rating": [4.2, 4.8, 3.9, 4.6, 4.1, 4.7, 4.9, 4.0]
})

#sorting single columns
df.sort_values(by="salary",ascending=True,inplace=True)
# print(df)
#sorting multiple columns(used when some data of a column is same)
df.sort_values(by=["salary","employee"],ascending=True,inplace=True)
print(df)