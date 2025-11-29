# Retail Data Analysis  
### *From Static Spreadsheets to Real-Time Insights*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)  
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B)  
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)

---

## What is this?

Most retail businesses drown in CSV files. They have the data, but they can’t see the **story** behind it.

**Global Retail Intelligence** is a full-stack data application that transforms raw transaction logs (50,000+ rows) into an interactive dashboard. Rather than manually creating pivot tables every week, stakeholders can use this tool to instantly filter sales data by region, category, and date range.

This project addresses the **"Data Latency"** problem—reducing the time from **"Data Generated"** to **"Decision Made"** from hours to seconds.

---

## Key Features

- **Real-Time KPIs**: Instantly calculates metrics such as Total Revenue, Average Order Value (AOV), and Profit Margins.
- **Interactive Filtering**: Filter sales data by Region, Month, or Product Category with no coding required.
- **Trend Analysis**: Automatically visualizes seasonality and sales spikes using dynamic line charts.
- **Auto-Cleaning Pipeline**: A built-in Pandas script that handles missing values and inconsistent date formats automatically.

---

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (Interactive Web UI)
- **Backend**: Python (Logic & Computation)
- **Data Processing**: Pandas & NumPy
- **Visualization**: Matplotlib & Streamlit Native Charts

---

## How to Run Locally

### 1. Clone the Repository
git clone https://github.com/Priyank-2005/Retail-Data-Analysis.git
cd Retail-Data-Analysis

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the App
streamlit run app.py

---

## Project Architecture

- **Ingestion**: Reads raw orders.csv data.
- **Processing**: Cleans currency symbols, handles null values, and parses dates.
- **Aggregation**: Groups data by Month/Year for trend analysis.
- **Display**: Renders interactive KPIs and charts via Streamlit.

---

## Created by

**Priyank Bohra** | Data Analyst & Python Developer
