import pandas as pd

# Employees table
employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["Aman", "Riya", "Karan", "Neha", "Simran", "Vikas"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT"]
})

# Salaries table
salaries = pd.DataFrame({
    "emp_id": [101, 102, 103, 105, 106, 107],
    "salary": [50000, 62000, 48000, 58000, 60000, 70000],
    "bonus": [5000, 7000, 4000, 4500, 6000, 8000]
})

# Performance table
performance = pd.DataFrame({
    "emp_id": [101, 102, 104, 105, 106],
    "rating": [4.2, 4.8, 4.6, 4.1, 4.7]
})

combined1 = pd.merge(employees,salaries,on="emp_id",how="left")
combined2 = pd.merge(employees,performance,on="emp_id",how="left")
all_combined = pd.merge(combined1,combined2,on="emp_id",how="left")
print(all_combined)