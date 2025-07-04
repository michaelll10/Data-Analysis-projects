# ⚽ FIFA Player‑Stats EDA (Pandas)

This project explores a FIFA player statistics dataset using **Pandas** and basic NumPy operations.

## 📁 Files
- `fifa_eda.csv` – raw FIFA player data  
- `fifa_eda.ipynb` (or `.py`) – notebook / script with all analysis steps

## 🔍 Key Steps

1. **Data Cleaning**
   - Standardised column names (`lowercase`, `underscores`)
   - Converted `date` columns to `datetime`
   - Fixed dtypes (e.g.\ `Joined` as categorical/​object)

2. **Descriptive Statistics & Queries**
   - Players aged 45, tallest player, lightest player
   - Average age, max height, min weight
   - Positions of specific stars (e.g.\ Cristiano Ronaldo)

3. **Group‑by Insights**
   - Average market **value by joining year**
   - **Number of players per club**
   - Top 5 positions & nationalities
   - Egyptian players list
   - Count of players with names starting with **“M”**
   - Players who joined in 2018 & have 2 skill‑moves

4. **Correlation Check**
   - Pearson correlation between **International Reputation** and **Wage** (≈ 0.66 – strong positive)

## ✅ Tools Used
- Python 3.10+
- pandas
- numpy

## ✨ Key Insights
- Positive link (0.66) between international reputation and wage – higher‑profile players earn more.
- Clubs vary widely in squad size; certain clubs dominate player counts.
- Majority of players cluster in a handful of positions and nationalities.
- Tallest and lightest extreme players identified for scouting curiosity.

---

**Author**: Michael Mamdouh  
**License**: MIT
