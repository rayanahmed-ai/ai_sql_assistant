from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# =========================================
# AZURE SQL CONNECTION
# =========================================
load_dotenv()
def get_db():
    
    server = "rayan.database.windows.net"

    database = "SalesDB2"

    username = "CloudSA5818b0af"
    import streamlit as st

    password = os.getenv("azurepw")

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
