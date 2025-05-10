import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
import os

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Encode labels
le = LabelEncoder()
df['label_encoded'] = le.fit_transform(df['label'])

X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label_encoded']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split and train model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and transformers
os.makedirs("models", exist_ok=True)
pickle.dump(model, open("models/crop_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(le, open("models/label_encoder.pkl", "wb"))

print("✅ Model training complete and saved.")
