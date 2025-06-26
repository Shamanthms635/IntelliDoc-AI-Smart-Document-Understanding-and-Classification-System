import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load saved document data
with open("document_data.pkl", "rb") as f:
    document_data = pickle.load(f)

# Split data into features and labels
text, labels = zip(*document_data)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(text, labels, test_size=0.2, random_state=42)

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Make predictions
predictions = model.predict(X_test_vec)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)
print("✅ Accuracy:", round(accuracy * 100, 2), "%")


# Save the trained model
with open("document_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save the vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("💾 Model and vectorizer saved successfully!")

