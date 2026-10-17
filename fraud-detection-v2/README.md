# Credit Card Fraud Detection — V2

## Model Comparison and Evaluation

V2 extends the exploratory analysis and baseline modeling completed in V1.

The objective of V2 is to train, compare, and evaluate multiple machine-learning models for credit-card fraud detection while considering the severe class imbalance in the dataset.

The models are evaluated using fraud-focused metrics rather than accuracy alone.

---

## Project Objective

The dataset contains credit-card transactions labeled as either:

- `0`: Legitimate transaction
- `1`: Fraudulent transaction

Fraudulent transactions represent only a very small proportion of all transactions. Therefore, accuracy alone can be misleading.

V2 focuses on:

- Preparing the data for machine learning
- Creating a stratified train/test split
- Handling class imbalance
- Training multiple classification models
- Comparing model performance
- Analyzing false positives and false negatives
- Selecting a strong candidate for hyperparameter tuning
- Studying classification thresholds

---

## Models Compared

V2 compares four models.

### 1. Dummy Classifier

The Dummy Classifier provides a reference baseline.

It does not learn meaningful relationships from the data. Its purpose is to demonstrate why accuracy is not sufficient for this fraud-detection problem.

### 2. Logistic Regression

Logistic Regression is used as an interpretable linear baseline.

It provides a simple reference point and helps evaluate how well a linear model performs on the dataset.

### 3. Random Forest

Random Forest is an ensemble of decision trees.

It can model nonlinear relationships and interactions between features.

### 4. XGBoost

XGBoost is a gradient-boosting algorithm designed for strong performance on structured tabular data.

It is expected to be one of the strongest candidate models for this problem.

---

## Dataset

V2 uses the same shared dataset as V1.

The dataset source is:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains:

- 284,807 transactions
- 30 input columns
- 28 PCA-transformed numerical features
- `Time`
- `Amount`
- `Class` as the target column
- 492 fraudulent transactions
- 284,315 legitimate transactions

Target values:

- `0`: Legitimate transaction
- `1`: Fraudulent transaction

The dataset is highly imbalanced:

- Legitimate transactions: approximately 99.83%
- Fraudulent transactions: approximately 0.17%

All project versions use one shared raw dataset:

```text
data/raw/creditcard.csv
```

The raw dataset is intentionally excluded from Git because it is a large local file.

---

## Tech Stack

### Programming Language

- Python

### Data Processing

- pandas
- NumPy

### Machine Learning

- scikit-learn
- imbalanced-learn
- XGBoost

### Data Visualization

- Matplotlib
- Seaborn

### Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

### Environment

- Python virtual environment
- Shared environment located at:

```text
venv/
```

---

## Project Structure

```text
Credit Card Fraud Detection/
│
├── data/
│   ├── raw/
│   │   └── creditcard.csv
│   └── processed/
│       ├── v1/
│       ├── v2/
│       ├── v3/
│       └── v4/
│
├── fraud-detection-v1/
│   ├── notebooks/
│   │   ├── 01_eda.ipynb
│   │   └── 02_model_training.ipynb
│   ├── src/
│   │   ├── __init__.py
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   └── evaluate.py
│   ├── models/
│   ├── reports/
│   ├── README.md
│   └── requirements.txt
│
├── fraud-detection-v2/
│   ├── notebooks/
│   │   ├── 01_model_comparison.ipynb
│   │   └── 02_hyperparameter_tuning.ipynb
│   │
│   ├── src/
│   │   ├── __init__.py
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   └── evaluate.py
│   │
│   ├── models/
│   ├── reports/
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
│
├── fraud-detection-v3/
│   ├── notebooks/
│   │   ├── 01_feature_importance.ipynb
│   │   └── 02_model_explainability.ipynb
│   ├── src/
│   ├── models/
│   ├── reports/
│   ├── README.md
│   └── requirements.txt
│
├── fraud-detection-v4/
│   ├── notebooks/
│   │   └── 01_final_pipeline.ipynb
│   ├── src/
│   ├── models/
│   ├── reports/
│   ├── app/
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

The raw dataset is stored only once:

```text
data/raw/creditcard.csv
```

Version-specific outputs can be stored in:

```text
data/processed/v1/
data/processed/v2/
data/processed/v3/
data/processed/v4/
```

V2 models should be stored in:

```text
fraud-detection-v2/models/
```

V2 reports and visualizations should be stored in:

```text
fraud-detection-v2/reports/
```

---

## Setup

Run the following commands from the repository root:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the V2 dependencies:

```powershell
python -m pip install -r .\fraud-detection-v2\requirements.txt
```

If the shared environment does not exist yet, create it from the repository root:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Place the dataset at:

```text
data/raw/creditcard.csv
```

---

## Running the Notebooks

Open the following notebooks:

```text
fraud-detection-v2/notebooks/01_model_comparison.ipynb
fraud-detection-v2/notebooks/02_hyperparameter_tuning.ipynb
```

Select the shared project kernel:

```text
Python (Credit Card Fraud Detection)
```

Because the notebooks are located inside:

```text
fraud-detection-v2/notebooks/
```

load the shared dataset using:

```python
import pandas as pd

