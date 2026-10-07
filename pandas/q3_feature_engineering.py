import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [80, 60, 90, 70, 85, 55],
    "Science": [75, 65, 95, 72, 80, 60],
    "English": [85, 70, 88, 75, 90, 50]
}

df = pd.DataFrame(data)

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Passed"] = df["Average"] >= 60

print("DataFrame:")
print(df)

print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])

print("\nStudents with Average >= 80:")
print(df[df["Average"] >= 80])

print("\nSorted by Average:")
print(df.sort_values(by="Average", ascending=False))

print("\nOverall Average:")
print(df["Average"].mean())

print("\nName, Average and Passed:")
print(df[["Name", "Average", "Passed"]])
