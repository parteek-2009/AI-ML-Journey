""" we can get some numerical summary values of our data
1. sum
2. mean
3. min
4. max"""
import pandas as pd
df = pd.DataFrame({
    "employee": ["Aman", "Riya", "Karan", "Neha", "Aman", "Riya", "Karan", "Neha"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "salary": [50000, 62000, 48000, 71000, 54000, 60000, 75000, 58000],
    "experience": [2, 5, 1, 7, 3, 4, 8, 2],
    "rating": [4.2, 4.8, 3.9, 4.6, 4.1, 4.7, 4.9, 4.0]
})
minimum = df["salary"].min()
maximum_exp = df["experience"].max()
print(maximum_exp)