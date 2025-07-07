# 🛍️ Online Retail RFM Segmentation

This project performs **RFM (Recency, Frequency, Monetary)** analysis on an e-commerce dataset to segment customers and recommend targeted marketing actions.

---

## 📁 Files

- `Online Retail.xlsx` — Raw transaction data
- `rfm_segmentation.ipynb` — Jupyter notebook with full analysis

---

## 🎯 Objectives

- Clean and prepare transaction data
- Calculate RFM metrics per customer
- Generate RFM scores and combine into a segmentation strategy
- Visualize segment distribution
- Map each segment to a suggested marketing action

---

## 🔢 Key Features & Process

### 📌 Data Prep

- Dropped null `CustomerID`s
- Converted datatypes and created new columns: `TotalPrice`, `Year`, `Month`, `Day`, `Hour`

### 📊 RFM Metrics

| Metric     | Description                                       |
|------------|---------------------------------------------------|
| **Recency** | Days since last purchase (as of Dec 9, 2011)     |
| **Frequency** | Total unique purchases (invoices)               |
| **Monetary** | Total money spent by customer                   |

### 🧠 RFM Scoring

- Scores scaled from 1 (low) to 5 (high) using `qcut`
- Final `RFM_Score` = combination of R, F, and M scores

### 🧩 Segments Defined

| Segment Name         | Example Score Pattern | Description                          |
|----------------------|-----------------------|--------------------------------------|
| Champion             | 555, 554, etc.        | Recent, frequent, big spenders       |
| Loyal                | 433+, 344+, etc.      | High frequency, high value           |
| New Customer         | 511, 521              | Very recent, small spend             |
| At Risk              | 1–2 recency, moderate freq/value | Losing engagement              |
| Dormant Big Spender  | 1–3 recency, 3–5 monetary | Inactive but spent a lot         |
| Hibernating          | Low RFM across all    | Likely churned                       |
| Lost                 | Lowest across all     | Severely disengaged                 |

---

## 📢 Marketing Actions

Each segment is mapped to a relevant strategy:
- `Champion` → Early access to VIP campaigns
- `Loyal` → Loyalty programs
- `Hibernating` → Flash offer reactivation emails
- `New Customer` → Welcome discount

(see full mapping in `rfm['Marketing_Action']`)

---

## 📊 Visualizations

- **Bar chart** of customers per segment  
- **Heatmap** of average R, F, M scores per segment

---

## 🛠 Tools Used

- Python 3.10+
- pandas
- matplotlib
- seaborn

---

## ✅ How to Run

1. Install dependencies:
```bash
pip install pandas seaborn matplotlib openpyxl
