
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
