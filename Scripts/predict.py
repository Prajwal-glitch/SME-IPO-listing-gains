# fastapi_app.py
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

with open('model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

app = FastAPI(title="IPO Listing Price Prediction")

class IPOData(BaseModel):
    issue_amount_: float
    assets_: float
    revenue_: float
    profit_after_tax_: float
    net_worth_: float
    reserves_and_surplus_: float
    total_borrowing_: float
    issue_price_: float
    sub: float
    gmp: float
    anchor: float

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_listing_price(ipo: IPOData):
    data = pd.DataFrame([{
        'issue_amount_(rs.cr.)': ipo.issue_amount_,
        'assets_(rs.cr.)': ipo.assets_,
        'revenue_(rs.cr.)': ipo.revenue_,
        'profit_after_tax_(rs.cr.)': ipo.profit_after_tax_,
        'net_worth_(rs.cr.)': ipo.net_worth_,
        'reserves_and_surplus_(rs.cr.)': ipo.reserves_and_surplus_,
        'total_borrowing_(rs.cr.)': ipo.total_borrowing_,
        'issue_price_(rs)': ipo.issue_price_,
        'sub': ipo.sub,
        'gmp': ipo.gmp,
        'anchor': ipo.anchor
    }])
    
    prediction = model.predict(data)[0]         
    proba = model.predict_proba(data)[0]         

    result = "gains" if prediction == 1 else "loss"
    probability = proba[1] if prediction == 1 else proba[0]

    print(type(probability))

    return {
        "prediction": result,
        "probability": round(float(probability),4)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
