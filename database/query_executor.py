import pandas as pd

from database.connection import get_db

# =========================================
# EXECUTE SQL QUERY
# =========================================

def execute_query(sql_query):

    try:

        engine = get_db()

        df = pd.read_sql(

            sql_query,

            engine

        )

        return df

    except Exception as e:

        return f"Execution Error: {e}"