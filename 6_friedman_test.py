import pandas as pd
from scipy.stats import friedmanchisquare

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Perform the Friedman test
result = friedmanchisquare(data['Population'], data['AverageIncome'], data['Age'])

# Print the test statistic and p-value
print("Friedman test:")
print("Test Statistic:", result.statistic)
print("p-value:", result.pvalue)
