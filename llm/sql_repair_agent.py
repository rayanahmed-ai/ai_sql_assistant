from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# GEMINI MODEL
# =========================================

repair_model = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash-lite",

    temperature=0,

    api_key=st.secret["REPAIR_API_KEY"]

)

# =========================================
# REPAIR SQL
# =========================================

def repair_sql(

    broken_sql,

    error_message,

    schema

):

    prompt = f"""
    You are an expert SQL Server debugger.

    DATABASE SCHEMA:
    {schema}

    BROKEN SQL:
    {broken_sql}

    SQL SERVER ERROR:
    {error_message}

    TASK:
    Fix the SQL query.

    RULES:
    - Return ONLY corrected SQL
    - Use SQL Server syntax
    - Preserve original intent
    """

    response = repair_model.invoke(

        prompt

    )

    fixed_sql = response.content.strip()

    fixed_sql = fixed_sql.replace(

        "```sql",

        ""

    )

    fixed_sql = fixed_sql.replace(

        "```",

        ""

    )

    return fixed_sql.strip()
