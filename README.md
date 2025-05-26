# Loan-prediction-ml-model

## Project Title:
Loan Eligibility Prediction using Machine Learning

## Objective:
To build a machine learning model that accurately predicts whether a loan applicant is eligible for a loan based on personal, financial, and credit-related features, helping banks streamline their loan approval process and reduce risk.

## Tools & Technologies Used:
Python – for model development
Pandas & NumPy – for data manipulation
Matplotlib  – for exploratory data analysis and visualization
Scikit-learn – for preprocessing, model training, and evaluation
Jupyter Notebook – as the development environment

## Dataset Details:
Source: Kaggle – Loan Prediction Dataset
<a href="https://github.com/NAGESHKATTIMANI/Loan-prediction-ml-model/blob/main/loan-train.csv">Dataset</a>


## Features: Gender, Marital Status, Education, Applicant Income, Loan Amount, Credit History, Property Area, etc.
Target: Loan Status (Y/N)

## Approach:
Data Cleaning:
Handled missing values for features like LoanAmount and Credit_History
Converted categorical variables using Label Encoding 

### Exploratory Data Analysis (EDA):
Uncovered trends such as higher approval rates for applicants with credit history and steady income
Identified correlations between features and target variable

## Model Building:
As it is my first ml project so built it using 
Logistic Regression
and got an accuracy of 80% which ig good for a beginner...:)
Hyperparameter tuning performed using GridSearchCV

##Evaluation Metrics:
Accuracy, Precision, Recall, F1 Score, Confusion Matrix
model achieved ~82% accuracy on test data

## Key Learnings & Insights:
Applicants with credit history, higher income, and less loan amount had better chances of loan approval
Feature importance analysis helped explain model decisions

## Real-world Applications:
Assists banks and NBFCs in automating loan approvals
Minimizes manual errors and improves decision consistency
Can be integrated into a loan application portal with real-time eligibility feedback

📌 Future Scope:
Deploy model as a web app using Flask or Streamlit

Incorporate additional features like credit score, employment history

Retrain periodically with real-time data
