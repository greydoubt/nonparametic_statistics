# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Perform the Friedman test
result <- friedman.test(data[, c("Population", "AverageIncome", "Age")])

# Print the test statistic and p-value
cat("Friedman test:\n")
cat("Test Statistic:", result$statistic, "\n")
cat("p-value:", result$p.value, "\n")
