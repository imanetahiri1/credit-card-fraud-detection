# Fraud Detection V3 — Model Explainability

This version focuses on explaining the tuned XGBoost fraud-detection model from V2.

## Contents

- Global XGBoost feature importance
- SHAP summary analysis
- SHAP feature-importance table
- Individual transaction explanation
- Fraudulent versus legitimate transaction comparison
- SHAP dependence plots for V14 and V4

## Main Findings

V14 and V4 are the most influential features. Their effects vary across transactions and may interact with other features.

SHAP values explain model behavior but should not be interpreted as causal explanations for fraud.

## Model Source

V3 reuses the tuned model created in:

```text
fraud-detection-v2/models/xgboost_tuned.joblib
```