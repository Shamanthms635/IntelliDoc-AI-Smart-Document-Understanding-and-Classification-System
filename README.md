# 🧠 Smart Document Classifier

A Python-based intelligent system that scans documents (`.pdf`, `.docx`, `.txt`), extracts metadata, summarizes the content using a pre-trained transformer model, and classifies the document (e.g., **resume**, **invoice**, **article**) using a machine learning model — all through a clean, interactive GUI.

---

## 📁 Features

- ✅ Upload a **file** or **entire folder** of documents
- 📋 View **file metadata**: name, size, last modified
- 📝 Get **automatic summaries** using Hugging Face’s DistilBART
- 🧠 Predict **document type** using a trained Naive Bayes model
- 🖼️ Clean and attractive **GUI interface**
- 📦 Built with `Tkinter`, `scikit-learn`, `transformers`, `pdfplumber`, and more

---

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/smart-document-classifier.git
   cd smart-document-classifier
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download model files (done automatically)**  
   The summarizer (`distilbart-cnn-12-6`) will be downloaded automatically on first run.

---

## 🚀 How to Run

### 🛠️ Step 1: Label Training Data

```bash
python main.py
```

### 🧠 Step 2: Train the Model

```bash
python model_train.py
```

### 🧾 Step 3: Predict Using GUI

```bash
python gui_predict.py
```

---

## 🧱 Folder Structure

```
├── documents/
├── main.py
├── model_train.py
├── gui_predict.py
├── document_data.pkl
├── document_model.pkl
├── vectorizer.pkl
├── README.md
└── requirements.txt
```

---

## 📌 Requirements

- Python 3.7+
- Internet for first-time model download (Hugging Face)

---

## 🙌 Author

Built by Shamanth MS  
*Learning Python & ML by building projects from scratch*