from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st

# =========================================
# GEMINI MODEL
# =========================================

# llm = ChatGoogleGenerativeAI(

#     model="gemini-pro",

#     google_api_key=st.secrets["API_KEY"]

# )
# llm = ChatGoogleGenerativeAI(

#     model="models/gemini-1.5-flash-latest",

#     google_api_key=st.secrets["API_KEY"],

#     temperature=0

# # )
llm = ChatGoogleGenerativeAI(

    model="models/gemini-2.0-flash",

    temperature=0,

    google_api_key=st.secrets["API_KEY"]
)
# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0,
#     api_key=os.getenv("API_KEY")
# )

# =========================================
# DETECT AMBIGUITY
# =========================================

def detect_ambiguity(query):

    prompt = f"""

    You are an AI Business Intelligence Assistant.

    Analyze the user query.

    Determine whether the query is ambiguous
    or missing important business information.

    Examples:
    - missing date range
    - missing region
    - missing granularity
    - missing filters

    User Query:
    {query}

    Return ONLY in this format:

    NEEDS_CLARIFICATION: YES or NO

    QUESTION: clarification question or NONE
    """

    response = llm.invoke(prompt)

    text = response.content

    needs = "YES" in text

    question = "NONE"

    if "QUESTION:" in text:

        question = (

            text.split("QUESTION:")[-1]

            .strip()

        )

    return {

        "needs_clarification": needs,

        "clarification_question": question

    }
