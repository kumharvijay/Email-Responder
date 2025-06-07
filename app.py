# app.py
!pip install textblob
!pip install pandas
!pip install nltk

import streamlit as st
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download once
nltk.download('vader_lexicon')

# App title and description
st.set_page_config(page_title="AI Email Sentiment Responder")
st.title("AI Email Sentiment Responder")
st.write("Enter an email message. This AI will detect sentiment and generate an appropriate auto-reply.")

# Input box
email_text = st.text_area("Enter your email message below:", height=200)

# Analyze function
def analyze_email(text):
    blob = TextBlob(text)
    sid = SentimentIntensityAnalyzer()
    compound_score = sid.polarity_scores(text)['compound']

    # Decide sentiment
    if compound_score >= 0.3:
        sentiment = "Positive"
        reply = "We're thrilled to hear that! Thank you for your kind feedback."
    elif compound_score <= -0.3:
        sentiment = "Negative"
        reply = "We're sorry for the inconvenience. Our team will follow up with you shortly."
    else:
        sentiment = "Neutral"
        reply = "Thank you for reaching out. We’ll get back to you with more information soon."

    return sentiment, reply

# Button to trigger analysis
if st.button("Analyze"):
    if email_text.strip() == "":
        st.warning("Please enter an email message first.")
    else:
        sentiment, auto_reply = analyze_email(email_text)
        st.markdown(f"**Sentiment Detected:** `{sentiment}`")
        st.markdown("**Auto-Generated Reply:**")
        st.success(auto_reply)
