# ==========================================
# FINANCE REPORT - DATA ANALYSIS PROJECT
# ==========================================

# 1. Importing Libraries

import pandas as pd
import numpy as np

print("===================================")
print("       FINANCE REPORT SYSTEM")
print("===================================")


# 2. Loading Dataset

df = pd.read_csv("Finance_Data.csv")

print("\n===== ORIGINAL FINANCE DATA =====")
print(df.head())


# 3. Dataset Information

print("\n===== DATASET INFORMATION =====")

print("Total Transactions:", len(df))
print("Dataset Shape:", df.shape)

print("\nColumn Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all"))


# 4. Checking Missing Values

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())


# 5. Checking Duplicate Records

print("\n===== DUPLICATE RECORDS =====")

print("Duplicate Transactions:", df.duplicated().sum())


# 6. Removing Duplicate Records

df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df.shape)


# 7. Handling Missing Values

# Fill missing numerical values with median

for col in ["Income", "Expense"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values

for col in ["Category", "Description", "Payment_Mode", "Account"]:
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna("Not Available")


# 8. Converting Date into Date Format

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df = df.dropna(subset=["Date", "Transaction_ID"])


# 9. Removing Invalid Financial Records

df = df[
    (df["Income"] >= 0) &
    (df["Expense"] >= 0)
]

print("\n===== CLEANED DATA =====")

print(df)


# 10. Creating New Financial Columns

df["Net_Amount"] = df["Income"] - df["Expense"]

df["Month"] = df["Date"].dt.month_name()

df["Year"] = df["Date"].dt.year


# 11. Total Income and Expenses

total_income = df["Income"].sum()

total_expense = df["Expense"].sum()

net_savings = total_income - total_expense

print("\n===== FINANCIAL SUMMARY =====")

print("Total Income: ₹", total_income)

print("Total Expenses: ₹", total_expense)

print("Net Savings: ₹", net_savings)


# 12. Average Income and Expenses

print("\n===== AVERAGE FINANCIAL DATA =====")

print("Average Income: ₹",
      round(df["Income"].mean(), 2))

print("Average Expense: ₹",
      round(df["Expense"].mean(), 2))


# 13. Highest and Lowest Expenses

highest_expense = df.loc[df["Expense"].idxmax()]

lowest_expense = df[df["Expense"] > 0].loc[
    df[df["Expense"] > 0]["Expense"].idxmin()
]

print("\n===== EXPENSE ANALYSIS =====")

print("Highest Expense:")

print(highest_expense[
    ["Category", "Description", "Expense"]
])

print("\nLowest Expense:")

print(lowest_expense[
    ["Category", "Description", "Expense"]
])


# 14. Category Wise Expense Analysis

category_expense = df.groupby(
    "Category"
)["Expense"].sum().sort_values(ascending=False)

print("\n===== CATEGORY WISE EXPENSES =====")

print(category_expense)


# 15. Payment Mode Analysis

payment_analysis = df.groupby(
    "Payment_Mode"
)["Expense"].sum()

print("\n===== PAYMENT MODE ANALYSIS =====")

print(payment_analysis)


# 16. Income Source Analysis

income_analysis = df.groupby(
    "Category"
)["Income"].sum().sort_values(ascending=False)

print("\n===== INCOME SOURCE ANALYSIS =====")

print(income_analysis)


# 17. Account Wise Analysis

account_analysis = df.groupby(
    "Account"
)[["Income", "Expense"]].sum()

print("\n===== ACCOUNT WISE ANALYSIS =====")

print(account_analysis)


# 18. NumPy Analysis

income_array = np.array(df["Income"])

expense_array = np.array(df["Expense"])

print("\n===== NUMPY ANALYSIS =====")

print("Maximum Income:", np.max(income_array))

print("Minimum Income:", np.min(income_array))

print("Average Income:", round(np.mean(income_array), 2))

print("Maximum Expense:", np.max(expense_array))

print("Minimum Expense:", np.min(expense_array))

print("Average Expense:", round(np.mean(expense_array), 2))


# 19. Monthly Financial Report

monthly_report = df.groupby("Month")[
    ["Income", "Expense"]
].sum()

monthly_report["Net_Savings"] = (
    monthly_report["Income"] -
    monthly_report["Expense"]
)

print("\n===== MONTHLY FINANCIAL REPORT =====")

print(monthly_report)


# 20. Final Financial Report

print("\n===================================")
print("          FINAL FINANCE REPORT")
print("===================================")

print("Total Transactions:", len(df))

print("Total Income: ₹", total_income)

print("Total Expenses: ₹", total_expense)

print("Net Savings: ₹", net_savings)

if total_income > 0:
    savings_percentage = (net_savings / total_income) * 100
else:
    savings_percentage = 0

print("Savings Percentage:",
      round(savings_percentage, 2), "%")


# 21. Saving Cleaned Dataset and Reports

df.to_csv("Cleaned_Finance_Data.csv", index=False)

category_expense.to_csv("Category_Expense_Report.csv")

monthly_report.to_csv("Monthly_Finance_Report.csv")

print("\nAll Reports Saved Successfully!")

print("\n===== PROJECT COMPLETED =====")
 
