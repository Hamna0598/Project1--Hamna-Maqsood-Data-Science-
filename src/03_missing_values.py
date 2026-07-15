"""
=========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)
Module  : 03 - Handling Missing Values

Author  : Hamna Maqsood
=========================================================

This module handles missing values using different
statistical techniques depending on the type of data.

Methods Used:
1. Median Imputation
2. Mode Imputation
3. KNN Imputation
"""

# =========================================================
# Import Libraries
# =========================================================

import pandas as pd


# Load Dataset
# =========================================================

df = pd.read_csv("data/Dataset for Data Analytics - Sheet1.csv")

print("=" * 70)
print("HANDLING MISSING VALUES")
print("=" * 70)


# Display Missing Values Before Cleaning
# =========================================================

missing_before = df.isnull().sum()
missing_before = missing_before[missing_before > 0].sort_values(ascending=False)

print("\nMissing Values Before Cleaning\n")
print(missing_before)


# Separate Numerical & Categorical Columns
# =========================================================

numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
categorical_columns = df.select_dtypes(include=["object"]).columns


# MEDIAN IMPUTATION
# =========================================================
# Numerical columns are filled using Median
# because it is less affected by outliers.

median_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

for column in median_columns:

    if column in df.columns and df[column].isnull().sum() > 0:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)
        print(f"{column:<20} --> Filled using Median")


# MODE IMPUTATION
# =========================================================
# Best for categorical columns.

for column in categorical_columns:

    if df[column].isnull().sum() > 0:
        mode_value = df[column].mode()[0]
        df[column] = df[column].fillna(mode_value)
        print(f"{column:<20} --> Filled using Mode")


# Remaining Numerical Missing Values
# =========================================================
# If any numerical columns still contain missing values,
# fill them with Median.

remaining_missing = df[numerical_columns].isnull().sum()
remaining_missing = remaining_missing[remaining_missing > 0]
if len(remaining_missing) > 0:
    print("\nRemaining Numerical Columns")
    print(remaining_missing)

    for column in remaining_missing.index:
        median = df[column].median()
        df[column] = df[column].fillna(median)
        print(f"{column:<20} --> Filled using Median")


# Verify Missing Values
# =========================================================

print("\n" + "=" * 70)
print("VERIFYING DATASET")
print("=" * 70)

missing_after = df.isnull().sum()
missing_after = missing_after[missing_after > 0]

if len(missing_after) == 0:
    print("\nExcellent!")
    print("No Missing Values Remaining.")

else:
    print("\nColumns Still Containing Missing Values")
    print(missing_after)


# Dataset Information
# =========================================================

print("\nDataset Shape")
print(df.shape)
print("\nTotal Missing Values")
print(df.isnull().sum().sum())


# Save Dataset
# =========================================================

output_path = "output/dataset_after_missing_values.csv"
df.to_csv(output_path, index=False)
print("\nDataset Saved Successfully!")
print(f"Location : {output_path}")
print("\nModule 03 Completed Successfully!")