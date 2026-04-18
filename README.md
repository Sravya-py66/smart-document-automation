# 🚀 Smart Document Automation System

> AI-powered document classification and routing system for colleges

---

## 📌 Overview

The Smart Document Automation System is a web-based application that automatically processes uploaded documents, classifies them into categories, and routes them to the correct department folders.

It uses **Machine Learning (ML)** and **Natural Language Processing (NLP)** to reduce manual effort and improve efficiency.

---

## 🎯 Objectives

- Automate document classification
- Reduce manual sorting
- Improve processing speed
- Apply AI to real-world workflows

---

## ⚡ Key Features

- 📂 Upload PDF documents  
- 🔍 Automatic text extraction (PyPDF2)  
- 🤖 ML-based classification  
- 🚫 Spam detection (rule-based)  
- 📁 Automatic routing to folders  

### 📊 Categories

- 🧑‍💼 HR  
- 💰 Finance  
- 🎓 Academic  
- ⚖️ Legal  
- 🚫 Spam  

---

## 🧠 System Flow
Upload Document
↓
Extract Text (PyPDF2)
↓
Check Spam (Keywords)
↓
ML Classification (TF-IDF + Naive Bayes)
↓
Route to Folder


---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| ML | Scikit-learn |
| Model | Multinomial Naive Bayes |
| Feature | TF-IDF |
| PDF | PyPDF2 |

---

## ⚙️ How It Works

1. Upload PDF  
2. Extract text  
3. Detect spam  
4. If spam → Spam folder  
5. Else → ML classification  
6. Route file  

---

## 📂 Project Structure
document_automation_system/

main.py
generate_model.py
model.pkl
vectorizer.pkl

storage/
HR/
Finance/
Academic/
Legal/
Spam/


---

## 📊 Model Details

- Type: Supervised Learning  
- Algorithm: Multinomial Naive Bayes  
- Input: Text  
- Output: Category  

### Hybrid Approach
- Rule-based → Spam detection  
- ML → Document classification  

---

## 🧪 Example Output

- File: prize_win_contest.pdf  
- Category: Spam  
- Status: Routed successfully  

---

## ⚠️ Limitations

- Cannot read scanned PDFs (no OCR)
- Depends on training data quality
- Spam detection is basic

---

## 🔮 Future Improvements

- OCR support  
- Email routing  
- Cloud deployment  
- Login system  
- Confidence score  

---

## 📌 Conclusion

This project shows how AI can automate document workflows in colleges and organizations.

---
