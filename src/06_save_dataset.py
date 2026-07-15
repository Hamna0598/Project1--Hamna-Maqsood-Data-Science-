"""
=========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)
Module  : 06 - Save Final Dataset & Generate Report

Author  : Hamna Maqsood
=========================================================
"""

# =========================================================
# Import Libraries
# =========================================================

import pandas as pd
import os


# Create Output Folder
# =========================================================

os.makedirs("output", exist_ok=True)


# Load Original & Final Dataset
# =========================================================

original_df = pd.read_csv("data/Dataset for Data Analytics - Sheet1.csv")
final_df = pd.read_csv("output/final_engineered_dataset.csv")

print("=" * 70)
print("FINAL PROJECT SUMMARY")
print("=" * 70)


# Dataset Information
# =========================================================

rows, columns = final_df.shape

print(f"\nTotal Rows    : {rows}")
print(f"Total Columns : {columns}")


# Missing Values
# =========================================================

missing = final_df.isnull().sum().sum()
print(f"\nMissing Values Remaining : {missing}")


# Duplicate Rows
# =========================================================

duplicates = final_df.duplicated().sum()
print(f"Duplicate Rows : {duplicates}")


# Numerical & Categorical Columns
# =========================================================

numerical_columns = final_df.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_columns = final_df.select_dtypes(
    include=["object"]
).columns

print(f"\nNumerical Columns : {len(numerical_columns)}")
print(f"Categorical Columns : {len(categorical_columns)}")


# Automatically Detect New Features
# =========================================================

original_columns = set(original_df.columns)

new_features = [
    column
    for column in final_df.columns
    if column not in original_columns
]
print("\n" + "=" * 70)
print("ENGINEERED FEATURES")
print("=" * 70)

for feature in new_features:
    print(f" {feature}")


# Correlation of New Features
# =========================================================

print("\n" + "=" * 70)
print("CORRELATION WITH TOTAL PRICE")
print("=" * 70)

correlation = (
    final_df.select_dtypes(include=["int64", "float64"])
    .corr()["TotalPrice"]
    .sort_values(ascending=False)
)
print(correlation)

# =========================================================
# Save Final Dataset
# =========================================================

output_dataset = "output/cleaned_dataset.csv"

final_df.to_csv(
    output_dataset,
    index=False
)
print("\nFinal Dataset Saved Successfully!")

# =========================================================
# Generate Summary Report
# =========================================================

report_file = "output/summary_report.txt"

with open(report_file, "w") as report:

    report.write("=" * 70 + "\n")
    report.write("E-COMMERCE ORDERS DATASET PROJECT REPORT\n")
    report.write("=" * 70 + "\n\n")

    report.write(f"Total Rows : {rows}\n")
    report.write(f"Total Columns : {columns}\n\n")

    report.write(f"Missing Values Remaining : {missing}\n")
    report.write(f"Duplicate Rows : {duplicates}\n\n")

    report.write(f"Numerical Columns : {len(numerical_columns)}\n")
    report.write(f"Categorical Columns : {len(categorical_columns)}\n\n")

    report.write("Engineered Features:\n")

    for feature in new_features:
        report.write(f"- {feature}\n")

    report.write("\n")

    report.write("Modules Completed\n")
    report.write("-------------------------\n")
    report.write("Module 01 : Data Loading\n")
    report.write("Module 02 : Exploratory Data Analysis\n")
    report.write("Module 03 : Missing Value Handling\n")
    report.write("Module 04 : Outlier Detection & Treatment\n")
    report.write("Module 05 : Feature Engineering\n")
    report.write("Module 06 : Final Dataset & Report\n")

    report.write("\n")

    report.write("Techniques Used\n")
    report.write("-------------------------\n")
    report.write("- Median Imputation\n")
    report.write("- Mode Imputation\n")
    report.write("- IQR Outlier Detection\n")
    report.write("- IQR Outlier Capping\n")
    report.write("- Z-Score Comparison\n")
    report.write("- Feature Engineering\n")

print("\nSummary Report Generated Successfully!")
print(f"Location : {report_file}")

# =========================================================
# Project Completed
# =========================================================

print("\n" + "=" * 70)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nGenerated Files")

print("cleaned_dataset.csv")
print("final_engineered_dataset.csv")
print("summary_report.txt")
print("All EDA plots")

print("\nDataset is now cleaned, engineered, and ready for Machine Learning.")