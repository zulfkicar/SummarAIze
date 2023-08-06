import streamlit as st
from summarizer import Summarizer

st.set_page_config(
    page_title="Extractive Summarization"
    )
st.title('Extractive Text Summarization')
st.markdown('Using BERT')

#Initiate three columns for section to be side-by-side
col1, col2, col3 = st.columns(3)

with col1:
    _min_length = st.slider("Minimum Sentence Length", min_value=0.0, max_value=1024.0, value=40.0, step=1.0)

with col2:
    _max_length = st.slider("Maximum Sentence Length", min_value=0.0, max_value=1024.0, value=256.0, step=1.0)

with col3:
    _ratio = st.slider("Reduction Ratio", min_value=0.0, max_value=1.0, value=0.4, step=0.1)

#Provide the input area for text to be summarized
text = st.text_area("Enter the text you want to summarize:", height=200)

def run_model(input_text):
    model = Summarizer()
    result = model(input_text, min_length=_min_length,max_length=_max_length,ratio=_ratio)
    summary = ''.join(result)
    st.write('Summary')
    st.success(summary)

#Creating button for execute the text summarization
if st.button("Summarize"):
    run_model(text)