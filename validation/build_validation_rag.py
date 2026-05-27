from langchain_community.vectorstores import FAISS

from langchain_google_genai import (

    GoogleGenerativeAIEmbeddings

)

from validation.schema_metadata import (

    extract_metadata

)
import streamlit as st
import os

from dotenv import load_dotenv

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# LOAD EMBEDDINGS
# =========================================

embeddings = GoogleGenerativeAIEmbeddings(

    model="models/gemini-embedding-001",

    google_api_key=st.secrets["API_KEY2"]

)

# =========================================
# EXTRACT METADATA
# =========================================

metadata_docs = extract_metadata()

# =========================================
# BUILD VECTORSTORE
# =========================================

vectorstore = FAISS.from_texts(

    metadata_docs,

    embeddings

)

# =========================================
# SAVE VECTORSTORE
# =========================================

vectorstore.save_local(

    "validation/validation_vectorstore"

)

print(

    "Validation RAG built successfully."

)
