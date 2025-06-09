# 🚀 Personal Finance Dashboard  

Welcome to the **Personal Finance Dashboard**! This project is an automated financial transaction retrieval and processing pipeline, integrating UnionBank’s API with PostgreSQL and Apache Airflow for efficient data orchestration. 📊  

UnionBank API Reference: https://developer.unionbankph.com/reference

## 📌 Project Overview  
This pipeline automates the retrieval, transformation, and storage of structured financial transaction data, ensuring accurate balance updates and insightful analytics. It provides:  

💰 **Transaction Table:** Tracks individual transactions, amounts, dates, and sources.  

## ✨ Features  
✅ Automated retrieval of financial transactions from UnionBank's API.  
✅ Real-time ETL processing to cleanse and structure transaction data.  
✅ Efficient database storage using PostgreSQL for analytical querying.  
✅ Workflow automation with Apache Airflow for scheduled data updates.  
✅ Visualization in Power BI for actionable financial insights.  

## 🛠 Technologies Used  
🐍 **Python** (Data processing & API interaction)  
🔗 **RESTful API** (UnionBank API for transaction retrieval)  
🗄 **PostgreSQL** (Database storage & querying)  
⚙️ **Apache Airflow** (Workflow scheduling & automation)  
📊 **Power BI** (Data visualization & financial analysis)  
🖥 **Linux** (System deployment & execution)  

## 📂 Database Schema  
```sql
CREATE TABLE transactions (
    transaction_id VARCHAR(10) PRIMARY KEY,
    transaction_type VARCHAR(6),
    amount NUMERIC(12,2),
    currency CHAR(3),
    transaction_date TIMESTAMP,
    remarks VARCHAR(300),
    balance NUMERIC(30,2),
    posted_date TIMESTAMP
);
```

---

## 👤 Author
Developed by **Cley**  
📧 Contact: 02clintaudrey@gmail.com 
🌐 GitHub: SecreShall

---
