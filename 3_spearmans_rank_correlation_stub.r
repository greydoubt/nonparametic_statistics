# Generate two variables with a monotonic relationship
x <- sample(1:10, 100, replace = TRUE)
y <- x + rnorm(100)

# Calculate Spearman's rank correlation
result <- cor.test(x, y, method = "spearman")
cat("Spearman's Rank Correlation:\n")
cat("Correlation Coefficient:", result$estimate, "\n")
cat("P-value:", result$p.value, "\n")