df = pd.read_csv("../../data/raw/creditcard.csv")
```

The path works as follows:

- The first `..` moves from `notebooks/` to `fraud-detection-v2/`
- The second `..` moves to the repository root
- `data/raw/creditcard.csv` points to the shared dataset

Run the notebook cells in order.

---

## V2 Workflow

The V2 workflow is:

1. Load the shared raw dataset.
2. Separate features and target.
3. Create a stratified training and testing split.
4. Calculate the class-imbalance ratio.
5. Train the Dummy Classifier.
6. Train Logistic Regression.
7. Train Random Forest.
8. Train XGBoost.
9. Generate predictions and probability scores.
10. Calculate evaluation metrics.
11. Compare model performance.
12. Plot confusion matrices.
13. Analyze false positives and false negatives.
14. Select the strongest candidate.
15. Tune the selected model.
16. Analyze classification thresholds.
17. Save models and results.

---

## Class-Imbalance Strategy

The dataset contains far fewer fraud cases than legitimate transactions.

V2 uses several strategies to reduce the impact of class imbalance:

- Stratified splitting preserves the class distribution.
- Logistic Regression uses `class_weight="balanced"`.
- Random Forest uses `class_weight="balanced_subsample"`.
- XGBoost uses `scale_pos_weight`.
- PR-AUC is used as an important comparison metric.

Resampling methods such as SMOTE may be explored in future experiments.

If resampling is used, it must be applied only to the training data. Applying resampling before the train/test split can cause data leakage.

---

## Evaluation Metrics

The models are evaluated using:

- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Confusion matrix
- Classification report

### Precision

Precision measures how many transactions predicted as fraud were actually fraudulent.

### Recall

Recall measures how many actual fraudulent transactions were detected.

High recall is important because the goal is to catch fraudulent transactions.

### F1-score

F1-score balances precision and recall.

### ROC-AUC

ROC-AUC measures the model's ability to separate legitimate and fraudulent transactions across different thresholds.

### PR-AUC

PR-AUC focuses on the relationship between precision and recall.

It is especially useful for rare-event detection and highly imbalanced classification.

### Confusion Matrix

The confusion matrix contains:

- True negatives
- False positives
- False negatives
- True positives

The main comparison metric for V2 is **PR-AUC**, supported by recall, precision, and F1-score.

Accuracy is not used as the main selection metric.

---

## Expected Outcome

At the end of V2, the project should contain:

- A trained version of each comparison model
- A results table containing evaluation metrics
- Confusion matrices
- Classification reports
- Precision-recall comparisons
- A preliminary model ranking
- A selected candidate for hyperparameter tuning
- Threshold-analysis results
- Saved model files in `fraud-detection-v2/models/`
- Evaluation reports in `fraud-detection-v2/reports/`

The best model will not be selected using accuracy alone.

The final decision will consider the trade-off between:

- Detecting more fraudulent transactions
- Maintaining acceptable precision
- Reducing false positives
- Achieving strong PR-AUC and F1-score

---

## V2 Roadmap

### V1 — Foundation and Baseline

V1 focuses on:

- Exploratory data analysis
- Understanding class imbalance
- Basic preprocessing
- Train/test splitting
- Baseline model training
- Fraud-focused evaluation

### V2 — Model Comparison and Tuning

V2 focuses on:

- Comparing multiple models
- Handling class imbalance
- Hyperparameter tuning
- Threshold analysis
- Improving recall and precision
- Selecting a strong candidate model

### V3 — Explainability

V3 will focus on:

- Feature importance
- Model interpretation
- SHAP analysis
- Understanding model predictions
- Explaining results to stakeholders

### V4 — Practical Application

V4 will focus on:

- Building a reusable prediction pipeline
- Saving and loading trained models
- Creating an API or dashboard
- Preparing the project for deployment
- Improving reproducibility and presentation

---

## Next Steps

After completing the initial model comparison:

1. Select the strongest candidate model.
2. Tune its hyperparameters.
3. Test different classification thresholds.
4. Compare threshold effects on precision and recall.
5. Save the final model.
6. Save preprocessing objects.
7. Save evaluation results and visualizations.
8. Prepare the selected model for explainability work in V3.