# import os
# from dotenv import load_dotenv

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# def embedding_model():
#     import os
#     from dotenv import load_dotenv

#     from langchain_google_genai import GoogleGenerativeAIEmbeddings
#     # =========================================
#     # LOAD ENV VARIABLES
#     # =========================================

#     load_dotenv()
#     api_key=os.getenv("API_KEY")
#     # =========================================
#     # GOOGLE GEMINI EMBEDDINGS
#     # =========================================

#     embedding_model = GoogleGenerativeAIEmbeddings(
#         model="models/gemini-embedding-001",
#         api_key=api_key
#     )

#     # =========================================
#     # TEST EMBEDDINGS
#     # =========================================

#     vector = embedding_model.embed_query("What is the capital of France?")

#     print(f"Vector Dimension: {len(vector)}")
#     print("First 5 values:", vector[:5])

    # # =========================================
    # # SAVE TO FILE
    # # =========================================

    # import pickle

    # with open("embeddings.pkl", "wb") as f:
    #     pickle.dump(embedding_model, f)

    # print("✅ Embeddings saved to embeddings.pkl")
import os

from dotenv import load_dotenv

from langchain_google_genai import (

    GoogleGenerativeAIEmbeddings

)

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# CREATE EMBEDDING MODEL
# =========================================

def embedding_model():

    api_key = os.getenv(

        "API_KEY"

    )

    embeddings = GoogleGenerativeAIEmbeddings(

        model="models/gemini-embedding-001",

        api_key=api_key

    )

    return embeddings