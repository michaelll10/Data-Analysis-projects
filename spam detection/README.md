# 📨 Spam Email Detection using KNN & TF-IDF

## 📘 Overview
This project builds a **Spam Email Classifier** using **TF-IDF vectorization** and **K-Nearest Neighbors (KNN)**.  
It demonstrates the complete machine learning workflow — from preprocessing to model evaluation and custom threshold tuning using the Precision–Recall curve.

---

## 🧩 Features
- Loads and processes email dataset  
- Splits data into training and testing sets  
- Converts text into TF-IDF vectors  
- Trains a **KNN model** (`metric='cosine'`)  
- Performs **cross-validation** to check model stability  
- Draws a **Precision–Recall Curve**  
- Tests **custom decision thresholds** (e.g. `0.777`)  
- Evaluates performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

---

## ⚙️ Requirements

Install the necessary libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn imbalanced-learn category-encoders
