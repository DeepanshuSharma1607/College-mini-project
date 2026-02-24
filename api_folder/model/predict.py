import joblib
import pandas as pd
from fastapi import HTTPException
MODEL_VERSION = '1.0.0'

def load_data(year : int):
    try:
        return joblib.load(f"model/model_year_{year}.pkl")
    except FileNotFoundError:
        raise HTTPException(status_code=400,detail="File not found error")

def predict_output(year : int,user_input:dict):
    input=pd.DataFrame([user_input])
    output=load_data(year).predict(input)[0]
    return output

