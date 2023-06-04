# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Calculate Spearman's rank correlation
correlation <- cor(data$Population, data$AverageIncome, method = "spearman")

# Print the correlation coefficient
cat("Spearman's rank correlation:\n")
cat("Correlation coefficient:", correlation, "\n")
