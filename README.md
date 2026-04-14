# nassau-candy-distributor-Project-

# 🚚 Logistics Efficiency Dashboard (Nassau Candy Distribution)

## 📌 Overview
This project analyzes logistics and shipping data to evaluate delivery performance and identify inefficiencies. An interactive dashboard is built using Streamlit to provide insights into route efficiency, delays, and bottlenecks.

---

## ❗ Problem Statement
The organization lacked visibility into logistics performance, specifically:
- Efficient vs inefficient delivery routes  
- Regions causing frequent delivery delays  
- Impact of shipping modes on delivery time  
- Overall delivery trends  

This project solves these problems using data analysis and visualization.

---

## 🎯 Objectives
- Clean and preprocess raw logistics data  
- Calculate delivery time and identify delays  
- Analyze route efficiency (State → Region)  
- Detect bottlenecks across regions  
- Build an interactive dashboard  

---

## 🗂️ Dataset Description
The dataset includes:
- Order ID, Customer ID  
- Order Date, Ship Date  
- Shipping Mode  
- Country/Region, State/Province, City  
- Product details  
- Sales, Units, Gross Profit Cost  

---

## 🧹 Data Preprocessing
- Converted date columns into datetime format  
- Handled missing/invalid values  
- Cleaned column names (removed spaces & inconsistencies)  
- Prepared dataset for analysis  

---

## ⚙️ Feature Engineering
- **Delivery Time** = Ship Date - Order Date  
- **Delay Status** (Delayed / On-Time)  
- **Route** = State/Province → Region  

---

## 📊 Dashboard Features

### 🔹 KPI Metrics
- Total Orders  
- Average Delivery Time  
- Delayed Orders Count  

### 🔹 Visualizations
- 📍 Route Efficiency (Fastest & Slowest Routes)  
- 🚚 Shipping Mode Performance  
- 🚨 Bottleneck Analysis (Region-wise delays)  
- ⏱️ Delay Distribution  
- 📅 Monthly Delivery Trends  

### 🔹 Interactivity
- Filters by Region, State, and Shipping Mode  
- Dynamic charts  
- Data preview & download  

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- Streamlit  
- OpenPyXL  

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/tanya-sippy/nassau-logistics-dashboard.git
