# Smart Document Automation System

## Overview
This project is a web-based system that automatically classifies and routes documents into different departments using machine learning.

## Features
- Upload PDF documents
- Extract text automatically
- Classify into:
  - HR
  - Finance
  - Academic
  - Legal
- Automatically move files to respective folders

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- PyPDF2

## How It Works
1. Upload document  
2. Extract text  
3. Convert text to features  
4. Predict category  
5. Move file to correct folder  

## Run the Project
```bash
streamlit run main.py