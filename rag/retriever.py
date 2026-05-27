

# def retrieve_model():
#     from langchain.tools import tool
#     from langchain_community.vectorstores import FAISS
#     from embeddings import embedding_model
#         # =========================================
#         # LOAD VECTOR STORE
#     # =========================================

#     vector_store = FAISS.load_local(
#         "faiss_schema_db",
#         embedding_model,
#         allow_dangerous_deserialization=True
#     )

#     # =========================================
#     # RETRIEVAL TOOL
#     # =========================================

#     @tool(response_format="content_and_artifact")
#     def retrieve_schema(query: str):
#         """
#         Retrieve relevant database schema information.
#         """

#         retrieved_docs = vector_store.similarity_search(
#             query,
#             k=2
#         )

#         serialized = "\n\n".join(
#             (
#                 f"Source: {doc.metadata}\n"
#                 f"Content: {doc.page_content}"
#             )
#             for doc in retrieved_docs
#         )

#         return serialized, retrieved_docs

#     # =========================================
#     # TEST QUERY
#     # =========================================

#     query = "Show me product wise sales"

#     result = retrieve_schema.invoke(query)

#     print("\n==============================")
#     print("RETRIEVED SCHEMA")
#     print("==============================")

#     print(result)
from langchain_community.vectorstores import FAISS

from rag.embeddings import embedding_model

# =========================================
# LOAD VECTOR STORE
# =========================================

embeddings = embedding_model()

vector_store = FAISS.load_local(

    "faiss_schema_db",

    embeddings,

    allow_dangerous_deserialization=True

)

# =========================================
# RETRIEVE RELEVANT CONTEXT
# =========================================

def retrieve_context(query):

    retrieved_docs = vector_store.similarity_search(

        query,

        k=5

    )

    context = "\n\n".join(

        [

            doc.page_content

            for doc in retrieved_docs

        ]

    )

    return context
