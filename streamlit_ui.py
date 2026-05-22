# # # import streamlit as st
# # # import pandas as pd

# # # from graph.workflow import graph

# # # # =========================================
# # # # PAGE CONFIG
# # # # =========================================

# # # st.set_page_config(

# # #     page_title="AI SQL Assistant",

# # #     page_icon="🤖",

# # #     layout="wide"

# # # )

# # # # =========================================
# # # # CUSTOM CSS
# # # # =========================================

# # # st.markdown(
# # #     """
# # #     <style>

# # #     .main {
# # #         padding-top: 2rem;
# # #     }

# # #     .stTextInput > div > div > input {
# # #         font-size: 18px;
# # #     }

# # #     .title {
# # #         font-size: 42px;
# # #         font-weight: bold;
# # #         color: #4F46E5;
# # #     }

# # #     .subtitle {
# # #         font-size: 18px;
# # #         color: gray;
# # #         margin-bottom: 30px;
# # #     }

# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True
# # # )

# # # # =========================================
# # # # HEADER
# # # # =========================================

# # # st.markdown(

# # #     '<div class="title">🤖 AI SQL Assistant</div>',

# # #     unsafe_allow_html=True

# # # )

# # # st.markdown(

# # #     '<div class="subtitle">'
# # #     'Ask questions in natural language and '
# # #     'generate SQL Server reports instantly.'
# # #     '</div>',

# # #     unsafe_allow_html=True

# # # )

# # # # =========================================
# # # # USER INPUT
# # # # =========================================

# # # question = st.text_input(

# # #     "Enter your question:",

# # #     placeholder="Example: Show monthly product wise sales for 2025"

# # # )

# # # # =========================================
# # # # RUN BUTTON
# # # # =========================================

# # # if st.button("Generate Report"):

# # #     if question.strip() == "":

# # #         st.warning("Please enter a question.")

# # #     else:

# # #         with st.spinner("Generating SQL and fetching results..."):

# # #             try:

# # #                 # =====================================
# # #                 # RUN LANGGRAPH WORKFLOW
# # #                 # =====================================

# # #                 response = graph.invoke(

# # #                     {

# # #                         "question": question

# # #                     }

# # #                 )

# # #                 # =====================================
# # #                 # DISPLAY CLEANED QUERY
# # #                 # =====================================

# # #                 st.subheader("🧠 Processed Query")

# # #                 st.code(

# # #                     response["cleaned_query"],

# # #                     language="text"

# # #                 )

# # #                 # =====================================
# # #                 # DISPLAY RAG CONTEXT
# # #                 # =====================================

# # #                 st.subheader("📚 Retrieved Context")

# # #                 st.info(

# # #                     response["rag_context"]

# # #                 )

# # #                 # =====================================
# # #                 # DISPLAY GENERATED SQL
# # #                 # =====================================

# # #                 st.subheader("🛢 Generated SQL")

# # #                 st.code(

# # #                     response["generated_sql"],

# # #                     language="sql"

# # #                 )

# # #                 # =====================================
# # #                 # VALIDATION STATUS
# # #                 # =====================================

# # #                 st.subheader("✅ Validation")

# # #                 if response["is_valid"]:

# # #                     st.success(

# # #                         response["validation_reason"]

# # #                     )

# # #                 else:

# # #                     st.error(

# # #                         response["validation_reason"]

# # #                     )

# # #                 # =====================================
# # #                 # DISPLAY QUERY RESULT
# # #                 # =====================================

# # #                 st.subheader("📊 Query Results")

# # #                 result = response["query_result"]

# # #                 # =====================================
# # #                 # HANDLE DATAFRAME
# # #                 # =====================================

# # #                 if isinstance(result, pd.DataFrame):

# # #                     st.dataframe(

# # #                         result,

# # #                         use_container_width=True,

# # #                         hide_index=True

# # #                     )

