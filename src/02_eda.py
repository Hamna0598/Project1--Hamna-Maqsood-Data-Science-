"""
=========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)
Module  : 02 - Exploratory Data Analysis (EDA)

Author  : Hamna Maqsood
=========================================================
"""

# =========================================================
# Import Libraries
# =========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Plot Style
sns.set_style("whitegrid")

# Load Dataset
df = pd.read_csv("data/Dataset for Data Analytics - Sheet1.csv")


# Dataset Shape
print("=" * 70)
print("DATASET SHAPE")
print("=" * 70)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


# Missing values
print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

print(missing)


# Duplicate rows
print("\n" + "=" * 70)
print("DUPLICATE ROWS")
print("=" * 70)

duplicates = df.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")


# Numerical & Categorical Columns
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

categorical_columns = df.select_dtypes(include=["object"]).columns

print("\nNumber of Numerical Columns :", len(numerical_columns))
print("Number of Categorical Columns :", len(categorical_columns))


# Target Variable Statistics
print("\n" + "=" * 70)
print("TOTAL PRICE STATISTICS")
print("=" * 70)

print(df["TotalPrice"].describe())


# Correlation with TotalPrice
print("\n" + "=" * 70)
print("TOP FEATURES CORRELATED WITH TOTAL PRICE")
print("=" * 70)

correlation = df.corr(numeric_only=True)
top_features = correlation["TotalPrice"].sort_values(ascending=False)
print(top_features.head(15))

# Create Output Folder
import os

os.makedirs("output/plots", exist_ok=True)


# Histogram - Total Price

plt.figure(figsize=(10,6))
sns.histplot(df["TotalPrice"], bins=30, kde=True)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/plots/totalprice_distribution.png")
plt.show()


# Boxplot - Total Price

plt.figure(figsize=(8,5))
sns.boxplot(x=df["TotalPrice"])
plt.title("Total Price Boxplot")
plt.tight_layout()
plt.savefig("output/plots/boxplot_totalprice.png")
plt.show()


# Correlation Heatmap

top_corr_features = correlation.index[:15]
plt.figure(figsize=(12,10))
sns.heatmap(
    df[top_corr_features].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/plots/correlation_heatmap.png")
plt.show()


# Missing Value Plot

plt.figure(figsize=(12,6))
missing.plot(kind="bar")
plt.title("Missing Values Per Column")
plt.xlabel("Columns")
plt.ylabel("Missing Count")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("output/plots/missing_values.png")
plt.show()


# Top 10 Products

plt.figure(figsize=(12,6))

sns.countplot(
    data=df,
    x="Product",
    order=df["Product"].value_counts().index
)
plt.xticks(rotation=90)
plt.title("Number of Orders by Product")
plt.tight_layout()
plt.savefig("output/plots/product_distribution.png")
plt.show()


# Scatter Plot

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Quantity",
    y="TotalPrice"
)
plt.title("Quantity vs Total Price")
plt.tight_layout()
plt.savefig("output/plots/quantity_vs_totalprice.png")
plt.show()

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)

print("Plots have been saved inside output/plots/")