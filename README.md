# 🚀 Smart Document Automation System

> Intelligent document classification and routing using Machine Learning

---

## 📌 Overview
This project is a web-based system that automatically classifies uploaded documents and routes them into the correct department folders.

It reduces manual work by using **Natural Language Processing (NLP)** and **Machine Learning**.

---

## ⚡ Features

✔ Upload PDF documents  
✔ Automatic text extraction  
✔ Smart classification using ML  
✔ Categories:
- 🧑‍💼 HR  
- 💰 Finance  
- 🎓 Academic  
- ⚖️ Legal  

✔ Automatic routing to folders  

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| ML Model | Multinomial Naive Bayes |
| Feature Extraction | TF-IDF |
| PDF Processing | PyPDF2 |

---

## ⚙️ How It Works

1. 📂 Upload document  
2. 🔍 Extract text  
3. 🔢 Convert text → TF-IDF vectors  
4. 🤖 Predict category  
5. 📁 Move file to correct folder  

---

## ▶️ Run Locally

```bash
pip install streamlit PyPDF2 scikit-learn
streamlit run main.py
