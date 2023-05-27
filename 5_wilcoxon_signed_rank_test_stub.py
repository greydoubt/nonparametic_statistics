import numpy as np
from scipy.stats import wilcoxon

# Generate two related samples
before = np.random.normal(loc=5, scale=2, size=100)
after = np.random.normal(loc=7, scale=2, size=100)

# Perform Wilcoxon signed-rank test
statistic, p_value = wilcoxon(before, after)
print("Wilcoxon Signed-Rank Test:")
print(f"Statistic: {statistic}")
print(f"P-value: {p_value}")



'''In both examples, we generate two related samples representing before and after measurements. The samples are drawn from normal distributions with different means. Then, we perform the Wilcoxon signed-rank test, which is a nonparametric test to compare the distributions of two related samples. The test evaluates whether there is a significant difference between the paired observations.

The Python example uses the SciPy library's wilcoxon function to calculate the test statistic and p-value. The R example uses the wilcox.test function, specifying paired = TRUE, and retrieves the test statistic and p-value from the test result.'''