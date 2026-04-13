import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("superstore_cleaned.csv")

# ── Prepare monthly sales data ───────────────────────────
df["Order Date"] = pd.to_datetime(df["Order Date"])
monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
monthly.index = monthly.index.to_timestamp()

# ── Build forecasting model ──────────────────────────────
model = ExponentialSmoothing(
    monthly,
    trend="add",
    seasonal="add",
    seasonal_periods=12
).fit()

# ── Forecast next 3 months ───────────────────────────────
forecast = model.forecast(3)

print("=== FORECAST: Next 3 Months ===")
for date, value in forecast.items():
    print(f"{date.strftime('%B %Y')}: ${value:,.2f}")

# ── Plot last 12 months + forecast only ──────────────────
last_12 = monthly.tail(12)

fig, ax = plt.subplots(figsize=(12, 6))

# Historical line
ax.plot(last_12.index, last_12.values,
        color="#2980b9", linewidth=2.5,
        marker="o", markersize=5, label="Historical Sales")

# Forecast line
ax.plot(forecast.index, forecast.values,
        color="#e74c3c", linewidth=2.5,
        linestyle="--", marker="o",
        markersize=10, label="Forecast")

# Divider line
ax.axvline(x=monthly.index[-1], color="gray",
           linestyle=":", linewidth=1.5)

ax.text(monthly.index[-1], ax.get_ylim()[1] * 0.95,
        "  Forecast starts", color="gray", fontsize=10)

# Forecast labels — clearly spaced
for date, value in forecast.items():
    ax.annotate(f"{date.strftime('%b %Y')}\n${value:,.0f}",
                xy=(date, value),
                xytext=(25, 10),
                textcoords="offset points",
                fontsize=11,
                fontweight="bold",
                color="#c0392b",
                arrowprops=dict(arrowstyle="->",
                                color="#c0392b",
                                lw=1.5))

ax.set_title("Sales Forecast — Next 3 Months\n(Based on 4 years of historical data)",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Sales ($)", fontsize=12)
ax.legend(fontsize=11)
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
plt.tight_layout()
plt.savefig("chart4_forecast.png", dpi=150)
plt.show()
print("Forecast chart saved.")