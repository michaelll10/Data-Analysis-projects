# 🛍️ Sales Data Analysis (Pandas + Plotly + Seaborn)

This project analyzes sales order data from a retail store using **Pandas**, **Plotly**, **Seaborn**, and **Matplotlib**. The analysis focuses on sales trends, customer behavior, product performance, and branch-level comparisons.

---

## 📁 Files

* `sales_analysis.ipynb`: Jupyter Notebook containing all code and visualizations
* `supermarket_sales - Sheet1.csv`: Raw sales data (original Excel sheet converted to CSV)

---

## 🔍 Key Features and Analysis

* Cleaned and standardized column names
* Converted `date` and `time` columns to datetime formats
* Extracted `year`, `month`, and `hour` from the `date` and `time`
* Generated summary statistics and explored categorical variables

---

## 📊 Visualizations

### 🔹 Branch and Sales:

* Pie chart: Total sales per branch
* Box & violin plots: Ratings per branch
* Strip + box combo: Detailed branch rating distribution

### 🔹 Time-based Analysis:

* Line chart: Sales per hour by branch
* Histogram: Distribution of customer ratings

### 🔹 Product and Category Analysis:

* Bar chart: Total per product line by branch
* Bar chart: Avg gross income per product line
* Bar chart: Avg rating and unit price per product line

### 🔹 Customer and Payment Behavior:

* Bar chart: Count of payment methods by gender and branch
* Pie chart: Quantity sold by product line
* Bar chart: Total by branch, gender, and customer type
* Scatter plot: Total vs Rating by gender and branch

---

## ✅ Tools Used

* Python 3.10+
* pandas
* numpy
* seaborn
* matplotlib
* plotly

---

## ✨ Key Insights

* Branches have similar total sales, but **Branch C** has slightly more consistent high ratings.
* **Electronics accessories** and **Food and beverages** are top-selling product lines.
* Sales peak between **12 PM and 3 PM** across branches.
* **Female customers** tend to prefer **Ewallet** payment, while males prefer **Cash**.
* Customer satisfaction (ratings) is generally high, regardless of branch or product.

---

**Author:** Michael Mamdouh
**License:** MIT
