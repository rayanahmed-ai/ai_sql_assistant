

# # def sql_generator():
# #     from dotenv import load_dotenv
# #     import os

# #     from langchain_google_genai import ChatGoogleGenerativeAI

# #     from langchain_community.utilities import SQLDatabase
# #     import pandas as pd

# #     # =========================================
# #     # LOAD ENV VARIABLES
# #     # =========================================

# #     load_dotenv()

# #     # =========================================
# #     # INITIALIZE GEMINI MODEL
# #     # =========================================

# #     model = ChatGoogleGenerativeAI(
# #         model="gemini-2.5-flash-lite",
# #         temperature=0,
# #         api_key=os.getenv("API_KEY")
# #     )

# #     # =========================================
# #     # CONNECT TO SQL SERVER
# #     # =========================================

# #     db = SQLDatabase.from_uri(

# #         "mssql+pyodbc://@LAPTOP-7RQS376A/SalesDB"
# #         "?driver=ODBC+Driver+17+for+SQL+Server"
# #         "&trusted_connection=yes"
# #         "&TrustServerCertificate=yes"
# #     )

# #     # =========================================
# #     # DATABASE INFO
# #     # =========================================

# #     print("\n==============================")
# #     print("DATABASE INFO")
# #     print("==============================")

# #     print(f"\nDialect: {db.dialect}")

# #     tables = db.get_usable_table_names()

# #     print(f"\nAvailable Tables:")
# #     print(tables)

# #     # =========================================
# #     # GET DATABASE SCHEMA
# #     # =========================================

# #     schema = db.get_table_info()

# #     print("\n==============================")
# #     print("SCHEMA")
# #     print("==============================")

# #     print(schema)

# #     # =========================================
# #     # USER QUESTION
# #     # =========================================

# #     question = "Show monthly product wise sales for 2025"

# #     # =========================================
# #     # CREATE PROMPT
# #     # =========================================

# #     prompt = f"""
# #     You are an expert SQL Server query generator.

# #     Database Dialect:
# #     {db.dialect}

# #     Database Schema:
# #     {schema}

# #     User Question:
# #     {question}

# #     STRICT RULES:

# #     - Generate ONLY SQL Server syntax
# #     - NEVER use SQLite syntax
# #     - NEVER use MySQL syntax
# #     - NEVER use PostgreSQL syntax

# #     USE:
# #     - YEAR()
# #     - MONTH()
# #     - DATENAME()
# #     - TOP

# #     DO NOT USE:
# #     - STRFTIME
# #     - LIMIT
# #     - AUTOINCREMENT

# #     DATABASE RULES:

# #     - ONLY generate SELECT queries
# #     - NEVER use INSERT
# #     - NEVER use UPDATE
# #     - NEVER use DELETE
# #     - NEVER use DROP

# #     IMPORTANT:

# #     Return ONLY the SQL query.
# #     Do NOT explain anything.
# #     Do NOT return markdown.
# #     Do NOT use ```sql
# #     """

# #     # =========================================
# #     # GENERATE SQL
# #     # =========================================

# #     response = model.invoke(prompt)

# #     generated_sql = response.content.strip()

# #     # =========================================
# #     # CLEAN SQL OUTPUT
# #     # =========================================

# #     generated_sql = generated_sql.replace("```sql", "")
# #     generated_sql = generated_sql.replace("```", "")

# #     generated_sql = generated_sql.strip()

# #     # =========================================
# #     # DISPLAY GENERATED SQL
# #     # =========================================

# #     print("\n==============================")
# #     print("GENERATED SQL")
# #     print("==============================")

# #     print(generated_sql)

# #     # # =========================================
# #     # # EXECUTE SQL
# #     # # =========================================

# #     # # try:

# #     # #     # result = db.run(generated_sql)

# #     # #     # print("\n==============================")
# #     # #     # print("QUERY RESULT")
# #     # #     # print("==============================")

# #     # #     # print(result)
# #     # #     import pandas as pd

# #     # # =========================================
# #     # # EXECUTE SQL
# #     # # =========================================
# #     # try:

# #     #     # Execute query
# #     #     result = db.run(generated_sql)

# #     #     # =====================================
# #     #     # CONVERT RESULT TO DATAFRAME
# #     #     # =====================================

# #     #     df = pd.read_sql(

# #     #         generated_sql,

# #     #         db._engine

# #     #     )

# #     #     print("\n==============================")
# #     #     print("QUERY RESULT")
# #     #     print("==============================")

