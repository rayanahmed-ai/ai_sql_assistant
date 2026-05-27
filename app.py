# # import streamlit as st
# # import pandas as pd

# # # ====================================
# # # PAGE CONFIG
# # # ====================================
# # st.set_page_config(
# #     page_title="Natural Language SQL Assistant",
# #     page_icon="📊",
# #     layout="wide"
# # )

# # # ====================================
# # # TITLE
# # # ====================================
# # st.title("📊 Natural Language SQL Assistant")

# # st.markdown("""
# # Ask questions in plain English.

# # ### Example Queries
# # - Show product-wise sales
# # - Show region-wise sales for 2025
# # - List customers who purchased more than 50000 last year
# # """)

# # # ====================================
# # # USER INPUT
# # # ====================================
# # user_query = st.text_input(
# #     "Enter your request:",
# #     placeholder="Example: Show product-wise sales for 2025"
# # )

# # # ====================================
# # # BUTTON
# # # ====================================
# # generate_button = st.button("Generate Report")

# # # ====================================
# # # SAMPLE OUTPUT
# # # ====================================
# # if generate_button:

# #     if not user_query.strip():
# #         st.warning("Please enter a query.")

# #     else:
# #         st.success("Query received successfully!")

# #         # Example extracted data
# #         st.subheader("🧠 Extracted Information")

# #         extracted_data = {
# #             "intent": "sales_report",
# #             "group_by": "product",
# #             "year": "2025"
# #         }

# #         st.json(extracted_data)

# #         # Example SQL
# #         st.subheader("🛠 Generated SQL")

# #         sample_sql = """
# #         SELECT
# #             ProductName,
# #             SUM(Amount) AS TotalSales
# #         FROM Sales
# #         GROUP BY ProductName
# #         """

# #         st.code(sample_sql, language="sql")

# #         # Example dataframe
# #         st.subheader("📋 Query Results")

# #         data = {
# #             "ProductName": ["Laptop", "Mouse", "Keyboard"],
# #             "TotalSales": [120000, 45000, 30000]
# #         }

# #         df = pd.DataFrame(data)

# #         st.dataframe(df, use_container_width=True)

# #         # ====================================
# #         # DOWNLOAD CSV
# #         # ====================================
# #         csv = df.to_csv(index=False).encode("utf-8")

# #         st.download_button(
# #             label="⬇ Download CSV",
# #             data=csv,
# #             file_name="report.csv",
# #             mime="text/csv"
# #         )

# # # ====================================
# # # SIDEBAR
# # # ====================================
# # st.sidebar.header("⚙ Features")

# # st.sidebar.markdown("""
# # - Natural Language Query
# # - SQL Generation
# # - SQL Server Integration
# # - CSV Export
# # - NLP Processing
# # - RAG Support
# # - LangGraph Workflow
# # """)
# from graph.workflow import graph

# response = graph.invoke(

#     {

#         "question":

#         "Show monthly product wise sales for 2025"

#     }

# )

# print("\n==============================")
# print("FINAL RESULT")
# print("==============================")

# print(response)
import google.generativeai as genai
import os
from dotenv import load_dotenv

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

genai.configure(

    api_key=os.getenv("API_KEY")

)

# =========================================
# LIST AVAILABLE MODELS
# =========================================

for model in genai.list_models():

    print(model.name)