"""
=========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)
Module  : 05 - Feature Engineering

Author  : Hamna Maqsood
=========================================================

Feature Engineering means creating new useful features
from existing columns to improve machine learning models.
"""

# =========================================================
# Import Libraries
# =========================================================

import pandas as pd
import numpy as np


# Load Dataset
# =========================================================

df = pd.read_csv("output/dataset_after_outliers.csv")

print("=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)


# Convert Date Column
# =========================================================

df["Date"] = pd.to_datetime(df["Date"])


# Feature 1 : Order Year
# =========================================================
# Extract year from order date

df["OrderYear"] = df["Date"].dt.year
print("OrderYear Created")


# Feature 2 : Order Month
# =========================================================
# Extract month from order date

df["OrderMonth"] = df["Date"].dt.month
print("OrderMonth Created")


# Feature 3 : Order Day
# =========================================================
# Extract day from order date

df["OrderDay"] = df["Date"].dt.day
print("OrderDay Created")


# Feature 4 : Day of Week
# =========================================================
# Extract weekday name

df["DayOfWeek"] = df["Date"].dt.day_name()
print("DayOfWeek Created")


# Feature 5 : Is Coupon Used
# =========================================================
# 1 = Coupon Applied
# 0 = No Coupon

df["IsCouponUsed"] = np.where(
    df["CouponCode"].notna(),
    1,
    0
)
print("IsCouponUsed Created")


# Feature 6 : Average Item Price
# =========================================================
# Average price per purchased item

df["AverageItemPrice"] = (
    df["TotalPrice"] / df["Quantity"]
)
print("AverageItemPrice Created")


# Feature 7 : Cart Value
# =========================================================
# Estimated cart value

df["CartValue"] = (
    df["ItemsInCart"] * df["UnitPrice"]
)
print("CartValue Created")


# Feature 8 : Bulk Order
# =========================================================
# Orders with quantity >= 3

df["BulkOrder"] = np.where(
    df["Quantity"] >= 3,
    1,
    0
)
print("BulkOrder Created")


# Feature 9 : High Value Order
# =========================================================
# Orders above median Total Price

median_price = df["TotalPrice"].median()

df["HighValueOrder"] = np.where(
    df["TotalPrice"] > median_price,
    1,
    0
)
print("HighValueOrder Created")


# Feature 10 : Discount Applied
# =========================================================
# 1 = Discount Used
# 0 = No Discount

df["DiscountApplied"] = np.where(
    df["CouponCode"].notna(),
    1,
    0
)
print("DiscountApplied Created")


# =========================================================
# Display New Features
# =========================================================

print("\n" + "=" * 70)
print("NEW FEATURES CREATED")
print("=" * 70)

new_features = [
    "OrderYear",
    "OrderMonth",
    "OrderDay",
    "DayOfWeek",
    "IsCouponUsed",
    "AverageItemPrice",
    "CartValue",
    "BulkOrder",
    "HighValueOrder",
    "DiscountApplied"
]
print(df[new_features].head())


# =========================================================
# Correlation with TotalPrice
# =========================================================

print("\n" + "=" * 70)
print("CORRELATION OF NEW FEATURES WITH TOTAL PRICE")
print("=" * 70)

correlation = df.select_dtypes(include=["int64", "float64"]).corr()

print(
    correlation["TotalPrice"]
    .sort_values(ascending=False)
)


# =========================================================
# Dataset Information
# =========================================================

print("\nDataset Shape")
print(df.shape)

print("\nTotal Columns After Feature Engineering :")
print(len(df.columns))


# =========================================================
# Save Dataset
# =========================================================

df.to_csv(
    "output/final_engineered_dataset.csv",
    index=False
)

print("\nFinal Engineered Dataset Saved Successfully.")
print("Location : output/final_engineered_dataset.csv")
print("\nModule 05 Completed Successfully!")