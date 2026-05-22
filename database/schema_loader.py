# def schema_loader():

#     from sqlalchemy import create_engine, inspect

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

#     engine = create_engine(connection_string)

#     # =========================================
#     # INSPECT DATABASE
#     # =========================================

#     inspector = inspect(engine)

#     # =========================================
#     # GET TABLES
#     # =========================================

#     tables = inspector.get_table_names()

#     print("\n==============================")
#     print("DATABASE TABLES")
#     print("==============================")

#     for table in tables:

#         print(f"\nTable: {table}")

#         columns = inspector.get_columns(table)

#         for column in columns:
#             print(f" - {column['name']} ({column['type']})")
from sqlalchemy import inspect

from database.connection import get_db

# =========================================
# LOAD DATABASE SCHEMA
# =========================================

def schema_loader():

    engine = get_db()

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    schema_info = ""

    for table in tables:

        schema_info += f"\nTable: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:

            schema_info += (

                f"- {column['name']} "
                f"({column['type']})\n"

            )

    return schema_info