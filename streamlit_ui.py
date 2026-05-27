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
# # SESSION STATE
# # =========================================

# if "conversation_history" not in st.session_state:

#     st.session_state.conversation_history = []

# if "intent_state" not in st.session_state:

#     st.session_state.intent_state = {}

# if "awaiting_clarification" not in st.session_state:

#     st.session_state.awaiting_clarification = False

# if "latest_question" not in st.session_state:

#     st.session_state.latest_question = ""

# if "current_clarification_question" not in st.session_state:

#     st.session_state.current_clarification_question = ""

# # =========================================
# # USER INPUT
# # =========================================

# question = st.text_input(

#     "Enter your question:",

#     placeholder="Example: Show monthly product wise sales for 2025"

# )

# # =========================================
# # CLARIFICATION SECTION
# # =========================================

# if st.session_state.awaiting_clarification:

#     st.info(

#         f"{st.session_state.current_clarification_question}"

#     )

#     clarification_answer = st.text_input(

#         "Answer the clarification question"

#     )

#     if clarification_answer.strip() == "":

#         st.stop()

#     # =====================================
#     # SUBMIT CLARIFICATION
#     # =====================================

#     if st.button(

#         "Submit Clarification",

#         key="clarification_btn"

#     ):

#         with st.spinner(

#             "Refining your request..."

#         ):

#             try:

#                 # =============================
#                 # STORE USER ANSWER
#                 # =============================

#                 st.session_state.conversation_history.append(

#                     {

#                         "user":

#                         clarification_answer

#                     }

#                 )

#                 # =============================
#                 # BETTER QUERY MERGING
#                 # =============================

#                 merged_query = f"""

#                 Original User Request:
#                 {st.session_state.latest_question}

#                 User Clarification:
#                 {clarification_answer}

#                 Current Intent State:
#                 {st.session_state.intent_state}

#                 """

#                 # =============================
#                 # RUN GRAPH AGAIN
#                 # =============================

#                 response = graph.invoke(

#                     {

#                         "question":

#                         merged_query,

#                         "conversation_history":

#                         st.session_state.conversation_history,

#                         "intent_state":

#                         st.session_state.intent_state

#                     }

#                 )

#                 # =============================
#                 # STILL NEEDS CLARIFICATION
#                 # =============================

#                 if response.get(

#                     "needs_clarification",

#                     False

#                 ):

#                     st.session_state.intent_state = (

#                         response.get(

#                             "updated_intent_state",

#                             {}

#                         )

#                     )

#                     st.session_state.current_clarification_question = (

#                         response.get(

#                             "clarification_question",

#                             "Please clarify further."

#                         )

#                     )

#                     st.rerun()

#                 # =============================
#                 # FINAL QUERY READY
#                 # =============================

#                 else:

#                     st.session_state.awaiting_clarification = False

#                     st.success(

#                         "Final query understood."

#                     )

#                     # =========================
#                     # GENERATED SQL
#                     # =========================

#                     st.subheader(

#                         "🛢 Generated SQL"

#                     )

#                     st.code(

#                         response.get(

#                             "generated_sql",

#                             ""

#                         ),

#                         language="sql"

#                     )

#                     # =========================
#                     # VALIDATION STATUS
#                     # =========================

#                     st.subheader(

#                         "✅ Validation"

#                     )

#                     if response.get(

#                         "is_valid",

#                         False

#                     ):

#                         st.success(

#                             response.get(

#                                 "validation_reason",

#                                 "SQL validated."

#                             )

#                         )

#                     else:

#                         st.error(

#                             response.get(

#                                 "validation_reason",

#                                 "Validation failed."

#                             )

#                         )

#                     # =========================
#                     # QUERY RESULT
#                     # =========================

#                     result = response.get(

#                         "query_result"

#                     )

#                     if isinstance(

#                         result,

#                         pd.DataFrame

#                     ):

#                         st.subheader(

#                             "📊 Query Results"

#                         )

#                         st.dataframe(

#                             result,

#                             use_container_width=True,

#                             hide_index=True

#                         )

#                         # =====================
#                         # METRICS
#                         # =====================

#                         col1, col2 = st.columns(2)

#                         with col1:

#                             st.metric(

#                                 "Rows",

#                                 len(result)

#                             )

