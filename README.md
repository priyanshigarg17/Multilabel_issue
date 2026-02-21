
# 📌 Multi-Label E-commerce User Interest Classification

## 📖 Problem Statement

In modern e-commerce platforms, a single user can be interested in multiple product categories simultaneously.

For example, a user may show interest in:

* Fashion
* Electronics
* Books
* Sports
* Home Decor

Traditional multi-class classification models assume that each instance belongs to only one class. However, in this case, categories are **not mutually exclusive**.

Therefore, this problem must be treated as a **Multi-Label Classification problem**, where each user can belong to multiple categories at the same time.

---

## 🎯 Objective

To build a machine learning model that predicts multiple product category interests for each user based on:

* Age
* Annual Income
* Purchase Frequency
* Time Spent on App
* Premium Membership Status

The goal is to help the business:

* Improve personalized recommendations
* Enable targeted marketing
* Increase conversion rates
* Improve user engagement

---

## 🧠 Problem Type

This is a **Multi-Label Classification Problem**, not a multi-class problem.

Why?

Because:

* A user can belong to multiple categories.
* Labels are independent.
* There is no competition between classes.

---

## 🚨 Initial Modeling Challenge

A multi-class modeling approach would incorrectly assume that:

> A user can belong to only one category.

This would force the model to predict only a single label, leading to:

* Loss of information
* Poor recommendation performance
* Business misalignment

---

## ✅ Solution Approach

To correctly solve the problem:

### 1️⃣ Multi-Label Strategy

Each category was treated as an independent binary classification problem using a One-vs-Rest strategy.

This means:

* One model predicts "Is Fashion?"
* One model predicts "Is Electronics?"
* One model predicts "Is Books?"
* and so on.

---

### 2️⃣ Models Used

Two machine learning approaches were applied:

* Logistic Regression (Baseline Model)
* Random Forest (Improved Non-Linear Model)

Random Forest was used to capture complex patterns and non-linear relationships in user behavior.

---

### 3️⃣ Hyperparameter Tuning

For Random Forest:

* Number of trees (n_estimators)
* Maximum depth (max_depth)
* Minimum samples per split
* Minimum samples per leaf
* Feature selection strategy

These were optimized using cross-validation with micro-averaged F1 score.

---

## 📊 Evaluation Metrics

Since this is a multi-label problem, traditional accuracy alone is not sufficient.

The following metrics were used:

### 🔹 Exact Match Accuracy

Percentage of users where all predicted labels exactly match the true labels.

### 🔹 Hamming Loss

Measures the fraction of incorrect label predictions.

### 🔹 Micro F1 Score

Balances precision and recall across all labels.

---

## 📈 Model Performance

* Exact Match Accuracy ≈ 79.5%
* Hamming Loss ≈ 4.4%
* Micro F1 Score ≈ 94.2%

### Interpretation:

* The model predicts user interests reliably.
* Very few label-level errors.
* Strong balance between precision and recall.

---

## 🚀 Business Impact

This solution enables:

* Accurate multi-category recommendation
* Smarter ad targeting
* Better user segmentation
* Higher personalization accuracy

---

## 🏁 Conclusion

This project demonstrates the correct handling of a real-world multi-label classification problem by:

* Identifying incorrect multi-class assumptions
* Redesigning the modeling approach
* Applying One-vs-Rest strategy
* Using appropriate evaluation metrics
* Improving performance through hyperparameter tuning

It highlights the importance of aligning machine learning design with actual business requirements.

