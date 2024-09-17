# Import necessary libraries
import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import shap

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

# Shapley Values for interpretability
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Visualize a summary plot of feature importance
shap.summary_plot(shap_values, X_test, feature_names=data.feature_names)


'''
    shap.Explainer(model): Initializes the SHAP explainer for the trained XGBoost model.
    explainer(X_test): Computes the SHAP values for the testing set, which measure the contribution of each feature to the model’s predictions.
    shap.summary_plot(): Creates a visualization of the SHAP values, showing the global importance of each feature in the model’s predictions.

Summary of Shapley Visualization:

    Summary Plot: A bar plot or bee-swarm plot showing the impact of each feature on the model's predictions. It reveals which features contribute the most to the predictions and how their values (low or high) influence outcomes.
'''