# # #                     # =================================
# # #                     # METRICS
# # #                     # =================================

# # #                     col1, col2, col3 = st.columns(3)

# # #                     with col1:

# # #                         st.metric(

# # #                             "Rows",

# # #                             len(result)

# # #                         )

# # #                     with col2:

# # #                         st.metric(

# # #                             "Columns",

# # #                             len(result.columns)

# # #                         )

# # #                     with col3:

# # #                         if "MonthlySales" in result.columns:

# # #                             st.metric(

# # #                                 "Total Sales",

# # #                                 f"{result['MonthlySales'].sum():,.0f}"

# # #                             )

# # #                     # =================================
# # #                     # DOWNLOAD BUTTON
# # #                     # =================================

# # #                     csv = result.to_csv(

# # #                         index=False

# # #                     ).encode("utf-8")

# # #                     st.download_button(

# # #                         label="⬇ Download CSV",

# # #                         data=csv,

# # #                         file_name="query_result.csv",

# # #                         mime="text/csv"

# # #                     )

# # #                     # =================================
# # #                     # OPTIONAL CHART
# # #                     # =================================

# # #                     if (

# # #                         "ProductName" in result.columns

# # #                         and "MonthlySales" in result.columns

# # #                     ):

# # #                         st.subheader("📈 Sales Visualization")

# # #                         chart_df = (

# # #                             result.groupby(

# # #                                 "ProductName"

# # #                             )["MonthlySales"]

# # #                             .sum()

# # #                             .reset_index()

# # #                         )

# # #                         st.bar_chart(

# # #                             chart_df.set_index(

# # #                                 "ProductName"

# # #                             )

# # #                         )

# # #                 else:

# # #                     st.error(result)

# # #                 # =====================================
# # #                 # EXPORT PATH
# # #                 # =====================================

# # #                 st.subheader("📁 Export Status")

# # #                 st.success(

# # #                     f"CSV saved successfully: "
# # #                     f"{response['export_path']}"

# # #                 )

# # #             except Exception as e:

# # #                 st.error(

# # #                     f"Application Error: {e}"

# # #                 )
# # import streamlit as st
# # import pandas as pd

# # from graph.workflow import graph

# # # =========================================
# # # PAGE CONFIG
# # # =========================================

# # st.set_page_config(

# #     page_title="AI SQL Assistant",

# #     page_icon="🤖",

# #     layout="wide"

# # )

# # # =========================================
# # # CUSTOM CSS
# # # =========================================

# # st.markdown(
# #     """
# #     <style>

# #     .main {
# #         padding-top: 2rem;
# #     }

# #     .stTextInput > div > div > input {
# #         font-size: 18px;
# #     }

# #     .title {
# #         font-size: 42px;
# #         font-weight: bold;
# #         color: #4F46E5;
# #     }

# #     .subtitle {
# #         font-size: 18px;
# #         color: gray;
# #         margin-bottom: 30px;
# #     }

# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# # # =========================================
# # # HEADER
# # # =========================================

# # st.markdown(

# #     '<div class="title">🤖 AI SQL Assistant</div>',

# #     unsafe_allow_html=True

# # )

# # st.markdown(

# #     '<div class="subtitle">'
# #     'Ask questions in natural language and '
# #     'generate SQL Server reports instantly.'
# #     '</div>',

# #     unsafe_allow_html=True

# # )

# # # =========================================
# # # SIDEBAR
# # # =========================================

# # with st.sidebar:

# #     st.title("⚡ Features")

# #     st.write("✅ LangGraph Workflow")
# #     st.write("✅ Gemini SQL Generation")
# #     st.write("✅ Azure SQL Database")
# #     st.write("✅ RAG Retrieval")
# #     st.write("✅ CSV Export")
# #     st.write("✅ Query Validation")

# #     st.divider()

# #     st.subheader("💡 Sample Queries")

# #     st.code(

# #         "Show monthly product wise sales for 2025"

