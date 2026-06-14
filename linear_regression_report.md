# Linear Regression Practical Task Report

## Introduction

This project focuses on implementing and evaluating Linear Regression models using the California Housing Dataset. The objective was to understand regression modeling, compare model performance, and analyze evaluation metrics.

## Tools and Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Tasks Performed

### Task 1: Baseline Linear Regression Model

* Loaded and cleaned the housing dataset
* Split the dataset into training and testing sets
* Trained a Linear Regression model
* Generated predictions
* Calculated evaluation metrics:

  * MSE
  * RMSE
  * MAE
  * R² Score
* Compared actual vs predicted values

### Task 2: One-Feature vs Multi-Feature Models

* Built Model A using one feature
* Built Model B using multiple features
* Compared model performance using regression metrics
* Observed that the multi-feature model performed better

### Task 3: Different Train/Test Splits

* Tested Linear Regression with:

  * 80/20 split
  * 70/30 split
  * 60/40 split
* Compared train and test performance
* Evaluated model stability across splits

### Task 4: Metric Verification and Exploration

* Calculated regression metrics manually
* Compared manual calculations with sklearn outputs
* Added Median Absolute Error as an additional metric
* Performed artificial error experiments
* Observed that MSE and RMSE react strongly to large prediction errors

## Conclusion

The project successfully demonstrated the implementation and evaluation of Linear Regression models. The experiments showed how feature selection, train-test splitting, and evaluation metrics affect model performance and prediction quality.
