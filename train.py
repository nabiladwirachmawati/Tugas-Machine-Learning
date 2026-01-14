import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("heart.csv")

# Fitur dan target
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Kolom numerik & kategorikal
numeric_features = [
    "Age", "RestingBP", "Cholesterol",
    "MaxHR", "Oldpeak", "FastingBS"
]

categorical_features = [
    "Sex", "ChestPainType", "RestingECG",
    "ExerciseAngina", "ST_Slope"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

# Model
model = LogisticRegression(max_iter=1000)

# Pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, "heart_disease_model.pkl")

print("Model berhasil disimpan: heart_disease_model.pkl")