# #     )

# #     st.code(

# #         "List all customer names"

# #     )

# #     st.code(

# #         "Show top selling products"

# #     )

# #     st.code(

# #         "Show customer wise revenue"

# #     )

# # # =========================================
# # # USER INPUT
# # # =========================================

# # question = st.text_input(

# #     "Enter your question:",

# #     placeholder="Example: Show monthly product wise sales for 2025"

# # )

# # # =========================================
# # # RUN BUTTON
# # # =========================================

# # if st.button("Generate Report"):

# #     if question.strip() == "":

# #         st.warning("Please enter a question.")

# #     else:

# #         with st.spinner("Generating SQL and fetching results..."):

# #             try:

# #                 # =====================================
# #                 # RUN LANGGRAPH WORKFLOW
# #                 # =====================================

# #                 response = graph.invoke(

# #                     {

# #                         "question": question

# #                     }

# #                 )

# #                 # =====================================
# #                 # CLARIFICATION HANDLING
# #                 # =====================================

# #                 if response["needs_clarification"]:

# #                     st.warning(

# #                         response["clarification_question"]

# #                     )

# #                     st.stop()

# #                 # =====================================
# #                 # DISPLAY CLEANED QUERY
# #                 # =====================================

# #                 st.subheader("🧠 Processed Query")

# #                 st.code(

# #                     response["cleaned_query"],

# #                     language="text"

# #                 )

# #                 # =====================================
# #                 # DISPLAY RAG CONTEXT
# #                 # =====================================

# #                 with st.expander("📚 Retrieved Context"):

# #                     st.write(

# #                         response["rag_context"]

# #                     )

# #                 # =====================================
# #                 # DISPLAY GENERATED SQL
# #                 # =====================================

# #                 st.subheader("🛢 Generated SQL")

# #                 st.code(

# #                     response["generated_sql"].strip(),

# #                     language="sql"

# #                 )

# #                 # =====================================
# #                 # VALIDATION STATUS
# #                 # =====================================

# #                 st.subheader("✅ Validation")

# #                 if response["is_valid"]:

# #                     st.success(

# #                         response["validation_reason"]

# #                     )

# #                 else:

# #                     st.error(

# #                         response["validation_reason"]

# #                     )

# #                 # =====================================
# #                 # DISPLAY QUERY RESULT
# #                 # =====================================

# #                 st.subheader("📊 Query Results")

# #                 result = response["query_result"]

# #                 # =====================================
# #                 # HANDLE DATAFRAME
# #                 # =====================================

# #                 if isinstance(result, pd.DataFrame):

# #                     if result.empty:

# #                         st.warning(

# #                             "No records found."

# #                         )

# #                     else:

# #                         st.dataframe(

# #                             result,

# #                             use_container_width=True,

# #                             hide_index=True

# #                         )

# #                         # =================================
# #                         # METRICS
# #                         # =================================

# #                         col1, col2, col3 = st.columns(3)

# #                         with col1:

# #                             st.metric(

# #                                 "Rows",

# #                                 len(result)

# #                             )

# #                         with col2:

# #                             st.metric(

# #                                 "Columns",

# #                                 len(result.columns)

# #                             )

# #                         with col3:

# #                             numeric_cols = result.select_dtypes(

# #                                 include="number"

# #                             ).columns

# #                             if len(numeric_cols) > 0:

# #                                 total_value = (

# #                                     result[numeric_cols[0]]

# #                                     .sum()

# #                                 )

# #                                 st.metric(

# #                                     "Total",

# #                                     f"{total_value:,.0f}"

# #                                 )

# #                         # =================================
# #                         # DOWNLOAD BUTTON
# #                         # =================================

# #                         csv = result.to_csv(

# #                             index=False

# #                         ).encode("utf-8")

# #                         st.download_button(

# #                             label="⬇ Download CSV",

# #                             data=csv,

