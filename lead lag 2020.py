#2020 lead lag analysis of SP500 and VIX
#Section 4.2 - Thesis



import matplotlib.pyplot as plt

lag_days = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
correlation = [-0.7095, -0.7477, -0.8335, -0.8735, -0.8682,
               -0.9546, -0.8909, -0.9327, -0.8965, -0.8648, -0.8519]


plt.figure(figsize=(10, 6))
plt.plot(lag_days, correlation, marker='o', linestyle='-', linewidth=2)

plt.ylim(-1.0, -0.7)
plt.xticks(lag_days) 
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Lag Days vs. Correlation')
plt.xlabel('Lag Days')
plt.ylabel('Correlation')

plt.tight_layout()
plt.show()
