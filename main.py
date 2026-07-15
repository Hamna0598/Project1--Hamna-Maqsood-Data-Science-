"""
=========================================================
Project : E-Commerce Orders - Exploratory Data Analysis (EDA)

Main File

Run this file to execute the complete project.

Author : Hamna Maqsood
=========================================================
"""

import subprocess
import sys

print("=" * 70)
print("STARTING E-COMMERCE ORDERS EDA PROJECT")
print("=" * 70)


modules = [
    "src/01_load_data.py",
    "src/02_eda.py",
    "src/03_missing_values.py",
    "src/04_outliers.py",
    "src/05_feature_engineering.py",
    "src/06_save_dataset.py"
]


for module in modules:

    print("\n" + "=" * 70)
    print(f"Running : {module}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, module]
    )

    if result.returncode != 0:

        print(f"\nError while executing {module}")

        break

print("\n" + "=" * 70)
print("PROJECT EXECUTION FINISHED")
print("=" * 70)