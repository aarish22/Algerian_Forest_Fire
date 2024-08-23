# Algerian Forest Fire Prediction

This repository contains the code and resources for predicting forest fire indices using various regression models. The dataset used is the **Algerian Forest Fires Dataset**.

## Project Overview

The goal of this project is to develop a predictive model for forest fire indices, specifically focusing on the Fire Weather Index (FWI). The dataset includes meteorological data, and the target variable is FWI.

## Dataset

The dataset is sourced from [Algerian Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset+).

### Data Preprocessing

- **Region Classification**: Data was categorized into two regions: `Region 0` and `Region 1`.
- **Handling Missing Values**: Rows with missing data were dropped.
- **Feature Transformation**: Relevant features were converted to appropriate data types.
- **Outlier Detection**: Box plots were used to visualize and handle outliers.

### Target Variable

- The target variable is `FWI` (Fire Weather Index).
- The `Classes` variable was converted into binary values, representing `Fire` (1) and `Not Fire` (0).

## Exploratory Data Analysis (EDA)

- **Correlation Analysis**: A heatmap was generated to identify highly correlated features.
- **Distribution Analysis**: Histograms and pie charts were created to visualize data distributions and class proportions.

## Model Training

Several regression models were trained on the dataset:

1. **Linear Regression**
2. **Lasso Regression**
3. **Ridge Regression**
4. **ElasticNet Regression**

### Model Evaluation

Each model was evaluated based on:

- **Mean Absolute Error (MAE)**
- **R-squared (R²) Score**

Scatter plots of predictions vs. actual values were used to visualize model performance.

## Feature Engineering

- **Feature Scaling**: StandardScaler was used to normalize the feature set.
- **Correlation Thresholding**: Features with a correlation above 0.85 were dropped to reduce multicollinearity.

## Results

| Model            | MAE   | R² Score |
|------------------|-------|----------|
| Linear Regression| 0.57  | 0.98     |
| Lasso Regression | 1.13  | 0.94     |
| Ridge Regression | 0.59  | 0.98     |
| ElasticNet       | 1.85  | 0.87     |


## Files

- **Algerian_Forest_Cleaned.csv**: Cleaned dataset.
- **ridge.pkl**: Trained Ridge regression model.
- **scaler.pkl**: StandardScaler object for scaling features.

## Conclusion
- The project demonstrates the process of predicting forest fire indices using regression techniques. The Ridge regression model provided the best performance among the models tested.
