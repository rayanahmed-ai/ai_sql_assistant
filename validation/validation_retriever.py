from langchain_community.vectorstores import FAISS

from langchain_google_genai import (

    GoogleGenerativeAIEmbeddings

)

import os

from dotenv import load_dotenv

# =========================================
# LOAD ENV
# =========================================

load_dotenv()
import streamlit as st
# =========================================
# LOAD EMBEDDINGS
# =========================================

embeddings = GoogleGenerativeAIEmbeddings(

    model="models/gemini-embedding-001",

    google_api_key=st.secret["API_KEY"]

)

# =========================================
# LOAD VECTORSTORE
# =========================================

vectorstore = FAISS.load_local(

    "validation/validation_vectorstore",

    embeddings,

    allow_dangerous_deserialization=True

)

# =========================================
# RETRIEVE VALIDATION CONTEXT
# =========================================

def retrieve_validation_context(query):

    docs = vectorstore.similarity_search(

        query,

        k=3

    )

    return "\n".join(

        [

            doc.page_content

            for doc in docs

        ]

    )
