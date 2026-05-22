

# def export_to_csv():
#     from llm.sql_generator import generated_sql,db
#     import pandas as pd
#     try:

#         # Execute query
#         result = db.run(generated_sql)

#         # =====================================
#         # CONVERT RESULT TO DATAFRAME
#         # =====================================

#         df = pd.read_sql(

#             generated_sql,

#             db._engine

#         )
        
#         print("\n==============================")
#         print("QUERY RESULT")
#         print("==============================")

#         print(df)

#         # =====================================
#         # EXPORT CSV
#         # =====================================

#         df.to_csv(

#             "query_result.csv",

#             index=False

#         )

#         print("\nCSV Exported Successfully!")

#     except Exception as e:

#         print("\n==============================")
#         print("EXECUTION ERROR")
#         print("==============================")

#         print(e)
import pandas as pd

# =========================================
# EXPORT DATAFRAME TO CSV
# =========================================

def export_to_csv(df):

    try:

        # =====================================
        # EXPORT CSV
        # =====================================

        file_path = "query_result.csv"

        df.to_csv(

            file_path,

            index=False

        )

        print("\n==============================")
        print("CSV EXPORTED")
        print("==============================")

        print(f"\nSaved to: {file_path}")

        return file_path

    except Exception as e:

        print("\n==============================")
        print("EXPORT ERROR")
        print("==============================")

        print(e)

        return None