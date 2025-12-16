# ml_service/app/main.py
from fastapi import FastAPI
from .schemas import ChurnRequest, ChurnResponse
from .service import ChurnModelService

app = FastAPI(title="Telco Churn API")

service = ChurnModelService()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": service.version,
    }


@app.post("/predict", response_model=ChurnResponse)
def predict(request: ChurnRequest):
    label, proba = service.predict(request.dict())
    return ChurnResponse(
        churn=label,
        probability=proba,
        model_version=service.version,
    )
