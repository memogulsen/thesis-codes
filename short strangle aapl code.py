#AAPL Short Strangle Example
#Section 4.3 - Thesis




import matplotlib.pyplot as plt
import pandas as pd


aapl_prices = [
    234.00, 232.50, 231.00, 229.50, 228.00, 226.50, 225.00, 223.50, 222.00, 220.50,
    219.00, 217.50, 216.00, 214.50, 213.00, 211.50, 210.00, 208.50, 207.00, 205.50,
    204.00, 202.50, 201.00, 199.50, 198.00, 196.50, 195.00, 193.50, 192.00, 190.50
]

profit_loss = [
    -723, -573, -423, -273, -123, 27, 177, 327, 477, 627, 
    677, 677, 677, 677, 677, 677, 677, 677, 677, 677, 
    577, 427, 277, 127, -23, -173, -323, -473, -623, -773
]

df = pd.DataFrame({"Stock Price": aapl_prices, "P/L": profit_loss})

plt.figure(figsize=(9, 5))  

plt.plot(df["Stock Price"], df["P/L"], 'o-', color="darkblue", label="Profit/Loss", markersize=5)

plt.axhline(0, color='gray', linestyle="--", linewidth=1, label="Breakeven Point")

plt.xlabel("AAPL Stock Price ($)")
plt.ylabel("Profit / Loss ($)")
plt.title("Apple (AAPL) Profit/Loss vs. Stock Price")

plt.legend()
plt.grid(True, linestyle=":", linewidth=0.6)

plt.show()
