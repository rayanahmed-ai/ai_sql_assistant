
import os

from dotenv import load_dotenv

from langchain_google_genai import (

    GoogleGenerativeAIEmbeddings

)

# =========================================
# LOAD ENV VARIABLES
# =========================================
import streamlit as st

load_dotenv()

# =========================================
# CREATE EMBEDDING MODEL
# =========================================

def embedding_model():
    # api_key = st.getenv("API_KEY")
    api_key = st.secret["API_KEY"]
    embeddings = GoogleGenerativeAIEmbeddings(

        model="models/gemini-embedding-001",

        api_key=api_key

    )

    return embeddings
