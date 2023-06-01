import pandas as pd
from scipy.stats import mannwhitneyu

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Perform the Mann-Whitney U test
result = mannwhitneyu(data['Population'], data['AverageIncome'])

# Print the test statistic and p-value
print("Mann-Whitney U test:")
print("Test Statistic:", result.statistic)
print("p-value:", result.pvalue)
