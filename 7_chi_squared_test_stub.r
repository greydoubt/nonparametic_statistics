# Create a contingency table
observed <- matrix(c(50, 30, 20, 40, 35, 25), nrow = 2, byrow = TRUE)

# Perform chi-squared test
result <- chisq.test(observed)
cat("Chi-squared Test:\n")
cat("Chi-squared statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")
cat("Degrees of freedom:", result$parameter, "\n")
