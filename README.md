# Sales Analytics ETL Pipeline

A complete end‑to‑end Sales Analytics ETL project built with Python and Pandas.  
This project transforms raw sales data into clean, structured, and insightful analytics tables, including profitability metrics, region performance, weekday trends, weekend analysis, shipping cost insights, and product‑level behaviour.

---

## Project Overview

This project demonstrates my ability to:

- Clean and preprocess raw CSV data  
- Engineer new features for deeper analysis  
- Build business‑ready analytics tables  
- Export insights as CSV files  
- Structure a real ETL workflow suitable for production or teaching  

It reflects practical data engineering and analytics skills used in real‑world environments.

---

## ETL Steps

### 1. Data Cleaning
- Convert date columns to datetime  
- Convert numeric fields to correct types  
- Drop unnecessary columns  
- Handle duplicates  
- Normalize text fields (e.g., payment method)  

### 2. Feature Engineering
- total_price  
- final_amount_paid  
- Date features: year, month, day, weekday  
- Weekend flag  
- Order size categories (Small, Medium, Large)  

### 3. Analytics & Insights
- Profitability metrics  
- Region‑level performance  
- Weekday vs weekend sales  
- Top products per order size  
- Highest shipping cost  
- Top product by shipping cost  
- Highest and lowest order days  
- Highest and lowest order months  

All analytics tables are exported as CSV files.

---

## Project Structure

sales-analytics-etl/
│
├── data/
│   └── raw_sales.csv
│
├── notebooks/
│   └── sales_etl_notebook.ipynb
│
├── scripts/
│   ├── clean.py
│   ├── transform.py
│   └── analytics.py
│
├── outputs/
│   ├── region_sales.csv
│   ├── orders_by_weekday.csv
│   ├── top_products_by_size.csv
│   ├── shipping_by_product.csv
│   └── highest_shipping_cost.csv
│
├── README.md
└── requirements.txt

---

## Key Insights Generated

- Regions with the highest and lowest sales  
- Weekday with the most and least orders  
- Weekend vs weekday revenue comparison  
- Top products for Small, Medium, and Large orders  
- Products with the highest shipping cost  
- Days and months with peak order activity  

These insights support reporting, forecasting, and business decision-making.

---

## Technologies Used

- Python  
- Pandas  
- Jupyter Notebook or Databricks  
- CSV data storage  
- Git and GitHub  

---

## How to Run the Project

1. Clone the repository  
2. Install dependencies using:
pip install -r requirements.txt
3. Run the ETL scripts or open the notebook  
4. View the generated CSV analytics in the `outputs/` folder  

---

## Purpose of This Project

This project showcases the ability to:

- Build structured ETL pipelines  
- Apply data engineering best practices  
- Perform business-driven analytics  
- Communicate insights clearly  
- Prepare data for dashboards and reporting  

It is designed as both a portfolio project and a teaching resource.




