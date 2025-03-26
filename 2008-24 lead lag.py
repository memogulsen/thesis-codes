#2008-2024 lead lag analysis of SP500 and VIX
#Section 4.1 - Thesis



import matplotlib.pyplot as plt

lag_days = list(range(-10, 11))
correlations = [-0.2026, -0.2045, -0.2063, -0.2083, -0.2102, -0.2123, -0.2145, -0.2167, -0.2191, -0.2215, -0.2246,
                -0.2240, -0.2238, -0.2233, -0.2227, -0.2221, -0.2216, -0.2215, -0.2213, -0.2218, -0.2212]

plt.figure(figsize=(10, 6))
plt.plot(lag_days, correlations, marker='o', linestyle='-')

plt.ylim(-0.225, -0.2)
plt.xticks(range(-10, 11, 2))

plt.xlabel('Lag days')
plt.ylabel('Correlation')
plt.title('Correlation vs Lag Days')

plt.grid(True)
plt.tight_layout()
plt.show()
