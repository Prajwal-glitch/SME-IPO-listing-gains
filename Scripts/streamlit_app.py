import streamlit as st
import requests

st.set_page_config(page_title="SME IPO Listing Price Predictor", page_icon="📈", layout="wide")
st.title("SME IPO Listing Price Predictor")

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Enter IPO Details")

    r1c1, r1c2, r1c3 = st.columns(3)
    issue_amount_ = r1c1.number_input("Issue Amount (Rs.cr.)", value=22.18)
    assets_ = r1c2.number_input("Assets (Rs.cr.)", value=35.65)
    revenue_ = r1c3.number_input("Revenue (Rs.cr.)", value=52.02)

    r2c1, r2c2, r2c3 = st.columns(3)
    profit_after_tax_ = r2c1.number_input("Profit After Tax (Rs.cr.)", value=6.77)
    net_worth_ = r2c2.number_input("Net Worth (Rs.cr.)", value=15.27)
    reserves_and_surplus_ = r2c3.number_input("Reserves & Surplus (Rs.cr.)", value=0.0)

    r3c1, r3c2, r3c3 = st.columns(3)
    total_borrowing_ = r3c1.number_input("Total Borrowing (Rs.cr.)", value=0.0)
    issue_price_ = r3c2.number_input("Issue Price (Rs)", value=75.0)
    sub = r3c3.number_input("Subscription", value=682.14)

    r4c1, r4c2, r4c3 = st.columns(3)
    gmp = r4c1.number_input("Grey Market Premium", value=1995.0)
    anchor_input = r4c2.selectbox("Anchor Investor?", ["Yes", "No"])
    anchor = 1 if anchor_input == "Yes" else 0
    r4c3.write("")

    if st.button("Predict Listing Price"):
        payload = {
            "issue_amount_": issue_amount_,
            "assets_": assets_,
            "revenue_": revenue_,
            "profit_after_tax_": profit_after_tax_,
            "net_worth_": net_worth_,
            "reserves_and_surplus_": reserves_and_surplus_,
            "total_borrowing_": total_borrowing_,
            "issue_price_": issue_price_,
            "sub": sub,
            "gmp": gmp,
            "anchor": anchor
        }
        try:
            response = requests.post("http://127.0.0.1:9696/predict", json=payload)
            result = response.json()
            st.success(f"Predicted: {result['prediction']}")
            st.info(f"Probability: {result['probability']}")
        except Exception as e:
            st.error(f"Error calling backend: {e}")

with right_col:
    st.subheader("Variable Descriptions")
    st.markdown("""
- Issue Amount (Rs.cr.)
- Assets (Rs.cr.)
- Revenue (Rs.cr.)
- Profit After Tax (Rs.cr.)
- Net Worth (Rs.cr.)
- Reserves & Surplus (Rs.cr.)
- Total Borrowing (Rs.cr.)
- Issue Price (Rs)
- Subscription
- Grey Market Premium (GMP)
- Anchor Investor
    """)
