# SME IPO Listing Gain Prediction – Machine Learning Project

## 📌 Problem Statement

SME IPOs in India often witness sharp listing-day volatility. Retail investors struggle to assess whether a new SME IPO is likely to provide **listing gains**. This project aims to build a **machine learning model** that helps in decision-making for buying an SME IPO **specifically for listing-day gains and exiting the position**.

---

## 📂 Dataset Description

The dataset includes publicly available SME IPO data scraped from [InvestorGain](https://www.investorgain.com/), containing:

* **Company financials** (Revenue, PAT, Assets)
* **IPO details** (issue size, price band, subscription levels)
* **Market sentiment indicators**
* **Listing price and returns**

The target variable:

* **Listing Gain (Boolean value)** – 1 for listing gains else 0

---

## 🔍 Exploratory Data Analysis (EDA) Summary

Key insights from the dataset:

* High correlation between **subscription levels** and listing gains
* Oversubscribed IPOs tend to exhibit stronger gains
* Grey market premium and presence of anchor have highest feature importance
* Clear presence of outliers due to SME market volatility

EDA included:

* Missing value treatment
* Outlier analysis
* Distribution plots
* Correlation heatmap

---

## 🤖 Modeling Approach

Multiple ML models were trained and compared:

* Logistic Regression
* Random Forest Classifier
* XGBoost Classifier

**Evaluation Metrics:**

* macro recall

The best-performing model was selected based on **highest macro recall**.

---

## 🛠️ How to Run the Project Locally

## 🚀 Setup Instructions (Using uv)

To clone the repository and install all dependencies with **uv**, run:

```bash
# Clone the repository
git clone https://github.com/Prajwal-glitch/SME-IPO-listing-gains.git
cd SME-IPO-listing-gains

# Install dependencies using uv
uv sync --locked || uv sync
```

Make sure you are at root of repo before executing below commands
```bash
# Try running each server in different terminal

# First terminal 
# Start FastAPI backend
cd Scripts
uv run uvicorn predict:app --host 0.0.0.0 --port 9696

```

```bash

# Second terminal
# Start Streamlit UI
cd Scripts
uv run streamlit run streamlit_app.py

```


---

## 🐳 Run Using Docker

### **1. Build Docker image**

```bash
docker build -t ipo-app .
```

### **2. Run container**

```bash
docker run -it --rm -p 9696:9696 -p 8501:8501 ipo-app
```

---

## 📡 API Usage Example

### **Endpoint: POST /predict**

```json
{
  "issue_amount_": 69.54,
  "assets_": 117.0,
  "revenue_": 620.16,
  "profit_after_tax_": 19.47,
  "net_worth_": 61.23,
  "reserves_and_surplus_": 44.57,
  "total_borrowing_": 0.16,
  "issue_price_": 122,
  "sub": 4.11,
  "gmp": 1.0,
  "anchor": 1.0
}

```

#### **Sample Response**

```json
{
  "prediction": "gains",
  "probability": 0.7186
}
```

---

## ⚠️ Known Limitations & Next Steps

### **Limitations**

* SME market is highly volatile → prediction uncertainty remains high
* Limited dataset availability
* No sentiment or news-based features yet

### **Next Steps**

* Integrate **real-time market sentiment** (Twitter, news, IPO grey market)
* Add **explainable AI** (SHAP values)
* Build Streamlit dashboard
* Deploy full API on Fly.io or AWS

---

## 🏗️ Architecture Diagram

```
   [Raw SME IPO Data]
            |
            v
     [Feature Engineering]
            |
            v
   [Trained ML Model (.pkl)]
            |
            v
      [FastAPI Backend]
            |
            v
        [API /predict]
```

---

## 📘 Author

Prajwal Patil – Machine Learning & Finance Enthusiast

#DataTalksClub
