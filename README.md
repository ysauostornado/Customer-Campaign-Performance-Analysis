# Customer Campaign Performance Analysis

Analyzing the effectiveness of marketing campaigns using customer demographics, transaction history, and offer engagement data.

---

## 🔍 Project Overview
This project investigates **which campaign offers drive the highest engagement and revenue** across different customer segments.  
By combining transaction, demographic, and campaign data, we identify **actionable recommendations** for optimizing marketing campaigns.

---

## 📂 Datasets
- `events.csv` – customer actions (transactions, offers received/viewed/completed)  
- `offers.csv` – metadata (offer type, duration, reward, difficulty)  
- `customers.csv` – demographics (age, gender, income, membership date)  
- `data/final_events_with_customers.csv` – cleaned & merged dataset (272K+ rows, 14,825 valid customers)

---

## 🛠️ Tools & Methods
- **Python (pandas, matplotlib, seaborn, numpy)** – data cleaning & analysis  
- **Excel** – quick cleaning & validation  
- **Tableau** (optional) – visualization  

**Data Cleaning**  
- Removed ~2,000 invalid customers (e.g., unrealistic ages, missing income/gender)  
- Merged events, offers, and customers datasets into one analysis-ready file  

**Analysis Focus**  
- Offer completion rates (Discount vs. BOGO, Gender differences)  
- Customer segmentation by age and income  
- Engagement trends over campaign timeline  

---

## 📈 Key Insights

### 💡 1. Age Group vs Income Group
The **30–44 age group with €50K–€100K income** completed the most offers, highlighting this segment as the most responsive.  

![Age vs Income](images/Age_Group_vs_Income_Group.png)

---

### 💡 2. Completions over Time
Engagement peaked during **Days 15–24**, after which completion rates declined sharply.  

![Completions Over Time](images/Completions_over_Time.png)

---

### 💡 3. Offer Completion by Gender
Both genders showed similar engagement levels, with only slight differences in completion trends.  

![Offer by Gender](images/Offer_Completion_by_Gender.png)

---

### 💡 4. Offer Completion Rate by Type
**Discount offers outperformed BOGO offers**, achieving a much higher completion rate.  

![Offer by Type](images/Offer_Completion_Rate_by_Type.png)

---

## 🎯 Recommendations
- Prioritize **discount offers** as the main promotional type  
- Target **30–44 age group with €50K–€100K income** for maximum ROI  
- Schedule **mid-campaign reminders** around Days 15–20 to maintain engagement  
- Continue improving **customer data quality** (gender/income completeness)  

---

## 📑 Deliverables
- 📄 [Final Presentation PDF](./presentation/Analytical%20Process%20-%20Arsenii%20Popenko.pdf)  
- 📊 Jupyter Notebook (coming soon) – `notebooks/campaign_analysis.ipynb`  
- 📂 Clean dataset – `data/final_events_with_customers.csv`

---

## 🚀 Outcome
This project demonstrates how **customer segmentation + campaign analytics** can drive **data-driven marketing strategies**.  
It highlights **real-world challenges** like data quality and shows how Python can be combined with business insights to create actionable recommendations.

---
