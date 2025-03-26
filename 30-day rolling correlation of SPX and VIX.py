#30 day rolling correlation
#Section 4.1 - Thesis


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("spx&vix data combined&interpolated.xlsx", sheet_name='Final Interpolated Data')
df = df.iloc[1:, :3]
df.columns = ['Date', 'SPX', 'VIX']
df['Date'] = pd.to_datetime(df['Date'])
df['SPX'] = pd.to_numeric(df['SPX'], errors='coerce')
df['VIX'] = pd.to_numeric(df['VIX'], errors='coerce')
df.dropna(inplace=True)
df.set_index('Date', inplace=True)

df['30-Day Rolling Correlation'] = df['SPX'].rolling(window=30).corr(df['VIX'])

plt.figure(figsize=(14, 6))
plt.plot(df.index, df['30-Day Rolling Correlation'], label='30-Day Rolling Correlation', linewidth=2)
plt.title('30-Day Rolling Correlation between SP500 and VIX')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
