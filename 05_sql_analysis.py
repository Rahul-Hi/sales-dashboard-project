import pandas as pd
import sqlite3

# Load cleaned data into a SQLite database
df = pd.read_csv("superstore_cleaned.csv")
conn = sqlite3.connect("superstore.db")
df.to_sql("orders", conn, if_exists="replace", index=False)
print("Database created successfully")

# ── SQL Query 1: Profit by Category ─────────────────────
q1 = """
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin_Pct
FROM orders
GROUP BY Category
ORDER BY Total_Profit DESC
"""
print("\n=== SQL: Profit by Category ===")
print(pd.read_sql_query(q1, conn))

# ── SQL Query 2: Region Performance ─────────────────────
q2 = """
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin_Pct
FROM orders
GROUP BY Region
ORDER BY Profit_Margin_Pct DESC
"""
print("\n=== SQL: Region Performance ===")
print(pd.read_sql_query(q2, conn))

# ── SQL Query 3: Top 10 most profitable products ─────────
q3 = """
SELECT 
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY "Product Name"
ORDER BY Total_Profit DESC
LIMIT 10
"""
print("\n=== SQL: Top 10 Most Profitable Products ===")
print(pd.read_sql_query(q3, conn))

# ── SQL Query 4: Loss-making products ───────────────────
q4 = """
SELECT 
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY "Product Name"
ORDER BY Total_Profit ASC
LIMIT 10
"""
print("\n=== SQL: Top 10 Loss-Making Products ===")
print(pd.read_sql_query(q4, conn))

conn.close()