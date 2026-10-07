import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 22, 30, 28],
    "Marks": [85, 72, 90, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("First 3 Rows:")
print(df.head(3))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nName and Marks:")
print(df[["Name", "Marks"]])

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))
