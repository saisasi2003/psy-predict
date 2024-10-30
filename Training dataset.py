# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load and preprocess your dataset
data = pd.read_csv('your_dataset.csv')
# Updated to include the new factors
X = data[['screen_time', 'num_calls', 'message_frequency', 'social_media_usage', 'gaming_frequency', 'sleeping_hours']]
y = data['mental_health_status']  # Assuming 'mental_health_status' is the target

# Split and train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate and save the model
y_pred = model.predict(X_test)
print("Model accuracy:", accuracy_score(y_test, y_pred))
joblib.dump(model, 'mental_health_predictor_model.pkl')
