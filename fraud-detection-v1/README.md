# Credit Card Fraud Detection — V1

## Exploratory Data Analysis and Baseline Modeling

V1 is the foundation of the Credit Card Fraud Detection project. It focuses on understanding the dataset, analyzing the severe class imbalance, exploring transaction patterns, and creating an initial baseline model.

The goal of V1 is not to build the final production model. Instead, it establishes a reliable foundation for the later project versions.

---

## Project Goal

This project aims to identify fraudulent credit-card transactions while minimizing false positives.

Fraud detection is an imbalanced classification problem because fraudulent transactions represent only a very small proportion of all transactions. Therefore, accuracy alone is not an appropriate evaluation metric.

V1 focuses on:

- Understanding the dataset
- Inspecting the dataset structure
- Measuring class imbalance
- Exploring transaction amounts and times
- Checking missing values
- Analyzing feature distributions
- Splitting the data into training and testing sets
- Training a baseline classifier
- Evaluating the baseline using fraud-focused metrics

---

## Why This Project Matters

Fraud detection is an important real-world machine-learning problem in financial systems.

A useful fraud-detection model should:

- Detect as many fraudulent transactions as possible
- Minimize false alarms
- Handle highly imbalanced data
- Provide meaningful evaluation results
- Support future model improvement and explainability

The most important lesson in V1 is that a high accuracy score can be misleading when the dataset is highly imbalanced.

---

## Dataset

This project uses the Kaggle Credit Card Fraud Detection dataset.

Dataset source:

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

All project versions use the same shared raw dataset:

```text
data/raw/creditcard.csv
```

The raw dataset is a large local file and is intentionally excluded from Git.

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
- Shared project environment located in:

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

The raw dataset is stored only once at:

```text
data/raw/creditcard.csv
```

Each project version has its own notebooks, source code, models, reports, and documentation.

---

## Setup

Run the following commands from the repository root:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the V1 dependencies:

```powershell
python -m pip install -r .\fraud-detection-v1\requirements.txt
```

If the shared environment does not exist yet, create it from the repository root:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Place the downloaded dataset at:

```text
data/raw/creditcard.csv
```

---

## Running the Notebooks

Open the following notebooks:

```text
fraud-detection-v1/notebooks/01_eda.ipynb
fraud-detection-v1/notebooks/02_model_training.ipynb
```

Select the project virtual-environment kernel in Jupyter or VS Code.

Because the notebooks are located inside:

```text
fraud-detection-v1/notebooks/
```

the shared dataset must be loaded using:

```python
import pandas as pd

df = pd.read_csv("../../data/raw/creditcard.csv")
```

The path works as follows:

- The first `..` moves from `notebooks/` to `fraud-detection-v1/`
- The second `..` moves to the repository root
- `data/raw/creditcard.csv` points to the shared dataset

Run the notebook cells in order.

---

## V1 Workflow

The V1 workflow is:

1. Load the shared dataset.
2. Inspect the shape and column names.
3. Check the data types.
4. Check for missing values.
5. Analyze the target-class distribution.
6. Explore transaction amounts.
7. Explore transaction times.
8. Analyze feature distributions.
9. Inspect potential outliers.
10. Split the data into training and testing sets.
11. Train a baseline classifier.
12. Generate predictions.
13. Evaluate the baseline model.
14. Save useful results for V2.

---

## Evaluation Metrics

The baseline model is evaluated using:

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

Recall is especially important because missing a fraudulent transaction can be costly.

### F1-score

F1-score balances precision and recall.

### ROC-AUC

ROC-AUC measures how well the model separates legitimate and fraudulent transactions across different thresholds.

### PR-AUC

PR-AUC is especially useful for highly imbalanced classification problems because it focuses more on the positive class.

---

## V1 Roadmap

### V1 — Foundation and Baseline

V1 focuses on:

- Exploratory data analysis
- Understanding class imbalance
- Basic preprocessing
- Train/test splitting
- Baseline model training
- Fraud-focused evaluation

### V2 — Improved Performance

V2 focuses on:

- Comparing multiple models
- Hyperparameter tuning
- Better class-imbalance handling
- Threshold analysis
- Improving recall and precision

### V3 — Explainability

V3 focuses on:

- Feature importance
- Model interpretation
- SHAP analysis
- Understanding why predictions are made
- Communicating results to stakeholders

### V4 — Practical Application

V4 focuses on:

- Building a reusable prediction pipeline
- Saving and loading trained models
- Creating an API or dashboard
- Preparing the project for deployment
- Improving reproducibility and presentation

---

## Current Status

V1 is focused on building a reliable foundation for the project.

The main objectives are:

- Understand the dataset
- Understand the class imbalance
- Build a correct baseline
- Learn which metrics are appropriate
- Prepare the project for model comparison in V2