# from langchain_google_genai import ChatGoogleGenerativeAI

# import streamlit as st

# # =========================================
# # GEMINI MODEL
# # =========================================

# # llm = ChatGoogleGenerativeAI(

# #     model="gemini-pro",

# #     google_api_key=st.secrets["API_KEY"]

# # )
# # llm = ChatGoogleGenerativeAI(

# #     model="models/gemini-1.5-flash-latest",

# #     google_api_key=st.secrets["API_KEY"],

# #     temperature=0

# # # )
# llm = ChatGoogleGenerativeAI(

#     model="models/gemini-2.0-flash",

#     temperature=0,

#     google_api_key=st.secrets["API_KEY"]
# )
# # model = ChatGoogleGenerativeAI(
# #     model="gemini-1.5-flash",
# #     temperature=0,
# #     api_key=os.getenv("API_KEY")
# # )

# # =========================================
# # DETECT AMBIGUITY
# # =========================================

# def detect_ambiguity(query):

#     prompt = f"""

#     You are an AI Business Intelligence Assistant.

#     Analyze the user query.

#     Determine whether the query is ambiguous
#     or missing important business information.

#     Examples:
#     - missing date range
#     - missing region
#     - missing granularity
#     - missing filters

#     User Query:
#     {query}

#     Return ONLY in this format:

#     NEEDS_CLARIFICATION: YES or NO

#     QUESTION: clarification question or NONE
#     """

#     response = llm.invoke(prompt)

#     text = response.content

#     needs = "YES" in text

#     question = "NONE"

#     if "QUESTION:" in text:

#         question = (

#             text.split("QUESTION:")[-1]

#             .strip()

#         )

#     return {

#         "needs_clarification": needs,

#         "clarification_question": question

#     }
# =========================================
# CLARIFICATION NODE
# =========================================

def clarification_node(state):

    query = state["cleaned_query"].lower()

    # =====================================
    # DEFAULT VALUES
    # =====================================

    needs_clarification = False

    clarification_question = ""

    # =====================================
    # SALES WITHOUT DATE RANGE
    # =====================================

    if "sales" in query:

        if (

            "2025" not in query

            and "2024" not in query

            and "2023" not in query

            and "month" not in query

            and "year" not in query

            and "last year" not in query

            and "this month" not in query

        ):

            needs_clarification = True

            clarification_question = (

                "Do you want sales for all periods "

                "or a specific date range?"

            )

    # =====================================
    # REGION CLARIFICATION
    # =====================================

    elif "region" in query:

        if (

            "north" not in query

            and "south" not in query

            and "east" not in query

            and "west" not in query

        ):

            needs_clarification = True

            clarification_question = (

                "Do you want the report for all "

                "regions or a particular region?"

            )

    # =====================================
    # ORDER FILTERS
    # =====================================

    elif "orders" in query:

        if "cancelled" not in query:

            needs_clarification = True

            clarification_question = (

                "Should cancelled orders be included?"

            )

    # =====================================
    # PRODUCT SUMMARY VS DETAIL
    # =====================================

    elif "product" in query:

        if (

            "summary" not in query

            and "detail" not in query

            and "transaction" not in query

        ):

            needs_clarification = True

            clarification_question = (

                "Do you want product-wise summary "

                "or detailed transaction-level data?"

            )

    # =====================================
    # CUSTOMER ANALYTICS
    # =====================================

    elif "customer" in query:

        if (

            "sales" not in query

            and "purchase" not in query

        ):

            needs_clarification = True

            clarification_question = (

                "Do you want customer details "

                "or customer purchase analysis?"

            )

    # =====================================
    # RETURN STATE
    # =====================================

    return {

        "needs_clarification":

        needs_clarification,

        "clarification_question":

        clarification_question

    }
