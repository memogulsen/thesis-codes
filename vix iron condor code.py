#VIX Iron Condor Example
#Section 4.3 - Thesis





import matplotlib.pyplot as plt
import pandas as pd


vix_levels = [
    26.00, 25.67, 25.34, 25.00, 24.67, 24.34, 24.00, 23.67, 23.34, 23.00, 
    22.67, 22.34, 22.00, 21.67, 21.34, 21.00, 20.67, 20.34, 20.00, 19.67, 
    19.34, 19.00, 18.67, 18.34, 18.00
]

expected_values = [
    -80, -47, -14, 20, 53, 86, 120, 120, 120, 120, 
    120, 120, 120, 120, 120, 120, 120, 120, 120, 87, 
    54, 20, -13, -46, -80
]

df = pd.DataFrame({"VIX Level": vix_levels, "Expected Value": expected_values})

plt.figure(figsize=(9, 5))  
plt.plot(df["VIX Level"], df["Expected Value"], 'o-', color="darkgreen", markersize=6, label="Expected Value")

plt.axhline(0, color='gray', linestyle="--", linewidth=1, label="Breakeven Level")

plt.xlabel("VIX Index Level")
plt.ylabel("Net Profit / Loss ($)")
plt.title("VIX Index vs Profit/Loss Performance")


plt.legend()
plt.grid(True, linestyle=":", linewidth=0.6)

plt.show()
