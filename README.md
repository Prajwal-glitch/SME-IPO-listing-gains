# SME IPO Listing Gain Prediction – Machine Learning Project

## 📌 Problem Statement

SME IPOs in India often witness sharp listing-day volatility. Retail investors struggle to assess whether a new SME IPO is likely to provide **listing gains**. This project aims to build a **machine learning model** that helps in decision-making for buying an SME IPO **specifically for listing-day gains and exiting the position**.

---

## 📂 Dataset Description

The dataset includes publicly available SME IPO data scraped from financial portals, containing:

* **Company financials** (Revenue, PAT, Assets)
* **IPO details** (issue size, price band, subscription levels)
* **Market sentiment indicators**
* **Listing price and returns**

The target variable:

* **Listing Gain (%)** – % change between issue price and listing price

---

## 🔍 Exploratory Data Analysis (EDA) Summary

Key insights from the dataset:

* High correlation between **subscription levels** and listing gains
* Oversubscribed IPOs tend to exhibit stronger gains
* Issue size and valuation multiples show non-linear relationships
* Clear presence of outliers due to SME market volatility

EDA included:

* Missing value treatment
* Outlier analysis
* Distribution plots
* Correlation heatmap

---

## 🤖 Modeling Approach

Multiple ML models were trained and compared:

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor
* Gradient Boosting

**Evaluation Metrics:**

* RMSE
* R² Score

The best-performing model was selected based on **lowest RMSE** and **highest R²**.

---

## 🛠️ How to Run the Project Locally

### **1. Clone the repository**

```bash
git clone <your-repo-url>
cd sme-ipo-ml
```

### **2. Create virtual environment & install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Run FastAPI backend**

```bash
uvicorn app.main:app --reload
```

### **4. API will be live at:**

```
http://127.0.0.1:8000
```

---

## 🐳 Run Using Docker

### **1. Build Docker image**

```bash
docker build -t sme-ipo-ml .
```

### **2. Run container**

```bash
docker run -p 8000:8000 sme-ipo-ml
```

---

## 📡 API Usage Example

### **Endpoint: POST /predict**

```json
{
  "issue_size": 42,
  "subscription": 110.5,
  "revenue_growth": 18.2,
  "pat_margin": 12.5
}
```

#### **Sample Response**

```json
{
  "predicted_listing_gain": 24.7
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
* Deploy full API on Fly.io or Railway

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
