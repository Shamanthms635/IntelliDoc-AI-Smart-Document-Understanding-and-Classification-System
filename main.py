import os
from pathlib import Path
from datetime import datetime
from docx import Document
import pickle
import pdfplumber

document_data = []

def scan_documents(folder_path):
    print(f"\n📁 Scanning documents in: {folder_path}\n")
    files = os.listdir(folder_path)
    for file in files:
        file_path = Path(folder_path) / file
        if file_path.is_file():
            if file_path.suffix == ".txt":
                extract_text_from_txt(file_path)
            elif file_path.suffix == ".pdf":
                extract_text_from_pdf(file_path)
            elif file_path.suffix == ".docx":
                extract_text_from_docx(file_path)

# ✅ Extract text from .txt
def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            label = input(f"🏷️ Enter label for {file_path.name} (e.g., resume/invoice/article): ")
            document_data.append((text, label.strip().lower()))
    except Exception as e:
        print(f"❌ Could not read {file_path.name}: {e}")

# ✅ Extract text from .pdf
def extract_text_from_pdf(file_path):
    try:
        text = ""
        with pdfplumber.open(str(file_path)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        if text.strip():
            label = input(f"🏷️ Enter label for {file_path.name} (e.g., resume/invoice/article): ")
            document_data.append((text, label.strip().lower()))
        else:
            print(f"⚠️ No readable text found in {file_path.name}")
    except Exception as e:
        print(f"❌ Could not read {file_path.name}: {e}")

# ✅ Extract text from .docx
def extract_text_from_docx(file_path):
    try:
        doc = Document(str(file_path))
        text = "\n".join([para.text for para in doc.paragraphs])
        label = input(f"🏷️ Enter label for {file_path.name} (e.g., resume/invoice/article): ")
        document_data.append((text, label.strip().lower()))
    except Exception as e:
        print(f"❌ Could not read {file_path.name}: {e}")

# Run
if __name__ == "__main__":
    scan_documents("documents")

if document_data:
    with open("document_data.pkl", "wb") as f:
        pickle.dump(document_data, f)
    print(f"\n✅ Document data saved to document_data.pkl")
else:
    print("\n⚠️ No document data to save.")
