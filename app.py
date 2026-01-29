import streamlit as st
from transformers import pipeline

# Load summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# App UI
st.set_page_config(page_title="AI Article Summarizer", layout="centered")

st.title("🧠 AI Article Summarizer")
st.write("Paste your article below and get a short AI-generated summary.")

article_text = st.text_area("Enter Article Text", height=300)

if st.button("Summarize"):
    if article_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(
                article_text,
                max_length=150,
                min_length=40,
                do_sample=False
            )
            st.subheader("📌 Summary")
            st.success(summary[0]['summary_text'])

