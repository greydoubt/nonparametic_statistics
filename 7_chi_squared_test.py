import pandas as pd
from scipy.stats import chi2_contingency

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Create a contingency table for the variables of interest
contingency_table = pd.crosstab(data['Education'], data['Employment'])

# Perform the chi-squared test
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Print the test statistic and p-value
print("Chi-squared test:")
print("Test Statistic:", chi2)
print("p-value:", p_value)
