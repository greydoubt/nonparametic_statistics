import pandas as pd
from scipy.stats import spearmanr

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Calculate Spearman's rank correlation
correlation, p_value = spearmanr(data['Population'], data['AverageIncome'])

# Print the correlation coefficient and p-value
print("Spearman's rank correlation:")
print("Correlation coefficient:", correlation)
print("p-value:", p_value)
