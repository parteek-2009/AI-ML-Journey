import pandas as pd

# January sales
jan_sales = pd.DataFrame({
    "emp_id": [101, 102, 103],
    "employee": ["Aman", "Riya", "Karan"],
    "sales": [50000, 62000, 48000]
})

# February sales
feb_sales = pd.DataFrame({
    "emp_id": [104, 105, 106],
    "employee": ["Neha", "Simran", "Vikas"],
    "sales": [71000, 58000, 60000]
})

# Bonus data (same employees as January)
bonus_data = pd.DataFrame({
    "bonus": [5000, 7000, 4000],
    "rating": [4.2, 4.8, 3.9]
})

data = pd.concat([jan_sales,feb_sales],axis=0)
# print(data)
bonus_combined = pd.concat([jan_sales,bonus_data],axis=1)
