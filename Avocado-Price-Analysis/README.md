# 🥑 Avocado Price Analysis & Visualization

This project explores the **Avocado Price dataset** through univariate, bivariate, and multivariate visualizations using **Pandas**, **Plotly**, **Seaborn**, and **Dash**.

---

## 📁 Files

- `avocado.csv` — Raw dataset
- `avocado_analysis.ipynb` — Jupyter Notebook with all visualizations
- (Optional) `dash_app.py` — Dash app version of selected visualizations

---

## 📊 Dataset Details

- **Date** — Date of observation  
- **AveragePrice** — Average price of a single avocado  
- **type** — Type of avocado (conventional/organic)  
- **year**, **month** — Derived from date  
- **region** — Region of sale  
- **Total Volume** — Total number of avocados sold  
- **4046, 4225, 4770** — PLU codes for avocado types sold  

---

## 📈 Visualizations Included

| Chart Type      | Description |
|------------------|-------------|
| 📊 Histogram       | Distribution of average prices (e.g., Jan 2018) |
| 📉 Distplot        | Distribution curve of average prices |
| 📦 Box Plot        | Overall and monthly price comparisons |
| 🔍 Scatter Plot    | Price vs. total bags sold |
| 📌 Pairplot        | Relationship between price, bags, and region |
| 📈 Line Chart      | Monthly price trends for each year |
| 🟣 Strip Plot      | Price spread by year |
| 🧱 Bar Chart       | Grouped bars by month and year |
| 📊 Facet Bar Chart | Volume & price per region over time |

---

## 🧠 Key Insights

- **Right-skewed price distribution**, with outliers over \$2.5
- **Seasonal pricing patterns**: Prices fluctuate month to month, especially in 2017–2018
- **Higher total volume doesn't always mean lower prices**
- Region-level patterns can vary drastically by year

---

## 🛠 Tools Used

- Python 3.10+
- pandas
- plotly
- seaborn
- jupyter-dash
- dash (optional)

---

## ✅ How to Run

1. Install required packages:
```bash
pip install pandas seaborn plotly dash jupyter-dash
