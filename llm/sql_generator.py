from groq import Groq
from dotenv import load_dotenv

import os

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# GROQ CLIENT
# =========================================

client = Groq(

    api_key=os.getenv(

        "GROQ_API_KEY"

    )

)

# =========================================
# SQL GENERATOR
# =========================================

def generate_sql(

    question,

    schema,

    rag_context

):

    prompt = f"""

    You are an expert SQL Server query generator.

    =====================================
    DATABASE SCHEMA
    =====================================

    {schema}

    =====================================
    RAG CONTEXT
    =====================================

    {rag_context}

    =====================================
    USER REQUEST
    =====================================

    {question}

    =====================================
    YOUR JOB
    =====================================

    Generate a valid SQL Server query
    based on:

    - database schema
    - relationships
    - business meaning
    - RAG examples/context

    =====================================
    IMPORTANT RULES
    =====================================

    - Generate ONLY SQL

    - DO NOT explain anything

    - DO NOT use markdown

    - DO NOT generate invalid joins

    - ONLY use columns/tables
      present in the schema

    - Use proper SQL Server syntax

    - Use aliases when needed

    - Always generate readable SQL

    - If aggregation is used,
      ensure GROUP BY is correct

    - If ORDER BY uses a column,
      ensure it is either:
      - aggregated
      - grouped
      - selected properly

    =====================================
    SQL SERVER RULES
    =====================================

    - Use TOP instead of LIMIT

    - Use GETDATE() for current date

    - Use YEAR(), MONTH(),
      DATENAME() where needed

    - Use proper JOIN conditions

    =====================================
    AGGREGATION RULES
    =====================================

    If using:

    - SUM
    - COUNT
    - AVG
    - MAX
    - MIN

    then:

    ALL non-aggregated columns
    MUST be included in GROUP BY.

    =====================================
    OUTPUT FORMAT
    =====================================

    Return ONLY the SQL query.

    """

    # =====================================
    # GROQ RESPONSE
    # =====================================

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {

                "role": "user",

                "content": prompt

            }

        ],

        temperature=0

    )

    sql_query = (

        response.choices[0]

        .message.content

        .strip()

    )

    # =====================================
    # CLEAN SQL
    # =====================================

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