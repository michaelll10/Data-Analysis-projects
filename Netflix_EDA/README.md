# 📊 Netflix Data Analysis

This repository contains an in-depth exploratory data analysis (EDA) on the Netflix Titles dataset, aiming to extract insights such as content trends, popular genres, release patterns, and more.

## 🗂 Dataset

The dataset used is [`netflix_titles.csv`](https://www.kaggle.com/datasets/shivamb/netflix-shows), which includes information about movies and TV shows available on Netflix.

---

## 🔧 Features & Cleaning

The following steps were performed during preprocessing:

- Converted `date_added` to datetime format.
- Filled missing values with:
  - `'unknown'` for `director`, `cast`, and `country`
  - `'Not added'` for `duration`
  - Forward and backward filling for the remaining nulls
- Extracted new features:
  - `year_added`
  - `month_added`
  - `month_name`
  - `duration_min`
  - `season_count`
- Converted appropriate columns to numeric types.

---

## 📊 Key Questions Answered

### ✅ General Insights

- How many TV Shows and Movies are available?
- What is the average movie duration?
- Which country produces the most content?

### ✅ Genre/Category Analysis

- What are the **top 10 content categories**?
- How many **Horror Movies** and **TV Shows** exist?
- What are the **top 10 Horror Movies**?

### ✅ People-Based Insights

- What are all the **movies Tom Cruise** appeared in?

### ✅ Temporal Analysis

- Growth in content over the **years**
- Growth in content over the **months**

---

## 📈 Visualizations

- Bar plots showing content types and ratings
- Line plots tracking Netflix's content growth over time
- Count plots for categorical distributions
- Interactive bar chart for top categories using Plotly

---

## 🗃 Summary Statistics

- Descriptive stats for movie durations and season counts
- Longest movie available
- Top countries in both Movie and TV Show releases

---

## 🔍 Libraries Used

- `pandas`, `numpy` – data manipulation
- `matplotlib`, `seaborn`, `plotly` – visualizations
- `scikit-learn`, `imblearn` – preprocessing utilities

---

## 📂 Project Structure

