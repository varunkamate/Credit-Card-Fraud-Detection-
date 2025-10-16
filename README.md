💳 Credit Card Fraud Detection App


📊 Dataset:===> https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

LIVE APP LINK:=====> https://gcuv7nsu7wb5bxqwigzt6m.streamlit.app/

This project is a Streamlit web application that predicts whether a given credit card transaction is fraudulent or legitimate using a trained Random Forest Classifier model.

🔍 Overview

The app allows users to input transaction feature values (V1–V28 and Amount) and instantly receive a prediction result. It’s built on the popular Credit Card Fraud Detection dataset from Kaggle, where features are derived from PCA transformations to maintain privacy.

⚙️ Features

Interactive web interface built with Streamlit

Real-time fraud prediction using a pre-trained Random Forest model

Data input form with 29 numerical features

Displays the prediction result clearly (Fraudulent ❌ or Legitimate ✅)

Sidebar section with model details and dataset info

🧠 Model

The model (Random_Forest_best_model.pkl) was trained using the Kaggle Credit Card Fraud Detection dataset. The Random Forest algorithm was selected for its high accuracy and ability to handle class imbalance effectively.

🚀 How to Run

Clone the repository

git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection


Install the required dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py

🧾 Files Included

app.py – Streamlit app source code

Random_Forest_best_model.pkl – Trained Random Forest model

requirements.txt – Required dependencies

