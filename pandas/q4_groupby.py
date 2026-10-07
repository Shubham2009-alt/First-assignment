import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000],
    "Experience": [2, 4, 3, 5, 6, 7, 1, 2]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")

print("Average Salary:")
print(grouped["Salary"].mean())

print("\nMaximum Salary:")
print(grouped["Salary"].max())

print("\nMinimum Salary:")
print(grouped["Salary"].min())

print("\nAverage Experience:")
print(grouped["Experience"].mean())

average_salary = grouped["Salary"].mean()

print("\nDepartment with Highest Average Salary:")
print(average_salary.idxmax())

print("\nEmployee Count:")
print(grouped["Employee"].count())

print("\nDepartments Sorted by Average Salary:")
print(average_salary.sort_values(ascending=False))
