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
        data = {k: payload[k] for k in self.feature_order}
        df = pd.DataFrame([data])
    
        pred = self.model.predict(df)[0]  # "No" of "Yes"
    
        # Pak probability voor "Yes" op basis van model.classes_
        classes = list(self.model.classes_)  # verwacht ["No", "Yes"]
        yes_idx = classes.index("Yes")
        proba = float(self.model.predict_proba(df)[0][yes_idx])
    
        churn = (pred == "Yes")
        return churn, proba
