import pandas as pd
from scipy.stats import kruskal

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Perform the Kruskal-Wallis test
result = kruskal(data['Population'], data['AverageIncome'], data['Age'])

# Print the test statistic and p-value
print("Kruskal-Wallis test:")
print("Test Statistic:", result.statistic)
print("p-value:", result.pvalue)
