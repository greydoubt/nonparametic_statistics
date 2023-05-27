import numpy as np

# Generate a sample dataset
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Perform bootstrapping
n_bootstrap = 1000
bootstrap_means = []
for _ in range(n_bootstrap):
    bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
    bootstrap_mean = np.mean(bootstrap_sample)
    bootstrap_means.append(bootstrap_mean)

# Calculate bootstrap statistics
bootstrap_mean = np.mean(bootstrap_means)
bootstrap_std = np.std(bootstrap_means)

print("Bootstrapping:")
print(f"Bootstrap Mean: {bootstrap_mean}")
print(f"Bootstrap Standard Deviation: {bootstrap_std}")

'''In both examples, we start with a sample dataset (in this case, a simple array of numbers). We then perform bootstrapping by repeatedly sampling from the original data with replacement. In each iteration, we calculate a statistic of interest (in this case, the mean) from the bootstrap sample. We store the bootstrap statistics (means) for further analysis.

After performing the desired number of bootstrap iterations, we calculate the statistics of interest from the collection of bootstrap statistics. In the provided examples, we calculate the mean and standard deviation of the bootstrap means.'''