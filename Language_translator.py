# Required libraries
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
import streamlit as st
from streamlit_extras.colored_header import colored_header
import json as js
import time
import pyaudio as audio


st.set_page_config(page_title='Language Translator By Praveen', layout="wide")


# Streamlit Process

class translator:

    def process(self):



        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
        col1 , col2 ,col3 = st.columns([6,10,3])
        col2.markdown("<h1 style='font-size: 60px;'><span style='color: white;'>Language</span> <span style='color: cyan;'>Translator</span> </h1>",unsafe_allow_html=True)
        col1, col2, col3 = st.columns([6, 10, 6])
        with col2:
            colored_header(
                label="",
                description="",
                color_name="blue-green-70"
            )
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col1, col2 = st.columns([10, 10])
        col1.markdown(
            "<h1 style='font-size: 30px;'><span style='color: white;'>Provide</span> <span style='color: cyan;'>Text</span> </h1>",
            unsafe_allow_html=True)
        col2.markdown(
            "<h1 style='font-size: 30px;'><span style='color: white;'>Select </span> <span style='color: cyan;'> Language</span> </h1>",
            unsafe_allow_html=True)

        col1, col2 = st.columns([10, 10])
        text = col1.text_input("      ")

        # Creation of translator object
        translator = Translator()

        languages = []  # Adding all languages and their code

        for code, name in LANGUAGES.items():
            languages.append({name: code})

        # Collecting Languages and their codes
        languages_name = [list(i.keys())[0] for i in languages]  # Collection of Languages Name
        lan_codes = [list(i.values())[0] for i in languages]  # Collection of Language codes

        selected_lan = col2.selectbox('', languages_name)

        x = languages_name.index(selected_lan)

        target_language = lan_codes[x]

        translated = translator.translate(text, dest=target_language)
        translated_text = translated.text

        col1, col2, col3 = st.columns([18, 10, 10])
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        if col2.button('Convert'):
            # Target Language

            with st.spinner('Converting...'):
                time.sleep(3)

            col3,col1, col2,col4 = st.columns([9,45, 20,10])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            # col2.write("")
            col1.write("")
            col1.write("")
            col1.write("")
            col1.write("")
            col1.write("")
            col1.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Provided Text : </span> <span style='color: white;'>{text}</span></h1>",
                unsafe_allow_html=True)

            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Converted Text : </span><span style='color: white;'>{translated_text}</span></h1>",
                unsafe_allow_html=True)
            colored_header(
                label="",
                description="",
                color_name="blue-green-70"
            )


# Object creation

object = translator()
object.process()