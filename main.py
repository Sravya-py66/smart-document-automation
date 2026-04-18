import streamlit as st
import pickle
import os
import io

import PyPDF2


CATEGORIES = ["HR", "Finance", "Academic", "Legal", "Spam"]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_BASE = os.path.join(ROOT_DIR, "storage")
MODEL_PATH = os.path.join(ROOT_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(ROOT_DIR, "vectorizer.pkl")


def create_storage_folders():
    for category in CATEGORIES:
        os.makedirs(os.path.join(STORAGE_BASE, category), exist_ok=True)


def extract_text(uploaded_file):
    pdf_bytes = uploaded_file.read()
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

def predict_category(text, model, vectorizer):
    # Rule-based spam detection
    spam_keywords = ["offer", "click", "buy now", "free", "random", "unknown", "win", "prize"]

    text_lower = text.lower()

    if any(word in text_lower for word in spam_keywords):
        return "Spam"

    # ML classification
    features = vectorizer.transform([text])
    return model.predict(features)[0]

def route_file(uploaded_file, category):
    destination_folder = os.path.join(STORAGE_BASE, category)
    os.makedirs(destination_folder, exist_ok=True)
    import time
    filename = f"{int(time.time())}_{uploaded_file.name}"
    destination_path = os.path.join(destination_folder, filename)
    with open(destination_path, "wb") as f:
        f.write(uploaded_file.getvalue())
        return destination_path


def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer


def main():
    st.title("Smart Document Automation System")

    create_storage_folders()

    try:
        model, vectorizer = load_model()
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")
        return

    st.subheader("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            try:
                raw_text = extract_text(uploaded_file)
                uploaded_file.seek(0)

                if not raw_text:
                    st.error("Unable to process document. It may be a scanned file.")
                    return

                category = predict_category(raw_text, model, vectorizer)
                route_file(uploaded_file, category)

                st.subheader("Result")
                st.markdown(f"""
---
**File:** {uploaded_file.name}

**Category:** {category}
""")
                st.success(f"Successfully routed to {category} Department")
                st.markdown("---")

                with st.expander("Show Details"):
                    st.text_area("Extracted Text", value=raw_text[:2000], height=200, disabled=True)

            except Exception as e:
                st.error(f"An error occurred while processing the document: {str(e)}")


if __name__ == "__main__":
    main()
