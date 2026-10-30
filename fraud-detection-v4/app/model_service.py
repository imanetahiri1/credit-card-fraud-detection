from pathlib import Path

import joblib
import pandas as pd


MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "xgboost_tuned.joblib"
)


class FraudModelService:
    def __init__(self) -> None:
        package = joblib.load(MODEL_PATH)

        self.model = package["model"]
        self.threshold = package["threshold"]
        self.feature_names = package["feature_names"]

    def predict(self, transaction: dict) -> dict:
        missing_features = [
            feature
            for feature in self.feature_names
            if feature not in transaction
        ]

        if missing_features:
            raise ValueError(
                f"Missing required features: {missing_features}"
            )

        features = pd.DataFrame(
            [[transaction[feature] for feature in self.feature_names]],
            columns=self.feature_names,
        )

        probability = float(self.model.predict_proba(features)[0, 1])

        return {
            "fraud_probability": probability,
            "is_fraud": probability >= self.threshold,
            "threshold": self.threshold,
        }