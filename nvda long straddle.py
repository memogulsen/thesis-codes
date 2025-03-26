#NVDA Long Straddle Example
#Section 4.3 - Thesis



import matplotlib.pyplot as plt
import pandas as pd

price_values = [
    150.00, 148.50, 147.00, 145.50, 144.00, 142.50, 141.00, 139.50, 138.00, 136.50, 
    135.00, 133.50, 132.00, 130.50, 129.00, 127.50, 126.00, 124.50, 123.00, 121.50, 
    120.00, 118.50, 117.00, 115.50, 114.00, 112.50, 111.00, 109.50, 108.00, 106.50, 
    105.00, 103.50, 102.00, 100.50
]

profit_values = [
    1464, 1314, 1164, 1014, 864, 714, 564, 414, 264, 114, -36, -186, -336, -486, -636, -786, 
    -936, -1086, -1236, -1086, -936, -786, -636, -486, -336, -186, -36, 114, 264, 414, 564, 
    714, 864, 1014
]

df = pd.DataFrame({"Price": price_values, "Profit": profit_values})

plt.style.use("default")  
plt.figure(figsize=(9, 5), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

plt.plot(df["Price"], df["Profit"], marker="o", linestyle="-", color="blue", label="Profit/Loss")

plt.axhline(y=0, color='red', linestyle="--", label="Breakeven")

plt.xlabel("Price of NVDA")
plt.ylabel("Profit ($)")
plt.title("Profit/Loss vs. Price of NVDA")
plt.legend()

plt.grid(True, color='black', linestyle='--', linewidth=0.5)

plt.show()