# #                             file_name="query_result.csv",

# #                             mime="text/csv"

# #                         )

# #                         # =================================
# #                         # AUTO VISUALIZATION
# #                         # =================================

# #                         numeric_columns = result.select_dtypes(

# #                             include="number"

# #                         ).columns

# #                         text_columns = result.select_dtypes(

# #                             include="object"

# #                         ).columns

# #                         if (

# #                             len(numeric_columns) > 0

# #                             and len(text_columns) > 0

# #                         ):

# #                             st.subheader(

# #                                 "📈 Visualization"

# #                             )

# #                             chart_df = result.groupby(

# #                                 text_columns[0]

# #                             )[numeric_columns[0]].sum()

# #                             st.bar_chart(chart_df)

# #                 else:

# #                     st.error(result)

# #                 # =====================================
# #                 # EXPORT STATUS
# #                 # =====================================

# #                 st.subheader("📁 Export Status")

# #                 if response["export_path"]:

# #                     st.success(

# #                         f"CSV saved successfully: "

# #                         f"{response['export_path']}"

# #                     )

# #             except Exception as e:

# #                 st.error(

# #                     f"Application Error: {e}"

# #                 )
# import streamlit as st
# import pandas as pd

# from graph.workflow import graph

# # =========================================
# # PAGE CONFIG
# # =========================================

# st.set_page_config(

#     page_title="AI SQL Assistant",

#     page_icon="🤖",

#     layout="wide"

# )

# # =========================================
# # SESSION STATE
# # =========================================

# if "clarification_mode" not in st.session_state:

#     st.session_state.clarification_mode = False

# if "original_question" not in st.session_state:

#     st.session_state.original_question = ""

# if "clarification_question" not in st.session_state:

#     st.session_state.clarification_question = ""

# if "response" not in st.session_state:

#     st.session_state.response = None

# # =========================================
# # CUSTOM CSS
# # =========================================

# st.markdown(
#     """
#     <style>

#     .main {
#         padding-top: 2rem;
#     }

#     .stTextInput > div > div > input {
#         font-size: 18px;
#     }

#     .title {
#         font-size: 42px;
#         font-weight: bold;
#         color: #4F46E5;
#     }

#     .subtitle {
#         font-size: 18px;
#         color: gray;
#         margin-bottom: 30px;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # =========================================
# # HEADER
# # =========================================

# st.markdown(

#     '<div class="title">🤖 AI SQL Assistant</div>',

#     unsafe_allow_html=True

# )

# st.markdown(

#     '<div class="subtitle">'
#     'Ask questions in natural language and '
#     'generate SQL Server reports instantly.'
#     '</div>',

#     unsafe_allow_html=True

# )

# # =========================================
# # SIDEBAR
# # =========================================

# with st.sidebar:

#     st.title("⚡ Features")

#     st.write("✅ LangGraph Workflow")
#     st.write("✅ Gemini SQL Generation")
#     st.write("✅ Azure SQL Database")
#     st.write("✅ RAG Retrieval")
#     st.write("✅ CSV Export")
#     st.write("✅ Query Validation")
#     st.write("✅ Conversational Clarification")

#     st.divider()

#     st.subheader("💡 Sample Queries")

#     st.code(

#         "Show monthly product wise sales"

#     )

#     st.code(

#         "List customers who purchased more than 50000 last year"

#     )

#     st.code(

#         "Show employee wise order count"

#     )

#     st.code(

#         "Show regional sales"

#     )

# # =========================================
# # USER INPUT
# # =========================================

# question = st.text_input(

#     "Enter your question:",

#     placeholder="Example: Show monthly product wise sales"

# )

# # =========================================
# # GENERATE REPORT
# # =========================================

# if st.button("Generate Report"):

#     if question.strip() == "":

#         st.warning("Please enter a question.")

#     else:

#         with st.spinner(

#             "Generating SQL and fetching results..."

#         ):

