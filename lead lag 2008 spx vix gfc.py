#2008-2009 lead lag analysis of SP500 and VIX
#Section 4.2 - Thesis



import matplotlib.pyplot as plt


lag_days = list(range(-10, 11))
correlation = [-0.8059, -0.8126, -0.8202, -0.8255, -0.8332, -0.8402, -0.8446, -0.8520, -0.8569, -0.8644,
               -0.8753, -0.8660, -0.8604, -0.8593, -0.8557, -0.8535, -0.8513, -0.8500, -0.8503, -0.8479, -0.8453]

plt.figure(figsize=(10, 6))
plt.plot(lag_days, correlation, marker='o', linestyle='-', linewidth=2)
plt.title("Correlation vs Lag Days")
plt.xlabel("Lag Days")
plt.ylabel("Correlation")
plt.ylim(-0.9, -0.8)
plt.grid(True)
plt.axvline(0, color='gray', linestyle='--', linewidth=1)
plt.axhline(-0.8753, color='red', linestyle='--', linewidth=1, label='Min Correlation')
plt.legend()
plt.xticks(ticks=range(-10, 11, 2))
plt.tight_layout()
plt.show()
