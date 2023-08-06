import streamlit as st
from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

#define model maps
model_map={'Long T5':'pszemraj/long-t5-tglobal-base-16384-book-summary',
           'LED Base':'pszemraj/led-base-book-summary',
           'LED Long':'pszemraj/led-large-book-summary'
           }

#Set the application title
st.title("Abstractive Text Summarization")
st.markdown("Using Fine-Tuned BigBirdPegasus, T5 and LED models trained on the BookSum dataset")

#Select the model to be used for the summary
model = st.selectbox('Select the model', ('Long T5', 'LED Base', 'LED Long'))

#Initiate three columns for section to be side-by-side
col1, col2, col3 = st.columns(3)

#Slider to control the model hyperparameter
with col1:
    _min_length = st.slider("Minimum Length", min_value=0.0, max_value=1024.0, value=16.0, step=1.0)
    _max_length = st.slider("Maximum Length", min_value=0.0, max_value=1024.0, value=256.0, step=1.0)

#Selection box to select the summarization style
with col2:
    _num_beams = st.slider("Number of Beams", min_value=2.0, max_value=5.0, value=4.0, step=1.0)
    _repetition_penalty = st.slider("Repetition Penalty", min_value=-2.0, max_value=4.0, value=3.5, step=0.1)
#Showing the current parameter used for the model 
with col3:
    _no_repeat_ngram_size = st.slider("N-Gram Repeats", min_value=2.0, max_value=5.0, value=3.0, step=1.0)
    _encoder_no_repeat_ngram_size = st.slider("Encoder N-Gram Repeats", min_value=2.0, max_value=5.0, value=3.0, step=1.0)
        
#Provide the input area for text to be summarized
text = st.text_area("Enter the text you want to summarize:", height=200)

#write a run_model function that runs the program
def run_model(input_text):
    global model
    hf_name = model_map[model]
    #initialize the summarizer in pipeline
    if model == 'Long T5':
        summarizer = pipeline(
            "summarization",
            hf_name,
            device=0 if torch.cuda.is_available() else -1,
        )
        result = summarizer(
           input_text,
           min_length=int(_min_length), 
           max_length=int(_max_length),
           no_repeat_ngram_size=int(_no_repeat_ngram_size), 
           encoder_no_repeat_ngram_size=int(_encoder_no_repeat_ngram_size),
           repetition_penalty=_repetition_penalty,
           num_beams=int(_num_beams),
           do_sample=False,
           early_stopping=True
        )
        summary=result[0]['summary_text']
        st.write('Summary')
        st.success(summary)
    elif model == 'LED Base':
        summarizer = pipeline(
            "summarization",
            hf_name,
            device=0 if torch.cuda.is_available() else -1,
        )
        result = summarizer(
           input_text,
           min_length=int(_min_length), 
           max_length=int(_max_length),
           no_repeat_ngram_size=int(_no_repeat_ngram_size), 
           encoder_no_repeat_ngram_size=int(_encoder_no_repeat_ngram_size),
           repetition_penalty=_repetition_penalty,
           num_beams=int(_num_beams),
           do_sample=False,
           early_stopping=True
        )
        summary=result[0]['summary_text']
        st.write('Summary')
        st.success(summary)
    else:
        summarizer = pipeline(
            "summarization",
            hf_name,
            device=0 if torch.cuda.is_available() else -1,
        )
        result = summarizer(
           input_text,
           min_length=int(_min_length), 
           max_length=int(_max_length),
           no_repeat_ngram_size=int(_no_repeat_ngram_size), 
           encoder_no_repeat_ngram_size=int(_encoder_no_repeat_ngram_size),
           repetition_penalty=_repetition_penalty,
           num_beams=int(_num_beams),
           early_stopping=True
        )
        summary=result[0]['summary_text']
        st.write('Summary')
        st.success(summary)
    

#Creating button for execute the text summarization
if st.button("Summarize"):
    run_model(text)