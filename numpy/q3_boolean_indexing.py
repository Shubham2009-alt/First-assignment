import numpy as np

X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

print("People with age >= 25:")
print(X[X[:, 0] >= 25])

print("\nPeople with salary > 60000:")
print(X[X[:, 1] > 60000])

print("\nAge >= 25 AND Salary > 60000:")
print(X[(X[:, 0] >= 25) & (X[:, 1] > 60000)])

X_modified = X.copy()
X_modified[:, 1] = np.where(X_modified[:, 1] < 30000, 30000, X_modified[:, 1])

print("\nAfter replacing salaries below 30000:")
print(X_modified)

print("\nAverage Salary:", np.mean(X_modified[:, 1]))

print("Average Salary for Age >= 25:",
      np.mean(X_modified[X_modified[:, 0] >= 25, 1]))
