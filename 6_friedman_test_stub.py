import numpy as np
from scipy.stats import friedmanchisquare

# Generate three related samples
sample1 = np.random.normal(loc=5, scale=2, size=100)
sample2 = np.random.normal(loc=7, scale=2, size=100)
sample3 = np.random.normal(loc=9, scale=2, size=100)

# Perform Friedman test
statistic, p_value = friedmanchisquare(sample1, sample2, sample3)
print("Friedman Test:")
print(f"Statistic: {statistic}")
print(f"P-value: {p_value}")


'''In both examples, we generate three related samples representing different conditions or treatments. The samples are drawn from normal distributions with different means. Then, we perform the Friedman test, which is a nonparametric test to compare the distributions of three or more related samples. The test evaluates whether there are significant differences among the groups.

The Python example uses the SciPy library's friedmanchisquare function to calculate the test statistic and p-value. The R example uses the friedman.test function and retrieves the test statistic and p-value from the test result.'''