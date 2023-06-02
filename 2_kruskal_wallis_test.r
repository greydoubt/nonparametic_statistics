# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Perform the Kruskal-Wallis test
result <- kruskal.test(list(data$Population, data$AverageIncome, data$Age))

# Print the test statistic and p-value
cat("Kruskal-Wallis test:\n")
cat("Test Statistic:", result$statistic, "\n")
cat("p-value:", result$p.value, "\n")
