# 🏎️ F1 Strategy & Race Data Analysis Dashboard

> Turning Formula 1 race data into strategic insights through data analysis and visualization.

---

## 📌 Overview

The **F1 Strategy & Race Data Analysis Dashboard** is a data-driven project that explores how Formula 1 race outcomes are influenced by strategy decisions such as pit stop timing, tyre selection, stint management, and track characteristics.

Instead of only presenting race statistics, this project focuses on **understanding the “why” behind race results** — how teams optimize performance using data in real-time race conditions.

This project simulates the kind of analysis performed by F1 race engineers and strategy teams during Grand Prix weekends.

---

## 🎯 Objective

Formula 1 is one of the most data-intensive sports in the world. Every decision — from pit stops to tyre selection — is influenced by data.

This project aims to:

- Analyze historical F1 race data to identify winning strategies
- Understand the impact of pit stop timing on race position changes
- Study tyre compound behavior across different circuits
- Analyze lap time degradation across stints
- Compare driver consistency and performance patterns
- Build an interactive dashboard for race strategy exploration

---

## 🧠 Key Insights & Findings

### 1. 🛞 Pit Stops Define Race Outcomes
Strategic pit stop timing (undercut vs overcut) has a major impact on track position. Even a 1–2 lap difference can change race results significantly.

---

### 2. 🔥 Tyre Strategy is Circuit Dependent
- Soft tyres = high performance, high degradation  
- Medium tyres = balanced performance  
- Hard tyres = stable but slower pace  

Each circuit demands a unique tyre strategy based on temperature, surface, and track layout.

---

### 3. 📉 Lap Time Degradation is Predictable
Lap times increase consistently after a certain number of laps in a stint due to tyre wear. Teams use this pattern to decide optimal pit windows.

---

### 4. 🧩 Consistency Beats Peak Performance
Drivers with stable lap times often outperform those with inconsistent high-speed laps, highlighting the importance of race rhythm over raw pace.

---

### 5. 🏁 Strategy is Not Universal
There is no “one-size-fits-all” race strategy. Each Grand Prix requires tailored decision-making based on:
- Track layout  
- Weather conditions  
- Tyre degradation rate  
- Safety car probability  

---

## 🛠️ Tech Stack

### Programming & Analysis
- Python 🐍
- Pandas
- NumPy

### Visualization
- Matplotlib
- Plotly
- PowerBI


### Data Sources
- FastF1 API 
- F1 historical race datasets

---

## 📊 Features of the Dashboard

- 📈 Lap time trend analysis per driver
- 🛞 Tyre compound performance comparison
- ⛽ Pit stop strategy visualization
- 📉 Stint-wise performance degradation charts
- 🏎️ Driver consistency scoring
- 🧠 Race strategy breakdown by circuit
- 📍 Position change tracking throughout race

---

## 🧪 Project Workflow

### 1. Data Collection
Race data is collected from F1 datasets / APIs including:
- Lap times
- Tyre compounds
- Race results

---

### 2. Data Cleaning
- Handling missing lap data
- Standardizing driver and team names
- Converting timestamps and lap formats

---

### 3. Feature Engineering
New metrics are created such as:
- Stint length
- Lap time delta
- Tyre degradation rate
- Position gain/loss per stint

---

### 4. Exploratory Data Analysis (EDA)
Patterns are identified in:
- Race strategy effectiveness
- Tyre performance curves
- Driver consistency trends

---

### 5. Visualization
Interactive and static plots are used to represent:
- Race strategy evolution
- Performance comparisons
- Stint analysis
- Tyre degradation trends
---

## 📷 Dashboards
<img width="508" height="314" alt="image" src="https://github.com/user-attachments/assets/ebbc0c73-97f6-4e78-98c6-5c7637355365" />
<img width="605" height="288" alt="image" src="https://github.com/user-attachments/assets/eccf2c9e-1f13-4bb7-8f3c-f38452e06b6b" />
<img width="447" height="272" alt="image" src="https://github.com/user-attachments/assets/14b3567e-20d6-4fac-a897-3a2471dc75c1" />
<img width="519" height="276" alt="image" src="https://github.com/user-attachments/assets/640e1abd-a16c-4f95-b8f5-605b708f2759" />
<img width="960" height="541" alt="image" src="https://github.com/user-attachments/assets/580333ca-3bab-48ad-81df-b07dfddc1315" />

---

## 🚀 How to Run This Project

```bash
# Clone repository
git clone https://github.com/saakshi2401/f1-strategy-dashboard.git

# Move into project folder
cd f1-strategy-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the dashboard (if Streamlit is used)
streamlit run app.py