#                         with col2:

#                             st.metric(

#                                 "Columns",

#                                 len(result.columns)

#                             )

#                         # =====================
#                         # DOWNLOAD CSV
#                         # =====================

#                         csv = result.to_csv(

#                             index=False

#                         ).encode("utf-8")

#                         st.download_button(

#                             label="⬇ Download CSV",

#                             data=csv,

#                             file_name="query_result.csv",

#                             mime="text/csv"

#                         )

#                     else:

#                         st.error(result)

#                     # =========================
#                     # EXPORT STATUS
#                     # =========================

#                     st.subheader(

#                         "📁 Export Status"

#                     )

#                     st.success(

#                         response.get(

#                             "export_path",

#                             "Export complete."

#                         )

#                     )

#                     st.rerun()

#             except Exception as e:

#                 st.error(

#                     f"Application Error: {e}"

#                 )

# # =========================================
# # MAIN GENERATE BUTTON
# # =========================================

# if not st.session_state.awaiting_clarification:

#     if st.button(

#         "Generate Report",

#         key="generate_btn"

#     ):

#         if question.strip() == "":

#             st.warning(

#                 "Please enter a question."

#             )

#         else:

#             with st.spinner(

#                 "Understanding your request..."

#             ):

#                 try:

#                     # =================================
#                     # SAVE QUESTION
#                     # =================================

#                     st.session_state.latest_question = (

#                         question

#                     )

#                     # =================================
#                     # RUN GRAPH
#                     # =================================

#                     response = graph.invoke(

#                         {

#                             "question": question,

#                             "conversation_history":

#                             st.session_state.conversation_history,

#                             "intent_state":

#                             st.session_state.intent_state

#                         }

#                     )

#                     # =================================
#                     # STORE USER HISTORY
#                     # =================================

#                     st.session_state.conversation_history.append(

#                         {

#                             "user": question

#                         }

#                     )

#                     # =================================
#                     # IRRELEVANT QUERY
#                     # =================================

#                     if not response.get(

#                         "is_relevant",

#                         True

#                     ):

#                         st.error(

#                             "I'm sorry, I can only help "
#                             "with business analytics "
#                             "and reporting queries."

#                         )

#                     # =================================
#                     # NEEDS CLARIFICATION
#                     # =================================

#                     elif response.get(

#                         "needs_clarification",

#                         False

#                     ):

#                         st.session_state.awaiting_clarification = True

#                         st.session_state.intent_state = (

#                             response.get(

#                                 "updated_intent_state",

#                                 {}

#                             )

#                         )

#                         st.session_state.current_clarification_question = (

#                             response.get(

#                                 "clarification_question",

#                                 "Please clarify."

#                             )

#                         )

#                         st.rerun()

#                     # =================================
#                     # FINAL QUERY READY
#                     # =================================

#                     else:

#                         st.success(

#                             "Final query understood."

#                         )

#                         # =============================
#                         # GENERATED SQL
#                         # =============================

#                         st.subheader(

#                             "🛢 Generated SQL"

#                         )

#                         st.code(

#                             response.get(

#                                 "generated_sql",

#                                 ""

#                             ),

#                             language="sql"

#                         )

#                         # =============================
#                         # VALIDATION
#                         # =============================

#                         st.subheader(

#                             "✅ Validation"

#                         )

#                         if response.get(

#                             "is_valid",

#                             False

#                         ):

#                             st.success(

#                                 response.get(

#                                     "validation_reason",

#                                     "SQL validated."

#                                 )

#                             )

#                         else:

#                             st.error(

#                                 response.get(

#                                     "validation_reason",

#                                     "Validation failed."

#                                 )

#                             )

#                         # =============================
#                         # QUERY RESULT
#                         # =============================

#                         result = response.get(

#                             "query_result"

#                         )

#                         if isinstance(

#                             result,

#                             pd.DataFrame

#                         ):

#                             st.subheader(

#                                 "📊 Query Results"

#                             )

#                             st.dataframe(

#                                 result,

#                                 use_container_width=True,

#                                 hide_index=True

#                             )

#                             # =========================
#                             # METRICS
#                             # =========================

#                             col1, col2 = st.columns(2)

#                             with col1:

#                                 st.metric(

#                                     "Rows",

