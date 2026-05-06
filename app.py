import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# 1. Load and Clean Data
# We use 'latin-1' encoding because many spam datasets have special characters
df = pd.read_csv('spam.csv', encoding='latin-1')
# Keep only the necessary columns (Label and Text)
df = df.iloc[:, [0, 1]] 
df.columns = ['label', 'text']

# 2. Vectorize (Turn text into numbers)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# 4. Create the User Interface
st.title("📧 Email Spam Detector")
st.write("Type an email below to check if it's Spam or Not.")

user_input = st.text_area("Enter email text:")

if st.button("Predict"):
    if user_input:
        data = vectorizer.transform([user_input])
        prediction = model.predict(data)
        result = "SPAM" if prediction[0] == 'spam' else "NOT SPAM"
        st.subheader(f"Result: {result}")
    else:
        st.warning("Please enter some text.")


         
