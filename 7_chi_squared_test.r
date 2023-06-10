# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Create a contingency table for the variables of interest
contingency_table <- table(data$Education, data$Employment)

# Perform the chi-squared test
result <- chisq.test(contingency_table)

# Print the test statistic and p-value
cat("Chi-squared test:\n")
cat("Test Statistic:", result$statistic, "\n")
cat("p-value:", result$p.value, "\n")