#                                     len(result)

#                                 )

#                             with col2:

#                                 st.metric(

#                                     "Columns",

#                                     len(result.columns)

#                                 )

#                             # =========================
#                             # DOWNLOAD BUTTON
#                             # =========================

#                             csv = result.to_csv(

#                                 index=False

#                             ).encode("utf-8")

#                             st.download_button(

#                                 label="⬇ Download CSV",

#                                 data=csv,

#                                 file_name="query_result.csv",

#                                 mime="text/csv"

#                             )

#                         else:

#                             st.error(result)

#                         # =============================
#                         # EXPORT STATUS
#                         # =============================

#                         st.subheader(

#                             "📁 Export Status"

#                         )

#                         st.success(

#                             response.get(

#                                 "export_path",

#                                 "Export complete."

#                             )

#                         )

#                 except Exception as e:

#                     st.error(

#                         f"Application Error: {e}"

#                     )
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
# SESSION STATE
# =========================================

if "conversation_history" not in st.session_state:

    st.session_state.conversation_history = []

if "intent_state" not in st.session_state:

    st.session_state.intent_state = {}

if "awaiting_clarification" not in st.session_state:

    st.session_state.awaiting_clarification = False

if "latest_question" not in st.session_state:

    st.session_state.latest_question = ""

if "current_clarification_question" not in st.session_state:

    st.session_state.current_clarification_question = ""

if "latest_response" not in st.session_state:

    st.session_state.latest_response = None

# =========================================
# USER INPUT
# =========================================

question = st.text_input(

    "Enter your question:",

    placeholder="Example: Show monthly product wise sales for 2025"

)

# =========================================
# CLARIFICATION SECTION
# =========================================

if st.session_state.awaiting_clarification:

    st.info(

        st.session_state.current_clarification_question

    )

    clarification_answer = st.text_input(

        "Answer the clarification question",

        key="clarification_input"

    )

    # =====================================
    # SUBMIT CLARIFICATION
    # =====================================

    if st.button(

        "Submit Clarification",

        key="clarification_btn"

    ):

        if clarification_answer.strip() == "":

            st.warning(

                "Please answer the clarification question."

            )

        else:

            with st.spinner(

                "Refining your request..."

            ):

                try:

                    # =============================
                    # STORE USER RESPONSE
                    # =============================

                    st.session_state.conversation_history.append(

                        {

                            "user":

                            clarification_answer

                        }

                    )

                    # =============================
                    # STRUCTURED QUERY MERGE
                    # =============================

                    merged_query = f"""

                    Original User Request:
                    {st.session_state.latest_question}

                    User Clarification:
                    {clarification_answer}

                    Current Intent State:
                    {st.session_state.intent_state}

                    """

                    # =============================
                    # RUN GRAPH
                    # =============================

                    response = graph.invoke(

                        {

                            "question":

                            merged_query,

                            "conversation_history":

                            st.session_state.conversation_history,

                            "intent_state":

                            st.session_state.intent_state

                        }

                    )

                    # =============================
                    # NEEDS MORE CLARIFICATION
                    # =============================

                    if (

                        response.get(

                            "needs_clarification",

                            False

                        )

                        and

                        not response.get(

                            "is_query_actionable",

                            False

                        )

                        and

                        response.get(

                            "confidence_score",

                            0

                        ) < 0.75

                    ):

                        st.session_state.awaiting_clarification = True

                        st.session_state.intent_state = (

                            response.get(

                                "updated_intent_state",

                                {}

                            )

                        )

                        st.session_state.current_clarification_question = (

                            response.get(

                                "clarification_question",

                                "Please clarify further."

                            )

                        )

                        st.rerun()

                    # =============================
                    # FINAL QUERY READY
                    # =============================

                    else:

                        st.session_state.awaiting_clarification = False

                        st.session_state.latest_response = response

                        st.rerun()

                except Exception as e:

                    st.error(

                        f"Application Error: {e}"

                    )

# =========================================
# MAIN GENERATE BUTTON
# =========================================

