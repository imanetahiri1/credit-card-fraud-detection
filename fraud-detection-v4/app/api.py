from fastapi import FastAPI

from app.model_service import FraudModelService
from app.schemas import PredictionResponse, Transaction


app = FastAPI(
    title="Real-Time Fraud Detection API",
    version="1.0.0",
)

model_service = FraudModelService()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/model-info")
def model_info() -> dict:
    return {
        "model": "tuned_xgboost",
        "feature_count": len(model_service.feature_names),
        "threshold": model_service.threshold,
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: Transaction) -> PredictionResponse:
    result = model_service.predict(transaction.model_dump())
    return PredictionResponse(**result)