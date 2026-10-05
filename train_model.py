import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# 1. Load the dataset
data = pd.read_csv("data/student_data.csv")

print("Dataset loaded successfully!")
print("Number of students:", len(data))


# 2. Select input features
X = data[
    [
        "attendance",
        "study_hours",
        "previous_marks",
        "assignment_marks",
        "internal_marks",
        "participation"
    ]
]


# 3. Select target
y = data["final_marks"]


# 4. Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Create the Machine Learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# 6. Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")


# 7. Make predictions
predictions = model.predict(X_test)


# 8. Check model performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))


# 9. Save the trained model
with open("models/student_performance_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
print("Location: models/student_performance_model.pkl")