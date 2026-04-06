"""
Run this script once to generate model.pkl and vectorizer.pkl.
These files are required by main.py to classify documents.

Usage:
    python generate_model.py
"""
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

CATEGORIES = ["HR", "Finance", "Academic", "Legal"]

training_samples = [
    ("employee recruitment onboarding performance review salary benefits payroll leave policy", "HR"),
    ("job description hiring manager interview candidate resume department training", "HR"),
    ("performance appraisal employee handbook workplace conduct attendance termination", "HR"),
    ("benefits compensation insurance pension retirement human resources staffing", "HR"),
    ("workforce planning talent acquisition succession planning grievance procedure", "HR"),
    ("revenue profit loss balance sheet income statement cash flow budget forecast", "Finance"),
    ("quarterly earnings financial report tax audit accounts payable receivable invoice", "Finance"),
    ("investment portfolio return on investment roi capital expenditure depreciation", "Finance"),
    ("financial statement net income expenses operating costs profit margin fiscal year", "Finance"),
    ("treasury bonds interest rate currency exchange rate dividend shareholder equity", "Finance"),
    ("research methodology hypothesis experiment data analysis statistical results", "Academic"),
    ("literature review abstract introduction conclusion references bibliography thesis", "Academic"),
    ("university study course syllabus examination grade academic paper journal", "Academic"),
    ("peer review scientific publication findings survey questionnaire sample population", "Academic"),
    ("dissertation faculty professor student curriculum lecture assignment semester", "Academic"),
    ("contract agreement terms conditions liability warranty indemnification clause", "Legal"),
    ("court judgment ruling plaintiff defendant attorney litigation arbitration appeal", "Legal"),
    ("intellectual property copyright trademark patent license intellectual rights", "Legal"),
    ("legal opinion statute regulation compliance jurisdiction due diligence", "Legal"),
    ("affidavit deposition subpoena injunction motion brief counsel attorney", "Legal"),
]

texts = [t for t, _ in training_samples]
labels = [l for _, l in training_samples]

vectorizer = TfidfVectorizer(max_features=500, stop_words="english")
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X, labels)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl and vectorizer.pkl have been created successfully.")
print(f"Model classes: {model.classes_}")
print(f"Vectorizer vocabulary size: {len(vectorizer.vocabulary_)}")
