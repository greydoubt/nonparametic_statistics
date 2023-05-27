# Generate a sample dataset
data <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Perform bootstrapping
n_bootstrap <- 1000
bootstrap_means <- replicate(n_bootstrap, mean(sample(data, replace = TRUE)))

# Calculate bootstrap statistics
bootstrap_mean <- mean(bootstrap_means)
bootstrap_std <- sd(bootstrap_means)

cat("Bootstrapping:\n")
cat("Bootstrap Mean:", bootstrap_mean, "\n")
cat("Bootstrap Standard Deviation:", bootstrap_std, "\n")
