"""
=========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)
Module  : 04 - Outlier Detection & Treatment

Author  : Hamna Maqsood
=========================================================

This module detects outliers using:

1. IQR Method
2. Z-Score Method

Outlier Treatment:
Outlier Treatment:
IQR Capping is used because numerical features may
contain extreme values, and IQR is robust to outliers.
"""

# =========================================================
# Import Libraries
# =========================================================

import pandas as pd
import numpy as np
from scipy.stats import zscore


# Load Dataset
# =========================================================

df = pd.read_csv("output/dataset_after_missing_values.csv")

print("=" * 70)
print("OUTLIER DETECTION")
print("=" * 70)


# Numerical Columns
# =========================================================

numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns


# IQR OUTLIER DETECTION
# =========================================================

print("\nDetecting Outliers using IQR...\n")

iqr_summary = {}

for column in numerical_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower) |
        (df[column] > upper)
    ]
    iqr_summary[column] = len(outliers)

print("=" * 70)
print("IQR OUTLIERS")
print("=" * 70)

for column, count in iqr_summary.items():
    if count > 0:
        print(f"{column:<25} : {count}")


# IQR OUTLIER TREATMENT
# =========================================================
# Cap values instead of deleting rows.

print("\nApplying IQR Capping...\n")

for column in numerical_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[column] = df[column].clip(lower=lower, upper=upper)

print("IQR Capping Completed Successfully.")


# Z-SCORE DETECTION
# =========================================================
# Used only for comparison.
# No rows are removed.

print("\nDetecting Outliers using Z-Score...\n")

z_scores = np.abs(
    zscore(df[numerical_columns])
)
zscore_summary = {}

for index, column in enumerate(numerical_columns):

    count = (z_scores[:, index] > 3).sum()

    zscore_summary[column] = count

print("=" * 70)
print("Z-SCORE OUTLIERS")
print("=" * 70)

for column, count in zscore_summary.items():

    if count > 0:
        print(f"{column:<25} : {count}")


# Comparison
# =========================================================

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

print("IQR Method  : Used for detecting and treating outliers.")
print("Z-Score     : Used only for comparison.")
print("Reason      : IQR is robust to extreme values")
print("              and works well for numerical business data.")


# Verify Dataset
# =========================================================

print("\nDataset Shape After Treatment")
print(df.shape)

# =========================================================
# Save Dataset
# =========================================================

output_file = "output/dataset_after_outliers.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nDataset Saved Successfully!")
print(f"Location : {output_file}")
print("\nModule 04 Completed Successfully!")