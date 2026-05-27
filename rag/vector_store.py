
from langchain_core.documents import Document

from langchain_text_splitters import (

    RecursiveCharacterTextSplitter

)

from langchain_community.vectorstores import FAISS

from rag.embeddings import embedding_model

# =========================================
# CREATE VECTOR STORE
# =========================================

def rag_generator():

    # =====================================
    # DATABASE SCHEMA + BUSINESS CONTEXT
    # =====================================

    schema_docs = [

        """
        Customers table stores customer information.

        Columns:
        CustomerID
        CustomerName
        Region
        """,

        """
        Products table stores product information.

        Columns:
        ProductID
        ProductName
        Category
        """,

        """
        Sales table stores sales transaction data.

        Columns:
        SaleID
        ProductID
        CustomerID
        Amount
        SaleDate
        """,

        """
        Product wise sales means:
        SUM(Amount)
        grouped by ProductName
        """,

        """
        Monthly sales means:
        GROUP BY YEAR(SaleDate)
        and MONTH(SaleDate)
        """,

        """
        Revenue means:
        SUM(Sales.Amount)
        """

    ]

    # =====================================
    # CONVERT TO DOCUMENTS
    # =====================================

    docs = [

        Document(

            page_content=doc,

            metadata={

                "source": "SQL Server Schema"

            }

        )

        for doc in schema_docs

    ]

    # =====================================
    # SPLIT DOCUMENTS
    # =====================================

    text_splitter = (

        RecursiveCharacterTextSplitter(

            chunk_size=500,

            chunk_overlap=50,

            add_start_index=True

        )

    )

    all_splits = text_splitter.split_documents(

        docs

    )

    print(

        f"\nTotal Chunks Created: "

        f"{len(all_splits)}"

    )

    # =====================================
    # LOAD EMBEDDINGS
    # =====================================

    embeddings = embedding_model()

    # =====================================
    # CREATE VECTOR STORE
    # =====================================

    vector_store = FAISS.from_documents(

        documents=all_splits,

        embedding=embeddings

    )

    # =====================================
    # SAVE VECTOR STORE
    # =====================================

    vector_store.save_local(

        "faiss_schema_db"

    )

    print(

        "\nVector Store Created Successfully!"

    )

    return vector_store
