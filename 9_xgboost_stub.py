# XGBoost builds an ensemble of weak prediction models, typically decision trees, and combines their predictions to create a stronger overall model.

import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an XGBoost classifier
model = xgb.XGBClassifier()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


'''In both examples, we start by loading a dataset (load_breast_cancer in Python and iris in R). Then, we split the data into training and testing sets. After that, we create an XGBoost classifier (XGBClassifier in Python and xgboost in R) and fit the model to the training data. Finally, we make predictions on the testing data and evaluate the model's performance using a suitable evaluation metric (accuracy_score in Python and caret::accuracy in R).

You can use these code examples as a starting point to apply XGBoost to your own datasets by modifying the data loading, splitting, and evaluation steps accordingly. XGBoost offers a wide range of parameters that you can tune to optimize the model's performance for your specific task.'''