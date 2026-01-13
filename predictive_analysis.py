# Predictive Analysis using Machine Learning
# CODTECH Internship Task-2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Create sample dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [35, 40, 45, 50, 55, 65, 70, 80]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Split data
X = df[['Hours_Studied']]
y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Visualization
plt.scatter(X, y)
plt.plot(X, model.predict(X),)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Predictive Analysis using Linear Regression")
plt.show()
