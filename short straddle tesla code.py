#TSLA Short Straddle Example
#Section 4.3 - Thesis




import matplotlib.pyplot as plt
import pandas as pd


tsla_stock_prices = [
    350, 343, 336, 329, 322, 315, 308, 301, 294, 287, 280, 273, 
    266, 259, 252, 245, 238, 231, 224, 217, 210, 203, 196, 189, 
    182, 175, 168, 161, 154
]

profit_or_loss = [
    -6609, -5909, -5209, -4509, -3809, -3109, -2409, -1709, -1009, -309, 
    391, 1091, 1791, 2479, 2972, 2819, 2191, 1493, 793, 93, -607, -1307, 
    -2007, -2707, -3407, -4107, -4807, -5507, -6207
]

df = pd.DataFrame({"Stock Price ($)": tsla_stock_prices, "Profit/Loss ($)": profit_or_loss})

print(df.head())  

plt.figure(figsize=(8.5, 5))  

plt.plot(df["Stock Price ($)"], df["Profit/Loss ($)"], marker="s", linestyle="-", color="blue", label="Profit/Loss")

plt.axhline(y=0, color='black', linestyle="--", linewidth=1, label="Breakeven Point")

plt.xlabel("Tesla Stock Price ($)")
plt.ylabel("Net Profit / Loss ($)")
plt.title("Tesla Stock Price vs Profit/Loss Performance")

plt.legend()

plt.grid(True, linestyle="--", linewidth=0.7)

plt.show()
