# Generate three independent samples
group1 <- rnorm(100, mean = 5, sd = 2)
group2 <- rnorm(120, mean = 7, sd = 2)
group3 <- rnorm(80, mean = 9, sd = 2)

# Perform Kruskal-Wallis test
result <- kruskal.test(list(group1, group2, group3))
cat("Kruskal-Wallis test:\n")
cat("Statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")
