# Credit Card Fraud Detection — V2
## Model Comparison and Evaluation

V2 extends the exploratory analysis completed in V1 by training and comparing machine-learning models for credit-card fraud detection.

The main objective is to identify a model that can detect fraudulent transactions effectively despite the severe class imbalance in the dataset.
--

## Project Objective

The dataset contains credit-card transactions labeled as either:

- `0`: Legitimate transaction
- `1`: Fraudulent transaction

Fraudulent transactions represent only a very small proportion of all transactions. Therefore, accuracy alone is not an appropriate metric for evaluating the models.

V2 focuses on:

- Preparing the data for machine learning
- Creating a stratified train/test split
- Handling class imbalance
- Training multiple classification models
- Comparing model performance
- Analyzing false positives and false negatives
- Selecting a strong candidate for further tuning

---

## Models Compared

The comparison includes four models:

### 1. Dummy Classifier

The Dummy Classifier is used as a reference baseline. It does not learn meaningful patterns from the data and helps demonstrate why accuracy is misleading for this problem.

### 2. Logistic Regression

Logistic Regression is used as an interpretable baseline model. It provides a simple starting point and allows us to understand how well a linear model performs.

### 3. Random Forest

Random Forest is an ensemble of decision trees. It can model nonlinear relationships and interactions between features.

### 4. XGBoost

XGBoost is a gradient-boosting model designed for strong performance on structured tabular data. It is expected to be one of the strongest candidates for this problem.

---

## Evaluation Metrics

The models are evaluated using metrics suited to highly imbalanced classification:

- **Precision:** The proportion of predicted fraud cases that are actually fraudulent.
- **Recall:** The proportion of actual fraud cases detected by the model.
- **F1-score:** The harmonic mean of precision and recall.
- **ROC-AUC:** Measures how well the model separates the two classes across thresholds.
- **PR-AUC:** Measures performance on the positive fraud class and is especially important for rare-event detection.
- **Confusion matrix:** Shows true negatives, false positives, false negatives, and true positives.

The main comparison metric is **PR-AUC**, supported by recall, precision, and F1-score.

---

## Dataset

The project uses the Credit Card Fraud Detection dataset.

The dataset contains:

- 284,807 transactions
- 30 input features
- 1 binary target column named `Class`
- 492 fraudulent transactions
- 284,315 legitimate transactions

The dataset is highly imbalanced:

- Legitimate transactions: approximately 99.83%
- Fraudulent transactions: approximately 0.17%

The raw dataset is stored at:

```text
data/raw/creditcard.csv
```

---

## Project Structure

```text
fraud-detection-v2/
├── data/
│   └── raw/
│       └── creditcard.csv
├── models/
├── notebooks/
│   ├── 01_model_comparison.ipynb
│   └── 02_hyperparameter_tuning.ipynb
├── reports/
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Workflow

The V2 workflow is:

1. Load the dataset.
2. Separate features and target.
3. Create a stratified training and testing split.
4. Calculate the class-imbalance ratio.
5. Train the Dummy Classifier, Logistic Regression, Random Forest, and XGBoost models.
6. Generate predictions and probability scores.
7. Calculate the evaluation metrics.
8. Compare the models.
9. Visualize confusion matrices.
10. Select the strongest candidate.
11. Tune the selected model in the next notebook.
12. Analyze classification thresholds.

---

## Class-Imbalance Strategy

The dataset contains far fewer fraud cases than legitimate transactions.

To reduce the impact of this imbalance:

- Logistic Regression uses `class_weight="balanced"`.
- Random Forest uses `class_weight="balanced_subsample"`.
- XGBoost uses `scale_pos_weight`.
- Stratified splitting preserves the class distribution in the training and test sets.

Resampling methods such as SMOTE may be explored during later experimentation, but resampling must only be applied to the training data to avoid data leakage.

---

## Environment Setup

The project uses the shared virtual environment located at the repository root:

```text
Credit Card Fraud Detection/venv/
```

Activate it from the repository root:

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Install the V2 dependencies:

```powershell
python -m pip install -r .\fraud-detection-v2\requirements.txt
```

The notebook kernel is:

```text
Python (Credit Card Fraud Detection)
```

---

## Running the Notebook

Open:

```text
notebooks/01_model_comparison.ipynb
```

Select the kernel:

```text
Python (Credit Card Fraud Detection)
```

Run the notebook cells in order.

The dataset path used from the notebook is:

```python
df = pd.read_csv("../data/raw/creditcard.csv")
```

---

## Expected Outcome

At the end of the first notebook, we should have:

- A trained version of each comparison model
- A results table containing all evaluation metrics
- Confusion matrices
- Classification reports
- A preliminary ranking of the models
- A selected candidate for hyperparameter tuning

The best model will not be selected using accuracy alone. The decision will consider the trade-off between detecting more fraud cases and limiting false alarms.

---

## Next Steps

After completing the model comparison:

1. Tune the best-performing model.
2. Test different model parameters.
3. Adjust the classification threshold.
4. Compare the effect of threshold changes on precision and recall.
5. Save the selected model and preprocessing objects.
6. Prepare the project for explainability work in V3.

---

## Version Roadmap

- **V1:** Exploratory Data Analysis
- **V2:** Model comparison, tuning, and evaluation
- **V3:** Model explainability and feature interpretation
- **V4:** Deployment and practical fraud-detection application