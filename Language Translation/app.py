import streamlit as st # a python program to build and share data apps
from transformers import pipeline 
#Transformers is a deep learning model that using a neural network architecture to trannsform one type of input into another type of output like chatbots.

st.set_page_config(
    page_title="Translator",
    page_icon=":robot:",
    layout="wide"
)

st.header("🌐 Language Translator 🌐")

# Language code lookup
languages = {
    "fr": "French",
    "en": "English",
    "es": "Spanish",
    "it": "Italian",
    "de": "German",
}

# Language options
source_lang, target_lang = st.columns(2)
with source_lang:
    src_lang_code = st.selectbox("Translate from", list(languages.keys()))

with target_lang:
    tgt_lang_code = st.selectbox("Translate to", list(languages.keys()))

# Model options
model_options = {
    "fr-en": "Helsinki-NLP/opus-mt-fr-en",
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",
    "es-en": "Helsinki-NLP/opus-mt-es-en",
    "en-es": "Helsinki-NLP/opus-mt-en-es",
    "it-en": "Helsinki-NLP/opus-mt-it-en",
    "en-it": "Helsinki-NLP/opus-mt-en-it",
    "en-de": "Helsinki-NLP/opus-mt-en-de",
    "de-en": "Helsinki-NLP/opus-mt-de-en",
}

model_key = f"{src_lang_code}-{tgt_lang_code}"
option_llm = model_options.get(model_key, "")

# User input
query = st.text_area(
    label=f"Your input text ({languages[src_lang_code]} to {languages[tgt_lang_code]})",
    placeholder="Enter text to translate",
    key="question_text"
)

# Translation and output
if st.button("Translate"):
    if query and len(query) > 1:
        try:
            with st.spinner(text="In progress..."):
                translator = pipeline("translation", model=option_llm)
                output = translator(query)[0]['translation_text']
            height = min(2 * len(output), 240)
            st.text_area(
                label="Translation",
                value=output,
                height=height
            )
        except Exception as e:
            st.error(f"Sorry: cannot translate! {e}")
