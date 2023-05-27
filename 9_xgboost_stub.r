library(xgboost)
library(datasets)
library(caret)

# Load the dataset
data(iris)
X <- iris[, 1:4]
y <- iris$Species

# Split the data into training and testing sets
set.seed(42)
train_indices <- createDataPartition(y, p = 0.8, list = FALSE)
X_train <- X[train_indices, ]
y_train <- y[train_indices]
X_test <- X[-train_indices, ]
y_test <- y[-train_indices]

# Create an XGBoost classifier
model <- xgboost(data = as.matrix(X_train), label = y_train, nrounds = 100)

# Make predictions on the testing data
y_pred <- predict(model, as.matrix(X_test))

# Evaluate the model
accuracy <- caret::accuracy(y_pred, y_test)
print("Accuracy:", accuracy)
