from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model
model = joblib.load("heart_disease_model.pkl")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class HeartData(BaseModel):
    Age: int
    Sex: str                  # M / F
    ChestPainType: str        # ATA, NAP, ASY, TA
    RestingBP: int
    Cholesterol: int
    FastingBS: int            # 0 / 1
    RestingECG: str           # Normal, ST, LVH
    MaxHR: int
    ExerciseAngina: str       # Y / N
    Oldpeak: float
    ST_Slope: str             # Up, Flat, Down

@app.post("/predict")
def predict_heart_disease(data: HeartData):
    # Convert input ke DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Prediksi
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "heart_disease_prediction": int(prediction),
        "risk_probability": round(float(probability), 3)
    }

# Run:
# uvicorn main:app --reload
