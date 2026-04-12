import pandas as pd

df = pd.read_csv("superstore_cleaned.csv")

# ── Question 1: Profit by Category ──────────────────────
cat = df.groupby("Category")[["Sales", "Profit"]].sum().round(2)
cat["Profit Margin %"] = round((cat["Profit"] / cat["Sales"]) * 100, 2)
print("=== PROFIT BY CATEGORY ===")
print(cat.sort_values("Profit", ascending=False))

# ── Question 2: Performance by Region ───────────────────
region = df.groupby("Region")[["Sales", "Profit"]].sum().round(2)
region["Profit Margin %"] = round((region["Profit"] / region["Sales"]) * 100, 2)
print("\n=== PERFORMANCE BY REGION ===")
print(region.sort_values("Profit", ascending=False))

# ── Question 3: Monthly Sales Trend ─────────────────────
monthly = df.groupby(["Order Year", "Order Month"])["Sales"].sum().round(2)
print("\n=== MONTHLY SALES TREND ===")
print(monthly)