import pandas as pd
from scipy.stats import kendalltau

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Calculate Kendall's rank correlation
correlation, p_value = kendalltau(data['Population'], data['AverageIncome'])

# Print the correlation coefficient and p-value
print("Kendall's rank correlation:")
print("Correlation coefficient:", correlation)
print("p-value:", p_value)