#             try:

#                 response = graph.invoke(

#                     {

#                         "question": question,

#                         "needs_clarification": False,

#                         "clarification_question": ""

#                     }

#                 )

#                 # =================================
#                 # HANDLE CLARIFICATION
#                 # =================================

#                 if response.get(

#                     "needs_clarification",

#                     False

#                 ):

#                     st.session_state.clarification_mode = True

#                     st.session_state.original_question = question

#                     st.session_state.clarification_question = (

#                         response["clarification_question"]

#                     )

#                 else:

#                     st.session_state.response = response

#                     st.session_state.clarification_mode = False

#             except Exception as e:

#                 st.error(

#                     f"Application Error: {e}"

#                 )

# # =========================================
# # CLARIFICATION INPUT
# # =========================================

# if st.session_state.clarification_mode:

#     st.warning(

#         st.session_state.clarification_question

#     )

#     clarification_answer = st.text_input(

#         "Your clarification answer:"

#     )

#     if st.button("Submit Clarification"):

#         final_question = (

#             st.session_state.original_question

#             + " "

#             + clarification_answer

#         )

#         with st.spinner(

#             "Generating final report..."

#         ):

#             try:

#                 response = graph.invoke(

#                     {

#                         "question": final_question,

#                         "needs_clarification": False,

#                         "clarification_question": ""

#                     }

#                 )

#                 st.session_state.response = response

#                 st.session_state.clarification_mode = False

#             except Exception as e:

#                 st.error(

#                     f"Application Error: {e}"

#                 )

# # =========================================
# # DISPLAY RESPONSE
# # =========================================

# if st.session_state.response:

#     response = st.session_state.response

#     # =====================================
#     # DISPLAY CLEANED QUERY
#     # =====================================

#     st.subheader("🧠 Processed Query")

#     st.code(

#         response["cleaned_query"],

#         language="text"

#     )

#     # =====================================
#     # DISPLAY RAG CONTEXT
#     # =====================================

#     with st.expander("📚 Retrieved Context"):

#         st.write(

#             response["rag_context"]

#         )

#     # =====================================
#     # DISPLAY GENERATED SQL
#     # =====================================

#     st.subheader("🛢 Generated SQL")

#     st.code(

#         response["generated_sql"].strip(),

#         language="sql"

#     )

#     # =====================================
#     # VALIDATION STATUS
#     # =====================================

#     st.subheader("✅ Validation")

#     if response["is_valid"]:

#         st.success(

#             response["validation_reason"]

#         )

#     else:

#         st.error(

#             response["validation_reason"]

#         )

#     # =====================================
#     # DISPLAY QUERY RESULT
#     # =====================================

#     st.subheader("📊 Query Results")

#     result = response["query_result"]

#     # =====================================
#     # HANDLE DATAFRAME
#     # =====================================

#     if isinstance(result, pd.DataFrame):

#         if result.empty:

#             st.warning(

#                 "No records found."

#             )

#         else:

#             st.dataframe(

#                 result,

#                 use_container_width=True,

#                 hide_index=True

#             )

#             # =================================
#             # METRICS
#             # =================================

#             col1, col2, col3 = st.columns(3)

#             with col1:

#                 st.metric(

#                     "Rows",

#                     len(result)

#                 )

#             with col2:

#                 st.metric(

#                     "Columns",

#                     len(result.columns)

#                 )

#             with col3:

#                 numeric_cols = result.select_dtypes(

#                     include="number"

#                 ).columns

#                 if len(numeric_cols) > 0:

#                     total_value = (

#                         result[numeric_cols[0]]

#                         .sum()

#                     )

#                     st.metric(

#                         "Total",

#                         f"{total_value:,.0f}"

#                     )

#             # =================================
#             # DOWNLOAD BUTTON
#             # =================================

#             csv = result.to_csv(

#                 index=False

#             ).encode("utf-8")

#             st.download_button(

