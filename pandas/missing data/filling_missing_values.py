import pandas as pd
employee_data = {
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["Aman", "Riya", "Vikram", "Neha", None, "Karan"],
    "age": [25, 28, None, 30, 27, 26],
    "department": ["IT", "HR", "IT", None, "Finance", "IT"],
    "salary": [50000, 60000, 55000, None, 70000, 52000],
    "experience_years": [2, 5, 3, 6, None, 4]
}
data = pd.DataFrame(employee_data)
print(data)
# Filling with a default value 
"""data.fillna("salary",0,inplace=True)"""#it will give an error because there are some string values also
#filling with specific values 
data["experience_years"]= data["experience_years"].fillna(data["experience_years"].mean())
data["salary"] = data["salary"].fillna(data["salary"].mean())
data["department"] = data["department"].fillna("IT")
data["age"] = data["age"].fillna(data["age"].mean())
print(data)