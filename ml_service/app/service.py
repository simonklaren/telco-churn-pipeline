# ml_service/app/service.py
from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "churn_pipeline.pkl"


class ChurnModelService:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.version = "1.0.0"  # pas aan bij nieuwe versie
      
        # Kolommen in dezelfde volgorde als tijdens training
        self.feature_order = [
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges",
        ]

    def predict(self, payload: dict):
        # zorg dat de volgorde klopt
        data = {k: payload[k] for k in self.feature_order}
        df = pd.DataFrame([data])

        proba = self.model.predict_proba(df)[0][1]
        pred = self.model.predict(df)[0]

        return bool(pred), float(proba)
