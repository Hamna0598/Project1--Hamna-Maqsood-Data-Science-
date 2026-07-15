# E-Commerce Orders - Exploratory Data Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) and Feature Engineering on an E-Commerce Orders Dataset.

The objective is to clean the dataset, analyze its structure, handle missing values, detect and treat outliers, engineer new features, and prepare the data for Machine Learning applications.

---

## Dataset

E-Commerce Orders Dataset

Rows : 1200

Columns : 14

Target Variable : TotalPrice

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## Project Structure

E-Commerce_Orders_EDA_Project

```
data/

output/

src/

requirements.txt

README.md

main.py
```

---

## Modules

### Module 1

- Load Dataset
- Dataset Overview
- Data Types
- Dataset Shape
- Statistical Summary

---

### Module 2

- Exploratory Data Analysis (EDA)
- Missing Values Analysis
- Duplicate Records Detection
- Correlation Analysis
- Histogram
- Box Plot
- Heatmap
- Scatter Plot
- Product Distribution

---

### Module 3

- Missing Value Handling
- Median Imputation
- Mode Imputation
- Missing Value Verification

---

### Module 4

- Outlier Detection
- IQR Method
- Z-Score Method
- IQR Outlier Capping
- Outlier Comparison

---

### Module 5

Feature Engineering

- OrderYear
- OrderMonth
- OrderDay
- DayOfWeek
- IsCouponUsed
- AverageItemPrice
- CartValue
- BulkOrder
- HighValueOrder
- DiscountApplied

---

### Module 6

- Save Final Dataset
- Generate Summary Report
- Project Summary

---

## Output Files

- cleaned_dataset.csv
- final_engineered_dataset.csv
- summary_report.txt
- plots/

---

## Run Project

```bash
pip install -r requirements.txt

python main.py
```

---

## Author

Hamna Maqsood