#                 label="⬇ Download CSV",

#                 data=csv,

#                 file_name="query_result.csv",

#                 mime="text/csv"

#             )

#             # =================================
#             # AUTO VISUALIZATION
#             # =================================

#             numeric_columns = result.select_dtypes(

#                 include="number"

#             ).columns

#             text_columns = result.select_dtypes(

#                 include="object"

#             ).columns

#             if (

#                 len(numeric_columns) > 0

#                 and len(text_columns) > 0

#             ):

#                 st.subheader(

#                     "📈 Visualization"

#                 )

#                 chart_df = result.groupby(

#                     text_columns[0]

#                 )[numeric_columns[0]].sum()

#                 st.bar_chart(chart_df)

#     else:

#         st.error(result)

#     # =====================================
#     # EXPORT STATUS
#     # =====================================

#     st.subheader("📁 Export Status")

#     if response["export_path"]:

#         st.success(

#             f"CSV saved successfully: "

#             f"{response['export_path']}"

#         )
import streamlit as st
import pandas as pd

from graph.workflow import graph

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="AI SQL Assistant",

    page_icon="🤖",

    layout="wide"

)

# =========================================
# SESSION STATE
# =========================================

if "clarification_mode" not in st.session_state:

    st.session_state.clarification_mode = False

if "original_question" not in st.session_state:

    st.session_state.original_question = ""

if "clarification_question" not in st.session_state:

    st.session_state.clarification_question = ""

if "response" not in st.session_state:

    st.session_state.response = None

