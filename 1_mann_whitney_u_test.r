# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Perform the Mann-Whitney U test
result <- wilcox.test(data$Population, data$AverageIncome)

# Print the test statistic and p-value
cat("Mann-Whitney U test:\n")
cat("Test Statistic:", result$statistic, "\n")
cat("p-value:", result$p.value, "\n")
