import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Load dataset (SMS Spam Collection CSV 'spam.csv')
def load_dataset(path="spam.csv"):
    # The dataset has columns: v1 (label), v2 (message)
    df = pd.read_csv(path, encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'message']
    return df

# Preprocess data
def preprocess_data(df):
    df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
    return df

# Vectorize text messages
def vectorize_messages(messages):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(messages)
    return X, vectorizer

# Train Naive Bayes Classifier
def train_model(X, y):
    model = MultinomialNB()
    model.fit(X, y)
    return model

# Predict new message
def predict_message(model, vectorizer, message):
    vec_msg = vectorizer.transform([message])
    pred = model.predict(vec_msg)[0]
    return "SPAM" if pred == 1 else "HAM"

# Main function
if __name__ == "__main__":
    print("Loading dataset...")
    df = load_dataset()
    df = preprocess_data(df)

    # Vectorize
    X, vectorizer = vectorize_messages(df['message'])
    y = df['label_num']

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))

    # Test with custom input
    sample = input("\nEnter a message to classify: ")
    print("Prediction:", predict_message(model, vectorizer, sample))
