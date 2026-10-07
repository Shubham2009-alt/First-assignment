import numpy as np

X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

print("Column Means:")
print(mean)

print("\nColumn Standard Deviations:")
print(std)

X_scaled = (X - mean) / std

print("\nScaled Matrix:")
print(X_scaled)

print("\nMean of Scaled Columns:")
print(np.mean(X_scaled, axis=0))

print("\nStandard Deviation of Scaled Columns:")
print(np.std(X_scaled, axis=0))
