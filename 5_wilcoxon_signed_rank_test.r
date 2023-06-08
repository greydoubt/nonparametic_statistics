# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Perform the Wilcoxon signed-rank test
result <- wilcox.test(data$Population, data$AverageIncome, paired = TRUE)

# Print the test statistic and p-value
cat("Wilcoxon signed-rank test:\n")
cat("Test Statistic:", result$statistic, "\n")
cat("p-value:", result$p.value, "\n")
