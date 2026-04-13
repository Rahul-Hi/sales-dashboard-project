import pandas as pd

df = pd.read_csv("superstore_cleaned.csv")

print("=== FURNITURE DISCOUNT ANALYSIS ===")
furniture = df[df["Category"] == "Furniture"]
print(f"Average discount on Furniture: {furniture['Discount'].mean()*100:.1f}%")
print(f"Orders with 0% discount: {len(furniture[furniture['Discount']==0])}")
print(f"Orders with discount > 20%: {len(furniture[furniture['Discount']>0.2])}")

print("\n=== PROFIT LOST TO DISCOUNTS ===")
high_discount = df[df["Discount"] > 0.2]
print(f"Total orders with >20% discount: {len(high_discount)}")
print(f"Total profit from these orders: ${high_discount['Profit'].sum():,.2f}")
print(f"Total sales from these orders: ${high_discount['Sales'].sum():,.2f}")
print(f"Profit margin on heavily discounted orders: {(high_discount['Profit'].sum()/high_discount['Sales'].sum()*100):.2f}%")

print("\n=== SIMULATION: Cap all discounts at 20% ===")
normal = df[df["Discount"] <= 0.2]
print(f"Profit with current discounting: ${df['Profit'].sum():,.2f}")
print(f"Profit if high discounts removed: ${normal['Profit'].sum():,.2f}")
print(f"Potential profit gain: ${normal['Profit'].sum() - df['Profit'].sum():,.2f}")

print("\n=== SUB-CATEGORIES LOSING MONEY ===")
sub = df.groupby("Sub-Category")[["Sales","Profit"]].sum()
sub["Margin %"] = (sub["Profit"]/sub["Sales"]*100).round(2)
losing = sub[sub["Profit"] < 0].sort_values("Profit")
print(losing)