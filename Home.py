import streamlit as st

st.set_page_config(
    page_title="Lecture Summarizer"
    )

st.title("Home")
st.markdown(""""The Lecture Summarizer Project is a Natural Language Processing (NLP) project that aims to summarize lectures automatically using various text summarization techniques. 

## Text Summarization Techniques

Text summarization techniques can be divided into three categories:

1. **Extractive**: This technique extracts the most important sentences or phrases from the original text to create a summary. It is widely used due to its simplicity and effectiveness.

2. **Abstractive**: This technique generates a summary by paraphrasing and rephrasing the original text. It is more challenging than extractive summarization, but it can generate summaries that are more concise and coherent.

3. **Descriptive**: This technique provides a description of the main topics and ideas discussed in the original text. It is less common than the other two techniques but can be useful for certain applications.

## Transformers

Transformers are a type of neural network architecture that has revolutionized NLP in recent years. Some popular transformer models used in text summarization are:

1. **T5**: T5 (Text-to-Text Transfer Transformer) is a transformer model that can perform a wide range of NLP tasks, including text summarization. It has achieved state-of-the-art performance in many NLP benchmarks.

2. **BERT**: BERT (Bidirectional Encoder Representations from Transformers) is another transformer model that has shown excellent results in various NLP tasks, including text summarization.

3. **Longformer Encoder-Decoder (LED)**: This is a transformer model that can handle long sequences of text, which is important for text summarization since it often involves processing large amounts of text.

## Relevant Information

The Lecture Summarizer Project can have various applications, such as helping students to study more efficiently, enabling researchers to scan through a large number of papers quickly, and assisting professionals to prepare for meetings and presentations. However, developing an accurate and reliable lecture summarizer is still a challenging task, and researchers are continuously working on improving the existing techniques and models.""")