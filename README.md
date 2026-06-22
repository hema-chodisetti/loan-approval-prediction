# Loan Approval Prediction System

A machine learning project that predicts whether a loan application is likely to be approved or rejected based on applicant and financial details.

## Project Overview

The goal of this project is to build a classification model that can predict loan approval status using features such as income, loan amount, CIBIL score, loan term, asset value, education, employment status, and other applicant details.

This project follows the complete machine learning workflow: data cleaning, exploratory data analysis, feature encoding, model training, model evaluation, model saving, and deployment using Streamlit.

## Features

- Predicts whether a loan will be approved or rejected
- Uses applicant financial and personal details
- Performs data cleaning and preprocessing
- Uses classification algorithms for prediction
- Compares Logistic Regression and Random Forest Classifier
- Saves the trained model using Joblib
- Provides a Streamlit web application for user-friendly prediction

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

## Machine Learning Concepts Used

### Data Preprocessing

Data preprocessing is the process of cleaning and preparing raw data before training a machine learning model. In this project, preprocessing included handling column names, checking missing values, encoding categorical variables, and preparing features for model training.

### Exploratory Data Analysis

Exploratory Data Analysis, also called EDA, helps understand the dataset using graphs and statistical summaries. In this project, I used visualizations such as count plots, histograms, and heatmaps to understand feature relationships.

### Feature Encoding

Machine learning models work with numbers, so categorical values such as education, employment status, self-employed status, and property type were converted into numerical format.

### Train-Test Split

The dataset was divided into training and testing data. The training data was used to train the model, and the testing data was used to check how well the model performs on unseen data.

### Logistic Regression

Logistic Regression is a classification algorithm used to predict categorical outcomes. In this project, it was used as a baseline model to predict loan approval or rejection.

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting. In this project, Random Forest performed better and was used as the final model.

### Model Evaluation

The model was evaluated using accuracy, precision, recall, F1-score, and classification report.

## Model Performance

The Random Forest Classifier achieved approximately **79.86% accuracy** on the test data.

## Project Structure

```text
loan-approval-prediction/
│
├── app.py
├── loan_approval_model.pkl
├── requirements.txt
├── README.md
├── loan_approval_prediction.ipynb
└── screenshots/
    └── app_screenshot.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/hema-chodisetti/loan-approval-prediction.git
```

Go to the project folder:

```bash
cd loan-approval-prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run the Streamlit App

Run this command:

```bash
streamlit run app.py
```

After running the command, the application will open in your browser.

## Input Features Used

The model uses applicant details such as:

- CIBIL score
- Annual income
- Loan amount
- Loan term
- Asset value
- Education
- Employment status
- Self-employed status
- Property type
- Number of dependents

## Output

The application predicts one of the following results:

- Loan Approved
- Loan Rejected
## What I Learned

Through this project, I learned how to build an end-to-end machine learning classification system. I practiced data preprocessing, exploratory data analysis, feature encoding, model training, model evaluation, saving a trained model, and building a Streamlit web application.

## Future Improvements

- Improve model accuracy using hyperparameter tuning
- Add more input features
- Deploy the app online
- Improve the user interface
- Add feature importance explanation
- Compare more machine learning models

## Author

Hemalatha Chodisetti

GitHub: [hema-chodisetti](https://github.com/hema-chodisetti)
