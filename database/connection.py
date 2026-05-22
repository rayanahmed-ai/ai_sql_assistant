
# def get_db():
#     from sqlalchemy import create_engine
#     import pandas as pd

#     # =========================================
#     # SQL SERVER CONNECTION
#     # =========================================

#     server = "LAPTOP-7RQS376A"
#     database = "SalesDB"

#     connection_string = (
#         f"mssql+pyodbc://@{server}/{database}"
#         "?driver=ODBC+Driver+17+for+SQL+Server"
#         "&trusted_connection=yes"
#         "&TrustServerCertificate=yes"
#     )

#     # Create engine
#     # engine = create_engine(connection_string)

#     # # =========================================
#     # # TEST QUERY
#     # # =========================================

#     # query = "SELECT * FROM Sales"

#     # df = pd.read_sql(query, engine)

#     # print(df.head(100))
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# # =========================================
# # DATABASE CONNECTION
# # =========================================

# def get_db():

#     server = "LAPTOP-7RQS376A"

#     database = "SalesDB"

#     connection_string = (

#         f"mssql+pyodbc://@{server}/{database}"
#         "?driver=ODBC+Driver+17+for+SQL+Server"
#         "&trusted_connection=yes"
#         "&TrustServerCertificate=yes"

#     )

#     engine = create_engine(

#         connection_string

#     )

#     return engine
# from sqlalchemy import create_engine

# =========================================
# AZURE SQL CONNECTION
# =========================================
load_dotenv()
def get_db():
    
    server = "rayan.database.windows.net"

    database = "SalesDB"

    username = "CloudSA5818b0af"
    import streamlit as st

    password = st.secrets["azurepw"]

    # password = os.getenv("azurepw")

    connection_string = (

        f"mssql+pyodbc://"

        f"{username}:{password}"

        f"@{server}:1433/{database}"

        "?driver=ODBC+Driver+17+for+SQL+Server"

    )

    engine = create_engine(

        connection_string

    )

    return engine
