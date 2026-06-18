# Phase 2 Mini Project Report

## Project Title

Order Delay Intelligence: Predict, Explain, Recommend

## Objective

The objective of this project was to analyze e-commerce order delivery data and build machine learning models capable of predicting delivery delays. The project also aimed to generate business insights through SQL analysis and data visualization.

## Dataset Used

The project used the Olist E-commerce Dataset containing information related to:

* Orders
* Customers
* Payments
* Order Items
* Products

## Data Audit and Cleaning

The following preprocessing steps were performed:

* Loaded and inspected multiple datasets
* Checked dataset dimensions and structure
* Identified missing values
* Converted date columns into datetime format
* Created new features such as:

  * delivery_days
  * delay_days
  * purchase_weekday
  * purchase_month
* Merged datasets into a unified analytical dataset

## Exploratory Data Analysis (EDA)

Several visualizations were created to understand business patterns:

1. Revenue Distribution
2. Payment Type Analysis
3. Monthly Order Trend
4. Delay Days Distribution
5. Average Delay by Weekday
6. Correlation Heatmap

### Key Findings

* Most orders were delivered on time.
* Payment values showed a right-skewed distribution.
* Delivery delays varied across weekdays.
* Monthly order volumes showed seasonal trends.
* Freight charges influenced overall order cost.

## SQL Analysis

SQLite was used to perform business-oriented analysis.

Queries included:

* Total orders
* Order status distribution
* Average payment by payment type
* Top customer states by orders
* Monthly order volume
* Average delay analysis
* Revenue analysis
* Delayed order identification
* Subquery-based customer analysis

### SQL Insight

Results obtained from SQL matched pandas-based calculations, validating data consistency.

## Machine Learning Model

### Problem Statement

Predict whether an order will be delayed.

Target Variable:

* 1 = Delayed
* 0 = Not Delayed

### Features Used

* payment_value
* price
* freight_value
* purchase_month

## Logistic Regression

A baseline Logistic Regression model was trained and evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

### Observation

The model successfully classified delayed and non-delayed orders and provided a baseline benchmark.

## XGBoost Model

An XGBoost classifier was implemented using a Scikit-Learn pipeline.

Pipeline components:

* Missing value imputation
* Feature scaling
* XGBoost classifier

### Observation

XGBoost demonstrated improved predictive performance by capturing more complex relationships within the data.

## Cross Validation

5-Fold Cross Validation was performed to evaluate model stability.

### Result

The model achieved consistent performance across multiple folds, indicating reliable generalization.

## Model Explainability using SHAP

SHAP values were used to understand feature contributions.

### Key Insight

Feature importance analysis highlighted the most influential variables affecting delivery delay predictions.

## Business Recommendations

1. Monitor orders with high freight charges more closely.
2. Identify high-risk delayed orders early.
3. Improve logistics planning during peak demand periods.
4. Use predictive analytics to enhance customer satisfaction.
5. Deploy advanced models such as XGBoost for operational decision-making.

## Conclusion

This project successfully combined data analysis, SQL, machine learning, cross-validation, and explainable AI techniques to build an Order Delay Prediction System. The developed solution can help businesses proactively identify delivery risks and improve operational efficiency and customer experience.
