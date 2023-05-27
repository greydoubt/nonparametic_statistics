import numpy as np
from scipy.stats import mannwhitneyu

# Generate two independent samples
group1 = np.random.normal(loc=5, scale=2, size=100)
group2 = np.random.normal(loc=7, scale=2, size=120)

# Perform Mann-Whitney U test
statistic, p_value = mannwhitneyu(group1, group2)
print("Mann-Whitney U test:")
print(f"Statistic: {statistic}")
print(f"P-value: {p_value}")



'''In both examples, we generate two independent samples from normal distributions with different means. Then, we perform the Mann-Whitney U test, which is a nonparametric test to compare the distributions of two independent samples. The test evaluates whether the two samples come from the same population or if their distributions differ significantly.

The Python example uses the SciPy library's mannwhitneyu function to calculate the test statistic and p-value. The R example uses the built-in wilcox.test function to perform the Mann-Whitney U test and retrieves the test statistic and p-value from the test result.'''