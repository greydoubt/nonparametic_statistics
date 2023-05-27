import numpy as np
from scipy.stats import chi2_contingency

# Create a contingency table
observed = np.array([[50, 30, 20], [40, 35, 25]])

# Perform chi-squared test
chi2, p_value, dof, expected = chi2_contingency(observed)
print("Chi-squared Test:")
print(f"Chi-squared statistic: {chi2}")
print(f"P-value: {p_value}")
print(f"Degrees of freedom: {dof}")

'''In both examples, we create a contingency table with observed frequencies for different categories. Then, we perform the chi-squared test, which is a statistical test used to determine if there is a significant association between two categorical variables. The test evaluates whether the observed frequencies differ significantly from the expected frequencies under the assumption of independence between the variables.

The Python example uses the SciPy library's chi2_contingency function to calculate the chi-squared statistic, p-value, degrees of freedom, and expected frequencies. The R example uses the chisq.test function and retrieves the chi-squared statistic, p-value, and degrees of freedom from the test result.'''