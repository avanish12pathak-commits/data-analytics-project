# Finance Data Analyzer - Data Cleaning

# 1. Import Libraries
import pandas as pd
import numpy as np

# 2. Load Dataset
df = pd.read_csv('Finance_Data.csv')

print("ORIGINAL DATASET")
print(df.head())

# 3. Explore Dataset
print("\nDataset Information:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nStatistical Summary:")
print(df.describe(include='all'))

# 4. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Check Duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 6. Remove Duplicate Records
df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df.shape)

# 7. Handle Missing Numerical Values
df['Income'] = df['Income'].fillna(
    df['Income'].median()
)

df['Expense'] = df['Expense'].fillna(
    df['Expense'].median()
)

# 8. Handle Missing Categorical Values
for col in ['Category', 'Payment_Mode', 'Account']:
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna('Not Available')

df['Description'] = df['Description'].fillna('Not Available')

# 9. Convert Date into DateTime Format
df['Date'] = pd.to_datetime(
    df['Date'],
    errors='coerce'
)

# 10. Check Invalid Financial Values
print("\nInvalid Income Records:")
print(df[df['Income'] < 0])

print("\nInvalid Expense Records:")
print(df[df['Expense'] < 0])

# Remove records with negative income or expense
df = df[
    (df['Income'] >= 0) &
    (df['Expense'] >= 0)
]

# 11. Check Payment Modes
print("\nAvailable Payment Modes:")
print(df['Payment_Mode'].unique())

# 12. Check Missing Values Again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 13. Display Cleaned Dataset
print("\nCLEANED DATASET:")
print(df)

# 14. Save Cleaned Dataset
df.to_csv('Cleaned_Finance_Data.csv', index=False)
print("\nCleaned dataset saved successfully!")