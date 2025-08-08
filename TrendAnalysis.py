import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range("2023-01-01", periods=200)
values = np.cumsum(np.random.randn(200) * 10)
categories = np.random.choice(["A", "B", "C"], size=200)
df = pd.DataFrame({"Date": dates, "Value": values, "Category": categories})

pivot = df.pivot_table(index="Date", columns="Category", values="Value", aggfunc="mean")
pivot = pivot.interpolate().rolling(7).mean()

plt.figure(figsize=(10,6))
for col in pivot.columns:
    plt.plot(pivot.index, pivot[col], label=col, linewidth=2)
plt.title("Trend Analysis", fontsize=18)
plt.legend()
plt.tight_layout()
plt.show()
