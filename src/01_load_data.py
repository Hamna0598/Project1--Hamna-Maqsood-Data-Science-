"""
===========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)
Module: 01 - Load and understand Dataset

Author: Hamna Maqsood
===========================================================
  """

# ===========================================================
# Import Libraries
# ===========================================================

import pandas as pd

# Function to Load Dataset
def load_dataset():

    # Read dataset from data folder
    df = pd.read_csv("data/Dataset for Data Analytics - Sheet1.csv")

    print("=" * 70)
    print("Dataset Loaded Successfully!")
    print("=" * 70)

    return df

# Function to display basic info
def dataset_overview(df):

    print("\n" + "=" * 70)
    print("Dataset Overview")
    print("=" * 70)

    # Shape of dataset
    rows, columns = df.shape

    print(f"\nNumber of Rows : {rows}")
    print(f"Number of Columns : {columns}")

    # Display first five records
    print("\nFirst Five Rows\n")
    print(df.head())

    #Display last five records
    print("\nLast Five Rows\n")
    print(df.tail())

    # Display column names
    print("\nColumn Names\n")
    print(df.columns.tolist())

    # Display info
    print("\nDataset Information\n")
    print(df.info())

    # Statistical summary
    print("\nStatistical Summary\n")
    print(df.describe())

    # Numerical columns
    numerical_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    # Categorical columns
    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    print("\nNumber of Numerical Columns :", len(numerical_columns))
    print("Number of Categorical Columns :", len(categorical_columns))

    print("\nNumerical Columns\n")
    print(list(numerical_columns))

    print("\nCategorical Columns\n")
    print(list(categorical_columns))

    # Check duplicate rows
    duplicates = df.duplicated().sum()

    print(f"\nDuplicate Rows : {duplicates}")

    # Check missing values
    missing = df.isnull().sum().sum()

    print(f"Total Missing Values : {missing}")

    # Target Variable
    print("\nTarget Variable : TotalPrice")

    print("\nFirst 10 Orders Prices\n")
    print(df["TotalPrice"].head(10))

    print("\nDataset Loaded and Explored Successfully.")


# =========================================================
# Main Function
# =========================================================

def main():
    df = load_dataset()
    dataset_overview(df)

# =========================================================
# Execute Program
# =========================================================

if __name__ == "__main__":
    main()