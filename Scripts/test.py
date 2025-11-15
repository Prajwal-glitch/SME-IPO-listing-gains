import pickle
import pandas as pd

with open('model.bin', 'rb') as f_in: 
    model = pickle.load(f_in)

if __name__ == "__main__":

    datapoint = [{
        'issue_amount_(rs.cr.)': 69.54,
        'assets_(rs.cr.)': 117.0,
        'revenue_(rs.cr.)': 620.16,
        'profit_after_tax_(rs.cr.)': 19.47,
        'net_worth_(rs.cr.)': 61.23,
        'reserves_and_surplus_(rs.cr.)': 44.57,
        'total_borrowing_(rs.cr.)': 0.16,
        'issue_price_(rs)': 122,
        'sub': 4.11,
        'gmp': 1.0,
        'anchor': 1.0
    }]


    data = pd.DataFrame(datapoint)

    # Predict first row
    prediction = model.predict(data)
    result = "gains" if prediction else "loss"
    proba = model.predict_proba(data)
    probability = proba[0][1] if prediction else proba[0][0]
    print(f"Predicted -> {result}")
    print(f"Probability -> {round(probability,4)}")
