import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
import shutil


# loading the preprocessed data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Safe path to data file
DATA_PATH = os.path.join(BASE_DIR, "../data/processed/train.csv")

# Load CSV like a boss
data = pd.read_csv(DATA_PATH)

# extracting target and dependent variables
x = data.drop(columns=['species'])
y = data['species']

#splitting into Train and Test data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#initializing the model
model = DecisionTreeClassifier(random_state=42 , max_depth=2 , n_estimators=2)

#training the model
model.fit(X_train,y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

# training and testing accuracies for model fitting check
print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")




# Clean previous models
model_dir = "models"
if os.path.exists(model_dir):
    shutil.rmtree(model_dir)
os.makedirs(model_dir, exist_ok=True)

# Save new model
joblib.dump(model, os.path.join(model_dir, "model.pkl"))
print("Old models wiped ,New model saved.")


import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

# Try feeding it a test row
sample = pd.DataFrame([[1.1, 5.5, 4.4, 1.2]], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
print(model.predict(sample))