# =========================================
# CUSTOM CSS
# =========================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .stTextInput > div > div > input {
        font-size: 18px;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #4F46E5;
    }

    .subtitle {
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================
# HEADER
# =========================================

st.markdown(

    '<div class="title">🤖 AI SQL Assistant</div>',

    unsafe_allow_html=True

)

st.markdown(

    '<div class="subtitle">'
    'Ask questions in natural language and '
    'generate SQL Server reports instantly.'
    '</div>',

    unsafe_allow_html=True

)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("⚡ Features")

    st.write("✅ LangGraph Workflow")
    st.write("✅ Gemini SQL Generation")
    st.write("✅ Azure SQL Database")
    st.write("✅ RAG Retrieval")
    st.write("✅ CSV Export")
    st.write("✅ Query Validation")
    st.write("✅ Conversational Clarification")

    st.divider()

    st.subheader("💡 Sample Queries")

    st.code(

        "Show monthly product wise sales"

    )

    st.code(

        "List customers who purchased more than 50000 last year"

    )

    st.code(

        "Show employee wise order count"

    )

    st.code(

        "Show regional sales"

    )

# =========================================
# USER INPUT
# =========================================

question = st.text_input(

    "Enter your question:",

    placeholder="Example: Show monthly product wise sales"

)

# =========================================
# GENERATE REPORT
# =========================================

if st.button("Generate Report"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner(

            "Generating SQL and fetching results..."

        ):

            try:

                response = graph.invoke(

                    {

                        "question": question,

                        "needs_clarification": False,

                        "clarification_question": ""

                    }

                )

                # =================================
                # HANDLE CLARIFICATION
                # =================================

                if response.get(

                    "needs_clarification",

                    False

                ):

                    st.session_state.clarification_mode = True

                    st.session_state.original_question = question

                    st.session_state.clarification_question = (

                        response.get(

                            "clarification_question",

                            ""

                        )

                    )

                    st.session_state.response = None

                else:

                    st.session_state.response = response

                    st.session_state.clarification_mode = False

            except Exception as e:

                st.error(

                    f"Application Error: {e}"

                )

# =========================================
# CLARIFICATION INPUT
# =========================================

if st.session_state.clarification_mode:

    st.warning(

        st.session_state.clarification_question

    )

    clarification_answer = st.text_input(

        "Your clarification answer:"

    )

    if st.button("Submit Clarification"):

        final_question = (

            st.session_state.original_question

            + " "

            + clarification_answer

        )

        with st.spinner(

            "Generating final report..."

        ):

            try:

                response = graph.invoke(

                    {

                        "question": final_question,

                        "needs_clarification": False,

                        "clarification_question": ""

                    }

                )

                st.session_state.response = response

                st.session_state.clarification_mode = False

            except Exception as e:

                st.error(

                    f"Application Error: {e}"

                )

# =========================================
# DISPLAY RESPONSE
# =========================================

if st.session_state.response:

    response = st.session_state.response

    # =====================================
    # DISPLAY CLEANED QUERY
    # =====================================

    if response.get("cleaned_query"):

        st.subheader("🧠 Processed Query")

        st.code(

            response.get(

                "cleaned_query",

                ""

            ),

            language="text"

        )

    # =====================================
    # DISPLAY RAG CONTEXT
    # =====================================

    if response.get("rag_context"):

        with st.expander("📚 Retrieved Context"):

            st.write(

                response.get(

                    "rag_context",

                    ""

                )

            )

    # =====================================
    # DISPLAY GENERATED SQL
    # =====================================

    if response.get("generated_sql"):

        st.subheader("🛢 Generated SQL")

        st.code(

            response.get(

                "generated_sql",

                ""

            ).strip(),

            language="sql"

        )

    # =====================================
    # VALIDATION STATUS
    # =====================================

    if "is_valid" in response:

        st.subheader("✅ Validation")

        if response.get(

            "is_valid",

            False

        ):

            st.success(

                response.get(

                    "validation_reason",

                    ""

                )

            )

        else:

            st.error(

                response.get(

                    "validation_reason",

                    ""

                )

            )

    # =====================================
    # DISPLAY QUERY RESULT
    # =====================================

    if "query_result" in response:

        st.subheader("📊 Query Results")

        result = response.get(

            "query_result",

            ""

        )

        # =================================
        # HANDLE DATAFRAME
        # =================================

        if isinstance(result, pd.DataFrame):

            if result.empty:

                st.warning(

                    "No records found."

                )

            else:

                st.dataframe(

                    result,

                    use_container_width=True,

                    hide_index=True

                )

                # =========================
                # METRICS
                # =========================

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(

                        "Rows",

                        len(result)

                    )

                with col2:

                    st.metric(

                        "Columns",

                        len(result.columns)

                    )

                with col3:

                    numeric_cols = (

                        result.select_dtypes(

                            include="number"

                        ).columns

                    )

                    if len(numeric_cols) > 0:

                        total_value = (

                            result[numeric_cols[0]]

                            .sum()

                        )

                        st.metric(

                            "Total",

                            f"{total_value:,.0f}"

                        )

                # =========================
                # DOWNLOAD BUTTON
                # =========================

                csv = result.to_csv(

                    index=False

                ).encode("utf-8")

                st.download_button(

                    label="⬇ Download CSV",

                    data=csv,

                    file_name="query_result.csv",

                    mime="text/csv"

                )

                # =========================
                # AUTO VISUALIZATION
                # =========================

                numeric_columns = (

                    result.select_dtypes(

                        include="number"

                    ).columns

                )

                text_columns = (

                    result.select_dtypes(

                        include="object"

                    ).columns

                )

                if (

                    len(numeric_columns) > 0

                    and len(text_columns) > 0

                ):

                    st.subheader(

                        "📈 Visualization"

                    )

                    chart_df = result.groupby(

                        text_columns[0]

                    )[numeric_columns[0]].sum()

                    st.bar_chart(chart_df)

        else:

            if result:

                st.error(result)

    # =====================================
    # EXPORT STATUS
    # =====================================

    if response.get("export_path"):

        st.subheader("📁 Export Status")

        st.success(

            f"CSV saved successfully: "

            f"{response.get('export_path', '')}"

        )
