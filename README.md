# week5
week 5 and 6 assignment 

Fraud Detection for E-commerce and Bank Transactions
Project Overview

This project focuses on improving fraud detection for e-commerce and bank credit transactions at Adey Innovations Inc. The goal is to build accurate and explainable fraud detection models while balancing transaction security and user experience.

This repository documents the end-to-end workflow, starting from exploratory data analysis (EDA) and preprocessing to model building and explainability.

Business Objective

Fraudulent transactions cause financial losses and damage customer trust. The objective of this project is to:

Detect fraudulent transactions accurately

Minimize false positives that negatively impact legitimate users

Address severe class imbalance inherent in fraud detection datasets

Provide interpretable insights that support business decision-making

Datasets

The project uses the following datasets:

Fraud_Data.csv – E-commerce transaction data

IpAddress_to_Country.csv – IP address to country mapping

creditcard.csv – Bank transaction fraud dataset

Task 1: Data Analysis and Preprocessing (Completed)
Key Activities

Data cleaning and type correction

Exploratory Data Analysis (univariate, bivariate, and class imbalance analysis)

IP address to country geolocation integration

Feature engineering (time-based and behavioral features)

Categorical encoding and numerical feature scaling

Class imbalance handling using undersampling (training data only)

Key Insights

Fraudulent transactions account for ~9.36% of e-commerce transactions, confirming strong class imbalance

Fraud rates vary significantly by country, highlighting the importance of geolocation features

Fraudulent users tend to show higher transaction velocity and abnormal transaction frequency

Time-based behavior (hour of day, day of week, time since signup) provides strong fraud signals