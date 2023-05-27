# Generate two related samples
before <- rnorm(100, mean = 5, sd = 2)
after <- rnorm(100, mean = 7, sd = 2)

# Perform Wilcoxon signed-rank test
result <- wilcox.test(before, after, paired = TRUE)
cat("Wilcoxon Signed-Rank Test:\n")
cat("Statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")
