# 📊 Data Analyst Job Dataset - EDA & Preprocessing Pipeline

This project walks through an end-to-end **Exploratory Data Analysis (EDA)** and **Preprocessing** pipeline on a dataset containing job listings for Data Analyst roles. The goal is to clean, explore, extract features, and prepare the data for modeling.

---

## 🧠 Project Highlights

### 1. **Understanding the Data**
- Dropped unnecessary columns like `Unnamed: 0`
- Handled datatypes and extracted meaningful numerical values from:
  - `Salary Estimate` ➝ `min_salary_estimate`, `max_salary_estimate`
  - `Size` ➝ `min_size`, `max_size`
  - `Revenue` ➝ `min_revenue`, `max_revenue`
- Cleaned up missing values like `-1`, `Unknown`, and `?`
- Standardized company names

---

### 2. **Exploratory Data Analysis (EDA)**

#### 🟦 Univariate Analysis
- Histograms and Boxplots for numerical columns
- Pie charts and Countplots for categorical features

#### 🟨 Bivariate Analysis
- Scatter plots and Line plots (Num vs Num)
- Box, Violin, and Strip plots (Num vs Cat)
- Countplots and Barplots (Cat vs Cat)

#### 🟥 Multivariate Analysis
- Correlation Heatmap
- Pairplot for numerical features

---

### 3. **Feature Engineering**
- Extracted features using:
  - `.str` & `.dt` for string and datetime manipulation
  - Geo-location extraction using IP (optional extensions)
  - Text Vectorization with `CountVectorizer`, `TfidfVectorizer`
- Cleaned `user_agent` strings and IP addresses (if applicable)

---

### 4. **Preprocessing Pipeline**

#### ✅ Duplicates
- Removed duplicate rows

#### ✅ Missing Values
- Numerical: Imputed using `SimpleImputer(strategy='median')`
- Categorical: Imputed using `SimpleImputer(strategy='most_frequent')`

#### ✅ Outliers
- Handled skewed numerical features using `np.log1p()`
- Visualized via boxplots

#### ✅ Encoding
- Categorical Features:
  - Used `BinaryEncoder` for high-cardinality features
- Boolean Features:
  - Converted `Easy Apply` to binary `0/1`

#### ✅ Feature Scaling
- Applied `StandardScaler` to revenue & salary
- Applied `RobustScaler` to company size

#### ✅ Splitting
- Data split into `train` and `test` using `train_test_split`

---

### 📁 Output Files
- `train_cleaned_encoded.csv`: Cleaned & encoded training set
- `test_cleaned_encoded.csv`: Cleaned & encoded test set

---

## 🛠️ Tools & Libraries

| Category            | Tools / Libraries                                  |
|---------------------|----------------------------------------------------|
| Data Manipulation   | `pandas`, `numpy`                                  |
| Visualization       | `matplotlib`, `seaborn`, `plotly`                  |
| Feature Engineering | `user_agents`, `ip2geotools`, `geopy`, `sklearn`  |
| Preprocessing       | `SimpleImputer`, `KNNImputer`, `StandardScaler`   |
| Encoding            | `OrdinalEncoder`, `LabelEncoder`, `BinaryEncoder` |
| Balancing (Optional)| `SMOTE`, `RandomOverSampler` (from `imblearn`)    |

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/data-analyst-eda.git
   cd data-analyst-eda
