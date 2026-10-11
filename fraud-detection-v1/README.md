# Credit Card Fraud Detection V1

A machine learning project focused on detecting fraudulent credit card transactions using a real-world imbalanced dataset.

## Project Goal

This project aims to build a model that can identify fraudulent transactions while minimizing false positives. Since fraudulent transactions are rare, this is an imbalanced classification problem.

## Why This Project Matters

Fraud detection is a critical real-world problem in financial systems. The goal is not only to maximize accuracy, but to correctly detect fraud cases while keeping false alarms low.

## Dataset

This project uses the Kaggle Credit Card Fraud Detection dataset.

- Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Number of rows: 284,807
- Fraudulent transactions: 492
- Features: 28 PCA-transformed numerical features, plus Time and Amount
- Target: Class (0 = legitimate, 1 = fraud)

## Tech Stack

- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- imbalanced-learn
- xgboost
- Jupyter Notebook

## Project Structure

```text
fraud-detection-v1/
├── data/
│   ├── raw/
│   │   └── creditcard.csv
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_training.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset and place it in:
```text
data/raw/creditcard.csv
```

4. Open Jupyter Notebook:
```bash
jupyter notebook
```

## Project Roadmap

This project is organized into four phases:

### V1 — Foundation and Baseline

V1 focuses on understanding the dataset and creating a working baseline model. This is the first and most important stage of the project.

In this phase, the project includes:
- Loading and inspecting the dataset
- Checking class imbalance
- Understanding feature distributions
- Handling missing values and basic preprocessing
- Splitting data into train and test sets
- Training a baseline model
- Evaluating the model using fraud-focused metrics

The goal of V1 is not to build the perfect model, but to establish a strong foundation and learn how fraud detection behaves in real data.

### V2 — Improved Performance

V2 focuses on improving model performance beyond the baseline. This includes:
- Comparing multiple models
- Tuning hyperparameters
- Handling class imbalance more effectively
- Evaluating threshold choices for fraud detection

The goal is to achieve better recall without creating too many false positives.

### V3 — Explainability and Practical Use

V3 focuses on making the model more meaningful in real-world usage:
- Feature importance analysis
- Model explainability
- Threshold tuning based on business risk
- Understanding which features contribute most to fraud detection

This phase makes the project more useful and easier to explain to stakeholders.

### V4 — Production-Ready and Portfolio-Ready

V4 focuses on polishing the project for presentation and real deployment:
- Cleaning the training pipeline
- Saving and loading models
- Building a dashboard or API
- Improving organization and reproducibility
- Making the project suitable for portfolio presentation

This phase transforms the project from a study into a professional ML project.

## V1: Specific Focus

V1 is the foundation of the project. It is where the project learns the data and builds the first working model.

V1 includes:
- Loading the dataset
- Checking shape and column names
- Analyzing class distribution
- Inspecting missing values
- Looking at transaction amount and time patterns
- Detecting outliers
- Splitting data into train and test sets
- Training a baseline classifier
- Evaluating with precision, recall, F1-score, confusion matrix, ROC-AUC, and PR-AUC

This phase teaches the most important lesson of fraud detection: accuracy is not enough, because the data is highly imbalanced.

For this project, recall is especially important because the goal is to catch as many actual fraud cases as possible.

## Important Metrics

For fraud detection, we focus on:
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Confusion matrix

Recall is especially important because we want to catch fraudulent transactions, even when they are rare.

## Current Status

This is V1 of the project. The focus is on:
- Understanding the dataset
- Building a correct baseline
- Learning the fundamentals of fraud detection