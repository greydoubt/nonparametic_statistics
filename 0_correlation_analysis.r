# Read the CSV data into a DataFrame
data <- read.csv("your_data.csv")

# Calculate the correlation matrix
correlation_matrix <- cor(data)

# Get the absolute correlation values for each variable pair
abs_correlation <- abs(correlation_matrix)

# Find the pairs with high correlation
high_correlation_pairs <- (abs_correlation > 0.7) & (abs_correlation < 1.0)
high_correlation_variables <- subset(as.data.frame(which(high_correlation_pairs, arr.ind = TRUE), stringsAsFactors = FALSE), select = -c(row))

# Rename the columns
colnames(high_correlation_variables) <- c("Variable 1", "Variable 2")

# Add the correlation values
high_correlation_variables$Correlation <- abs_correlation[high_correlation_pairs]

# Sort the pairs by correlation strength
sorted_pairs <- high_correlation_variables[order(high_correlation_variables$Correlation, decreasing = TRUE), ]

# Display the strongly correlated pairs
cat("Strongly Correlated Variable Pairs:\n")
print(sorted_pairs)
