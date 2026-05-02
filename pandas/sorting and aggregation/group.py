import pandas as pd
"""All the aggregation functions are here:
1. mean
2. minimum
3. maximum
4. count
5. std"""
df = pd.DataFrame({
    "employee": ["Aman", "Riya", "Karan", "Neha", "Simran", "Vikas", "Priya", "Arjun"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "salary": [50000, 62000, 48000, 71000, 58000, 60000, 69000, 55000],
    "experience": [2, 5, 1, 7, 3, 4, 6, 2],
    "rating": [4.2, 4.8, 3.9, 4.6, 4.1, 4.7, 4.5, 4.0]
})

department_grouped = df.groupby("department")["salary"].mean()
print(department_grouped)
minimum_exp = df.groupby("department")["experience"].min()
print(minimum_exp)
total_salary = df.groupby("department")["salary"].sum()
print(total_salary)
grouped = df.groupby("department")[["salary","experience"]].mean()
print(grouped)