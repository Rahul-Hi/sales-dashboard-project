import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("superstore_cleaned.csv")
sns.set_theme(style="whitegrid")

# ── Chart 1: Profit Margin by Category ──────────────────
cat = df.groupby("Category")[["Sales","Profit"]].sum()
cat["Profit Margin %"] = (cat["Profit"] / cat["Sales"] * 100).round(2)

plt.figure(figsize=(8, 5))
bars = plt.bar(cat.index, cat["Profit Margin %"],
               color=["#e74c3c" if x < 5 else "#2ecc71" for x in cat["Profit Margin %"]])
plt.title("Profit Margin % by Category", fontsize=14, fontweight="bold")
plt.ylabel("Profit Margin %")
plt.xlabel("Category")
for bar, val in zip(bars, cat["Profit Margin %"]):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             f"{val}%", ha="center", fontsize=11)
plt.tight_layout()
plt.savefig("chart1_category_profit.png", dpi=150)
plt.show()
print("Chart 1 saved")

# ── Chart 2: Region Performance ─────────────────────────
region = df.groupby("Region")[["Sales","Profit"]].sum().round(2)
region["Profit Margin %"] = (region["Profit"] / region["Sales"] * 100).round(2)
region = region.sort_values("Profit Margin %", ascending=False)

plt.figure(figsize=(8, 5))
bars = plt.bar(region.index, region["Profit Margin %"],
               color=["#e74c3c" if x < 10 else "#3498db" for x in region["Profit Margin %"]])
plt.title("Profit Margin % by Region", fontsize=14, fontweight="bold")
plt.ylabel("Profit Margin %")
plt.xlabel("Region")
for bar, val in zip(bars, region["Profit Margin %"]):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f"{val}%", ha="center", fontsize=11)
plt.tight_layout()
plt.savefig("chart2_region_profit.png", dpi=150)
plt.show()
print("Chart 2 saved")

# ── Chart 3: Monthly Sales Trend ────────────────────────
df["Year-Month"] = df["Order Date"].astype(str).str[:7]
monthly = df.groupby("Year-Month")["Sales"].sum().round(2)

plt.figure(figsize=(14, 5))
plt.plot(monthly.index, monthly.values, color="#8e44ad", linewidth=2, marker="o", markersize=3)
plt.title("Monthly Sales Trend (2014–2017)", fontsize=14, fontweight="bold")
plt.ylabel("Total Sales ($)")
plt.xlabel("Month")
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.tight_layout()
plt.savefig("chart3_monthly_trend.png", dpi=150)
plt.show()
print("Chart 3 saved")