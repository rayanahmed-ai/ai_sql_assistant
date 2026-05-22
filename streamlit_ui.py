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
# USER INPUT
# =========================================

question = st.text_input(

    "Enter your question:",

    placeholder="Example: Show monthly product wise sales for 2025"

)

# =========================================
# RUN BUTTON
# =========================================

if st.button("Generate Report"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating SQL and fetching results..."):

            try:

                # =====================================
                # RUN LANGGRAPH WORKFLOW
                # =====================================

                response = graph.invoke(

                    {

                        "question": question

                    }

                )

                # =====================================
                # DISPLAY CLEANED QUERY
                # =====================================

                st.subheader("🧠 Processed Query")

                st.code(

                    response["cleaned_query"],

                    language="text"

                )

                # =====================================
                # DISPLAY RAG CONTEXT
                # =====================================

                st.subheader("📚 Retrieved Context")

                st.info(

                    response["rag_context"]

                )

                # =====================================
                # DISPLAY GENERATED SQL
                # =====================================

                st.subheader("🛢 Generated SQL")

                st.code(

                    response["generated_sql"],

                    language="sql"

                )

                # =====================================
                # VALIDATION STATUS
                # =====================================

                st.subheader("✅ Validation")

                if response["is_valid"]:

                    st.success(

                        response["validation_reason"]

                    )

                else:

                    st.error(

                        response["validation_reason"]

                    )

                # =====================================
                # DISPLAY QUERY RESULT
                # =====================================

                st.subheader("📊 Query Results")

                result = response["query_result"]

                # =====================================
                # HANDLE DATAFRAME
                # =====================================

                if isinstance(result, pd.DataFrame):

                    st.dataframe(

                        result,

                        use_container_width=True,

                        hide_index=True

                    )

                    # =================================
                    # METRICS
                    # =================================

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

                        if "MonthlySales" in result.columns:

                            st.metric(

                                "Total Sales",

                                f"{result['MonthlySales'].sum():,.0f}"

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
                    # OPTIONAL CHART
                    # =================================

                    if (

                        "ProductName" in result.columns

                        and "MonthlySales" in result.columns

                    ):

                        st.subheader("📈 Sales Visualization")

                        chart_df = (

                            result.groupby(

                                "ProductName"

                            )["MonthlySales"]

                            .sum()

                            .reset_index()

                        )

                        st.bar_chart(

                            chart_df.set_index(

                                "ProductName"

                            )

                        )

                else:

                    st.error(result)

                # =====================================
                # EXPORT PATH
                # =====================================

                st.subheader("📁 Export Status")

                st.success(

                    f"CSV saved successfully: "
                    f"{response['export_path']}"

                )

            except Exception as e:

                st.error(

                    f"Application Error: {e}"

                )