if not st.session_state.awaiting_clarification:

    if st.button(

        "Generate Report",

        key="generate_btn"

    ):

        if question.strip() == "":

            st.warning(

                "Please enter a question."

            )

        else:

            with st.spinner(

                "Understanding your request..."

            ):

                try:

                    # =================================
                    # STORE QUESTION
                    # =================================

                    st.session_state.latest_question = (

                        question

                    )

                    # =================================
                    # RUN GRAPH
                    # =================================

                    response = graph.invoke(

                        {

                            "question": question,

                            "conversation_history":

                            st.session_state.conversation_history,

                            "intent_state":

                            st.session_state.intent_state

                        }

                    )

                    # =================================
                    # STORE HISTORY
                    # =================================

                    st.session_state.conversation_history.append(

                        {

                            "user": question

                        }

                    )

                    # =================================
                    # IRRELEVANT QUERY
                    # =================================

                    if not response.get(

                        "is_relevant",

                        True

                    ):

                        st.error(

                            "I'm sorry, I can only help "
                            "with business analytics "
                            "and reporting queries."

                        )

                    # =================================
                    # NEEDS CLARIFICATION
                    # =================================

                    elif (

                        response.get(

                            "needs_clarification",

                            False

                        )

                        and

                        not response.get(

                            "is_query_actionable",

                            False

                        )

                        and

                        response.get(

                            "confidence_score",

                            0

                        ) < 0.75

                    ):

                        st.session_state.awaiting_clarification = True

                        st.session_state.intent_state = (

                            response.get(

                                "updated_intent_state",

                                {}

                            )

                        )

                        st.session_state.current_clarification_question = (

                            response.get(

                                "clarification_question",

                                "Please clarify."

                            )

                        )

                        st.rerun()

                    # =================================
                    # FINAL QUERY READY
                    # =================================

                    else:

                        st.session_state.latest_response = response

                        st.rerun()

                except Exception as e:

                    st.error(

                        f"Application Error: {e}"

                    )

# =========================================
# FINAL RESULT DISPLAY
# =========================================

if st.session_state.latest_response:

    response = st.session_state.latest_response

    st.success(

        "Final query understood."

    )

    # =====================================
    # SHOW CONFIDENCE
    # =====================================

    # confidence = response.get(

    #     "confidence_score",

    #     0

    # )

    # st.metric(

    #     "Confidence Score",

    #     f"{confidence:.2f}"

    # )

    # =====================================
    # GENERATED SQL
    # =====================================

    st.subheader(

        "🛢 Generated SQL"

    )

    st.code(

        response.get(

            "generated_sql",

            ""

        ),

        language="sql"

    )

    # =====================================
    # VALIDATION
    # =====================================

    st.subheader(

        "✅ Validation"

    )

    if response.get(

        "is_valid",

        False

    ):

        st.success(

            response.get(

                "validation_reason",

                "SQL validated."

            )

        )

    else:

        st.error(

            response.get(

                "validation_reason",

                "Validation failed."

            )

        )

    # =====================================
    # QUERY RESULTS
    # =====================================

    result = response.get(

        "query_result"

    )

    if isinstance(

        result,

        pd.DataFrame

    ):

        st.subheader(

            "📊 Query Results"

        )

        st.dataframe(

            result,

            use_container_width=True,

            hide_index=True

        )

        # =================================
        # METRICS
        # =================================

        col1, col2 = st.columns(2)

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

        # =================================
        # DOWNLOAD BUTTON
        # =================================

        csv = result.to_csv(

            index=False

        ).encode("utf-8")

        st.download_button(

            label="⬇ Download CSV",

            data=csv,

            file_name="query_result.csv",

            mime="text/csv"

        )

        # =================================
        # OPTIONAL VISUALIZATION
        # =================================

        numeric_columns = result.select_dtypes(

            include="number"

        ).columns

        text_columns = result.select_dtypes(

            include="object"

        ).columns

        if (

            len(numeric_columns) > 0

            and len(text_columns) > 0

        ):

            st.subheader(

                "📈 Visualization"

            )

            chart_df = result[

                [

                    text_columns[0],

                    numeric_columns[0]

                ]

            ]

            chart_df = chart_df.set_index(

                text_columns[0]

            )

            st.bar_chart(

                chart_df

            )

    else:

        st.error(result)

    # =====================================
    # EXPORT STATUS
    # =====================================

    st.subheader(

        "📁 Export Status"

    )

    st.success(

        response.get(

            "export_path",

            "Export complete."

        )

    )