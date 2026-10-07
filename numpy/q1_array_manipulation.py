import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

print("Shape:", X.shape)
print("Dimensions:", X.ndim)
print("Data Type:", X.dtype)

print("\nSecond Column:")
print(X[:, 1])

print("\nFirst Two Rows:")
print(X[:2, :])

print("\nLast Two Columns:")
print(X[:, -2:])

X_modified = X.copy()
X_modified[X_modified > 80] = 0

print("\nArray after replacing values greater than 80 with 0:")
print(X_modified)

print("\nMinimum:", np.min(X, axis=0))
print("Maximum:", np.max(X, axis=0))
print("Mean:", np.mean(X, axis=0))
print("Standard Deviation:", np.std(X, axis=0))
