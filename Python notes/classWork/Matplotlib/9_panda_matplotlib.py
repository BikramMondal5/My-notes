import pandas as pd
import matplotlib.pyplot as plt
# Create a DataFrame
df = pd.DataFrame({
'Year': [2018, 2019, 2020, 2021, 2022],
'Sales': [120, 140, 90, 180, 210],
'Expenses': [90, 110, 80, 120, 150]
})
# Plot directly from DataFrame
df.plot(x='Year', y=['Sales', 'Expenses'], 
kind='bar')
plt.title('Annual Performance')
plt.ylabel('Amount ($K)')
plt.show()
