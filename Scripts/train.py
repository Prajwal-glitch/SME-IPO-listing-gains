import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle


def prepare_data():
    df = pd.read_csv("../Data/clean_data.csv")
    
    # Not used in model
    company_name = df["company_name"]
    df = df.drop("company_name", axis=1)

    df.fillna(0, inplace=True)

    y = df["listing_gains"]   # True = Loss, False = Gain
    del df["listing_gains"]

    X = df
    return X, y 


def train_model(X, y):
    # Best hyperparameters you provided (cleaned up for XGBoost)
    best_params = {
        'colsample_bytree': 0.8099,
        'learning_rate': 0.1012,
        'max_depth': 9,
        'n_estimators': 150,
        'scale_pos_weight': 10,     # Helps with class imbalance
        'subsample': 0.8543,
        'eval_metric': 'logloss',
    }

    model = XGBClassifier(**best_params)
    model.fit(X, y)

    return model


def save_model(model):
    with open("model.bin", "wb") as f_out:
        pickle.dump(model, f_out)
    print("========= Model saved to model.bin =========")


if __name__ == "__main__":
    X, y = prepare_data()
    model = train_model(X, y)
    save_model(model)