# #     #     print(df)

# #     #     # =====================================
# #     #     # EXPORT CSV
# #     #     # =====================================

# #     #     df.to_csv(

# #     #         "query_result.csv",

# #     #         index=False

# #     #     )

# #     #     print("\nCSV Exported Successfully!")

# #     # except Exception as e:

# #     #     print("\n==============================")
# #     #     print("EXECUTION ERROR")
# #     #     print("==============================")

# #     #     print(e)
# from dotenv import load_dotenv
# import os

# from langchain_google_genai import ChatGoogleGenerativeAI

# # =========================================
# # LOAD ENV
# # =========================================

# load_dotenv()

# # =========================================
# # LOAD MODEL
# # =========================================

# model = ChatGoogleGenerativeAI(

#     model="gemini-2.5-flash-lite",

#     temperature=0,

#     api_key=os.getenv("API_KEY")

# )

# # =========================================
# # GENERATE SQL
# # =========================================

# def generate_sql(

#     question,

#     schema,

#     rag_context=""

# ):
#     from dotenv import load_dotenv
#     import os

#     from langchain_google_genai import ChatGoogleGenerativeAI

#     # =========================================
#     # LOAD ENV
#     # =========================================

#     load_dotenv()

#     # =========================================
#     # LOAD MODEL
#     # =========================================

#     model = ChatGoogleGenerativeAI(

#         model="gemini-2.5-flash-lite",

#         temperature=0,

#         api_key=os.getenv("API_KEY"))


#     prompt = f"""
#     You are an expert SQL Server query generator.

#     Database Schema:
#     {schema}

#     Business Context:
#     {rag_context}

#     User Question:
#     {question}

#     STRICT RULES:

#     - Generate ONLY SQL Server syntax
#     - NEVER use SQLite syntax
#     - NEVER use MySQL syntax
#     - NEVER use PostgreSQL syntax

#     USE:
#     - YEAR()
#     - MONTH()
#     - DATENAME()
#     - TOP

#     DO NOT USE:
#     - STRFTIME
#     - LIMIT
#     - AUTOINCREMENT

#     DATABASE RULES:

#     - ONLY generate SELECT queries
#     - NEVER use INSERT
#     - NEVER use UPDATE
#     - NEVER use DELETE
#     - NEVER use DROP

#     IMPORTANT:

#     Return ONLY SQL query.
#     No markdown.
#     No explanation.
#     """

#     response = model.invoke(prompt)

#     sql_query = response.content.strip()

#     # =========================================
#     # CLEAN OUTPUT
#     # =========================================

#     sql_query = sql_query.replace(

#         "```sql",

#         ""

#     )

#     sql_query = sql_query.replace(

#         "```",

#         ""

#     )

#     sql_query = sql_query.strip()

#     return sql_query
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# INITIALIZE GEMINI MODEL ONCE
# =========================================

model = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash-lite",

    temperature=0,

    api_key=os.getenv("API_KEY")

)

# =========================================
# GENERATE SQL
# =========================================

def generate_sql(

    question,

    schema,

    rag_context=""

):

    prompt = f"""
    You are an expert SQL Server query generator.

    Database Schema:
    {schema}

    Business Context:
    {rag_context}

    User Question:
    {question}

    STRICT RULES:

    - Generate ONLY SQL Server syntax
    - NEVER use SQLite syntax
    - NEVER use MySQL syntax
    - NEVER use PostgreSQL syntax

    USE:
    - YEAR()
    - MONTH()
    - DATENAME()
    - TOP

    DO NOT USE:
    - STRFTIME
    - LIMIT
    - AUTOINCREMENT

    DATABASE RULES:

    - ONLY generate SELECT queries
    - NEVER use INSERT
    - NEVER use UPDATE
    - NEVER use DELETE
    - NEVER use DROP

    SQL SERVER RULES:

    - If ORDER BY uses a column,
      that column MUST exist in:
        1. SELECT
        2. GROUP BY

    IMPORTANT:

    Return ONLY SQL query.
    No markdown.
    No explanation.
    """

    # =========================================
    # GENERATE RESPONSE
    # =========================================

    response = model.invoke(

        prompt

    )

    sql_query = response.content.strip()

    # =========================================
    # CLEAN SQL OUTPUT
    # =========================================

    sql_query = sql_query.replace(

        "```sql",

        ""

    )

    sql_query = sql_query.replace(

        "```",

        ""

    )

    sql_query = sql_query.strip()

    return sql_query