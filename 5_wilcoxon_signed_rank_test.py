import pandas as pd
from scipy.stats import wilcoxon

# Read the CSV data into a DataFrame
data = pd.read_csv('your_data.csv')

# Perform the Wilcoxon signed-rank test
result = wilcoxon(data['Population'], data['AverageIncome'])

# Print the test statistic and p-value
print("Wilcoxon signed-rank test:")
print("Test Statistic:", result.statistic)
print("p-value:", result.pvalue)
