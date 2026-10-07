# First Assignment - Pandas and NumPy

This repository contains my first assignment covering basic NumPy and Pandas operations.

## Structure

- `numpy/` contains five programs covering arrays, normalization, boolean indexing, matrix operations, and a small preprocessing pipeline.
- `pandas/` contains five programs covering DataFrames, missing values, feature engineering, groupby operations, and preprocessing.

## Requirements

- Python 3
- NumPy
- Pandas

Install the required libraries with:

```bash
pip install numpy pandas
```

## Running the programs

Run any program from the repository root. For example:

```bash
python numpy/q1_array_manipulation.py
python pandas/q1_dataframe_basics.py
```

Each file contains the complete program for its respective question.

## Note

The NumPy matrix-operations program uses the pseudoinverse when calculating the weights. For the given data, the design matrix contains linearly dependent columns, so the regular matrix inverse is not suitable.
