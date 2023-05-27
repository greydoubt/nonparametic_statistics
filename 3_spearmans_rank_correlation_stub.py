import numpy as np
from scipy.stats import spearmanr

# Generate two variables with a monotonic relationship
x = np.random.randint(1, 10, size=100)
y = x + np.random.normal(0, 1, size=100)

# Calculate Spearman's rank correlation
correlation, p_value = spearmanr(x, y)
print("Spearman's Rank Correlation:")
print(f"Correlation Coefficient: {correlation}")
print(f"P-value: {p_value}")


'''In both examples, we generate two variables x and y with a monotonic relationship. The variable x is a random integer sequence, and y is derived from x with some noise. Then, we calculate Spearman's rank correlation, which measures the strength and direction of the monotonic relationship between the variables.

The Python example uses the SciPy library's spearmanr function to compute the correlation coefficient and p-value. The R example uses the cor.test function, specifying the method as "spearman", and retrieves the correlation coefficient and p-value from the test result.'''