#USO Option P/L Visualization
#Section 2.6 - Thesis



import matplotlib.pyplot as plt
import pandas as pd


uso_prices = [
    80.00, 79.66, 79.33, 79.00, 78.66, 78.33, 78.00, 77.66, 77.33, 77.00, 76.66, 76.33,
    76.00, 75.66, 75.33, 75.00, 74.66, 74.33, 74.00, 73.66, 73.33, 73.00, 72.66, 72.33,
    72.00, 71.66, 71.33, 71.00, 70.66, 70.33, 70.00
]

profit_loss_adjusted = [
    412, 378, 345, 312, 278, 245, 212, 178, 145, 112, 78, 45, 12, -22, -55, -88, -88, -88,
    -88, -88, -88, -88, -88, -88, -88, -88, -88, -88, -88, -88, -88
]

df = pd.DataFrame({"USO Price": uso_prices, "P/L": profit_loss_adjusted})

plt.figure(figsize=(9, 5))

plt.plot(df["USO Price"], df["P/L"], 'o-', color="darkblue", label="Profit/Loss", markersize=5)

plt.axhline(0, color='gray', linestyle="--", linewidth=1, label="Breakeven Point")

plt.xlabel("USO Stock Price ($)")
plt.ylabel("Profit / Loss ($)")
plt.title("USO Profit/Loss vs. Stock Price")

plt.legend()
plt.grid(True, linestyle=":", linewidth=0.6)


plt.show()
