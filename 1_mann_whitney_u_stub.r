# Generate two independent samples
group1 <- rnorm(100, mean = 5, sd = 2)
group2 <- rnorm(120, mean = 7, sd = 2)

# Perform Mann-Whitney U test
result <- wilcox.test(group1, group2)
cat("Mann-Whitney U test:\n")
cat("Statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")


