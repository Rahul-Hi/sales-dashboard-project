import pandas as pd

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")

# Fix 1: Convert dates from text to actual dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Fix 2: Convert Postal Code to text
df["Postal Code"] = df["Postal Code"].astype(str)

# Fix 3: Add useful columns for analysis later
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%b")
df["Profit Margin %"] = round((df["Profit"] / df["Sales"]) * 100, 2)

# Verify everything looks right
print("Date type now:", df["Order Date"].dtype)
print("Postal Code type now:", df["Postal Code"].dtype)
print("\nNew columns added:")
print(df[["Order Date", "Order Year", "Order Month", "Profit Margin %"]].head())

# Save cleaned data
df.to_csv("superstore_cleaned.csv", index=False)
print("\nCleaned file saved as superstore_cleaned.csv")