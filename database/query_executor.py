# # import pandas as pd

# # from database.connection import get_db

# # # =========================================
# # # EXECUTE SQL QUERY
# # # =========================================

# # def execute_query(sql_query):

# #     try:

# #         engine = get_db()

# #         df = pd.read_sql(

# #             sql_query,

# #             engine

# #         )

# #         return df

# #     except Exception as e:

# #         return f"Execution Error: {e}"
# import pandas as pd

# from sqlalchemy import create_engine

# from llm.sql_repair_agent import repair_sql

# from validation.sql_validator import validate_sql

# import os

# # =========================================
# # DATABASE CONNECTION
# # =========================================

# connection_string = (

#     f"mssql+pyodbc://"

#     f"{os.getenv('AZURE_USER')}"

#     f":{os.getenv('AZURE_PASSWORD')}"

#     f"@{os.getenv('AZURE_SERVER')}"

#     f"/{os.getenv('AZURE_DATABASE')}"

#     f"?driver=ODBC+Driver+17+for+SQL+Server"

# )

# engine = create_engine(

#     connection_string

# )

# # =========================================
# # EXECUTE QUERY
# # =========================================

# def execute_query(

#     sql_query,

#     schema

# ):

#     # =====================================
#     # VALIDATE SQL
#     # =====================================

#     validation = validate_sql(

#         sql_query

#     )

#     if not validation["valid"]:

#         return validation["reason"]

#     # =====================================
#     # TRY EXECUTION
#     # =====================================

#     try:

#         df = pd.read_sql(

#             sql_query,

#             engine

#         )

#         return df

#     # =====================================
#     # REPAIR ON FAILURE
#     # =====================================

#     except Exception as e:

#         error_message = str(e)

#         try:

#             repaired_sql = repair_sql(

#                 broken_sql=sql_query,

#                 error_message=error_message,

#                 schema=schema

#             )

#             repaired_df = pd.read_sql(

#                 repaired_sql,

#                 engine

#             )

#             return repaired_df

#         except Exception as repair_error:

#             return (

#                 f"Execution Error:\n\n"

#                 f"{repair_error}"

#             )
import pandas as pd

from database.connection import get_db

from validation.sql_validator import validate_sql

from llm.sql_repair_agent import repair_sql

# =========================================
# EXECUTE SQL QUERY
# =========================================

def execute_query(

    sql_query,

    schema

):

    try:

        # =====================================
        # VALIDATE SQL
        # =====================================

        validation = validate_sql(

            sql_query

        )

        if not validation["valid"]:

            return (

                f"Validation Error: "

                f"{validation['reason']}"

            )

        # =====================================
        # GET DATABASE CONNECTION
        # =====================================

        engine = get_db()

        # =====================================
        # EXECUTE SQL
        # =====================================

        df = pd.read_sql(

            sql_query,

            engine

        )

        return df

    except Exception as e:

        # =====================================
        # ORIGINAL ERROR
        # =====================================

        error_message = str(e)

        try:

            # =================================
            # REPAIR SQL
            # =================================

            repaired_sql = repair_sql(

                broken_sql=sql_query,

                error_message=error_message,

                schema=schema

            )

            # =================================
            # EXECUTE REPAIRED SQL
            # =================================

            repaired_df = pd.read_sql(

                repaired_sql,

                engine

            )

            return repaired_df

        except Exception as repair_error:

            return (

                f"Execution Error: "

                f"{repair_error}"

            )