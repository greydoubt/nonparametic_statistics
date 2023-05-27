import numpy as np
from scipy.stats import kruskal

# Generate three independent samples
group1 = np.random.normal(loc=5, scale=2, size=100)
group2 = np.random.normal(loc=7, scale=2, size=120)
group3 = np.random.normal(loc=9, scale=2, size=80)

# Perform Kruskal-Wallis test
statistic, p_value = kruskal(group1, group2, group3)
print("Kruskal-Wallis test:")
print(f"Statistic: {statistic}")
print(f"P-value: {p_value}")


'''In both examples, we generate three independent samples from normal distributions with different means. Then, we perform the Kruskal-Wallis test, which is a nonparametric test to compare the distributions of three or more independent samples. The test evaluates whether the samples come from the same population or if at least one of the samples has a different distribution.

The Python example uses the SciPy library's kruskal function to calculate the test statistic and p-value. The R example uses the kruskal.test function, passing the samples as a list, and retrieves the test statistic and p-value from the test result.'''