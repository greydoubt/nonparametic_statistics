# Generate three related samples
sample1 <- rnorm(100, mean = 5, sd = 2)
sample2 <- rnorm(100, mean = 7, sd = 2)
sample3 <- rnorm(100, mean = 9, sd = 2)

# Perform Friedman test
result <- friedman.test(sample1, sample2, sample3)
cat("Friedman Test:\n")
cat("Statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")
