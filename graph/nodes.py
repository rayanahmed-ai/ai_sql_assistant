# # # # =========================================
# # # # IMPORT FUNCTIONS
# # # # =========================================

# # # from nlp.spacy_processor import query_processor

# # # from database.schema_loader import schema_loader

# # # from rag.retriever import retrieve_context

# # # from llm.sql_generator import generate_sql

# # # from validation.sql_validator import validate_sql

# # # from database.query_executor import execute_query

# # # from exports.exporter import export_to_csv

# # # # =========================================
# # # # PREPROCESS NODE
# # # # =========================================

# # # def preprocess_node(state):

# # #     cleaned_query = query_processor(

# # #         state["question"]

# # #     )

# # #     return {

# # #         "cleaned_query": cleaned_query

# # #     }

# # # # =========================================
# # # # SCHEMA LOADER NODE
# # # # =========================================

# # # def schema_node(state):

# # #     schema = schema_loader()

# # #     return {

# # #         "schema": schema

# # #     }

# # # # =========================================
# # # # RAG RETRIEVER NODE
# # # # =========================================

# # # def rag_node(state):

# # #     rag_context = retrieve_context(

# # #         state["cleaned_query"]

# # #     )

# # #     return {

# # #         "rag_context": rag_context

# # #     }

# # # # =========================================
# # # # SQL GENERATION NODE
# # # # =========================================

# # # def sql_node(state):

# # #     generated_sql = generate_sql(

# # #         question=state["cleaned_query"],

# # #         schema=state["schema"],

# # #         rag_context=state["rag_context"]

# # #     )

# # #     return {

# # #         "generated_sql": generated_sql

# # #     }

# # # # =========================================
# # # # VALIDATION NODE
# # # # =========================================

# # # def validation_node(state):

# # #     validation_result = validate_sql(

# # #         state["generated_sql"]

# # #     )

# # #     return {

# # #         "is_valid": validation_result["valid"],

# # #         "validation_reason":

# # #         validation_result["reason"]

# # #     }

# # # # =========================================
# # # # QUERY EXECUTION NODE
# # # # =========================================

# # # def execution_node(state):

# # #     result = execute_query(

# # #         state["generated_sql"]

# # #     )

# # #     return {

# # #         "query_result": result

# # #     }

# # # # =========================================
# # # # EXPORT NODE
# # # # =========================================

# # # # def export_node(state):

# # # #     export_path = export_to_csv(

# # # #         state["query_result"]

# # # #     )

# # # #     return {

# # # #         "export_path": export_path

# # # #     }
# # # def export_node(state):

# # #     result = state["query_result"]

# # #     # =====================================
# # #     # SKIP EXPORT IF ERROR
# # #     # =====================================

# # #     if isinstance(result, str):

# # #         return {

# # #             "export_path":

# # #             "Export skipped due to execution error."

# # #         }

# # #     export_path = export_to_csv(

# # #         result

# # #     )

# # #     return {

# # #         "export_path": export_path

# # #     }

# # # # =========================================
# # # # BLOCKED NODE
# # # # =========================================

# # # def blocked_node(state):

# # #     return {

# # #         "query_result":

# # #         f"Blocked Query: "

# # #         f"{state['validation_reason']}"

# # #     }
# # # =========================================
# # # IMPORT FUNCTIONS
# # # =========================================

# # from nlp.spacy_processor import query_processor

# # from database.schema_loader import schema_loader

# # from rag.retriever import retrieve_context

# # from llm.sql_generator import generate_sql

# # from validation.sql_validator import validate_sql

# # from database.query_executor import execute_query

# # from exports.exporter import export_to_csv

# # # =========================================
# # # PREPROCESS NODE
# # # =========================================

# # def preprocess_node(state):

# #     cleaned_query = query_processor(

# #         state["question"]

# #     )

# #     return {

# #         "cleaned_query": cleaned_query

# #     }

# # # =========================================
# # # CLARIFICATION NODE
# # # =========================================

# # def clarification_node(state):

# #     query = state["cleaned_query"]

# #     clarification_question = ""

# #     needs_clarification = False

# #     # =====================================
# #     # SALES WITHOUT DATE
# #     # =====================================

# #     if "sales" in query:

# #         if (

# #             "2025" not in query

# #             and "2024" not in query

# #             and "month" not in query

# #             and "year" not in query

# #         ):

# #             clarification_question = (

# #                 "Do you want sales for a "

# #                 "specific year or all years?"

# #             )

# #             needs_clarification = True

# #     # =====================================
# #     # REGION CHECK
# #     # =====================================

# #     elif "region" in query:

# #         if (

# #             "north" not in query

# #             and "south" not in query

# #             and "east" not in query

# #             and "west" not in query

# #         ):

# #             clarification_question = (

# #                 "Do you want all regions "

# #                 "or a specific region?"

# #             )

# #             needs_clarification = True

# #     # =====================================
# #     # CUSTOMER ANALYTICS
# #     # =====================================

# #     elif "customer" in query:

# #         if "sales" not in query and "purchase" not in query:

# #             clarification_question = (

# #                 "Do you want customer details "

# #                 "or customer sales analysis?"

# #             )

# #             needs_clarification = True

# #     # =====================================
# #     # RETURN STATE
# #     # =====================================

# #     return {

# #         "needs_clarification":

# #         needs_clarification,

# #         "clarification_question":

# #         clarification_question

# #     }

# # # =========================================
# # # SCHEMA LOADER NODE
# # # =========================================

# # def schema_node(state):

# #     schema = schema_loader()

# #     return {

# #         "schema": schema

# #     }

# # # =========================================
# # # RAG RETRIEVER NODE
# # # =========================================

# # def rag_node(state):

# #     rag_context = retrieve_context(

# #         state["cleaned_query"]

# #     )

# #     return {

# #         "rag_context": rag_context

# #     }

# # # =========================================
# # # SQL GENERATION NODE
# # # =========================================

# # def sql_node(state):

# #     generated_sql = generate_sql(

# #         question=state["cleaned_query"],

# #         schema=state["schema"],

# #         rag_context=state["rag_context"]

# #     )

# #     return {

# #         "generated_sql": generated_sql

# #     }

# # # =========================================
# # # VALIDATION NODE
# # # =========================================

# # def validation_node(state):

# #     validation_result = validate_sql(

# #         state["generated_sql"]

# #     )

# #     return {

# #         "is_valid": validation_result["valid"],

# #         "validation_reason":

# #         validation_result["reason"]

# #     }

# # # =========================================
# # # QUERY EXECUTION NODE
# # # =========================================

# # def execution_node(state):

# #     result = execute_query(

# #         state["generated_sql"]

# #     )

# #     return {

# #         "query_result": result

# #     }

# # # =========================================
# # # EXPORT NODE
# # # =========================================

# # def export_node(state):

# #     result = state["query_result"]

# #     # =====================================
# #     # SKIP EXPORT IF ERROR
# #     # =====================================

# #     if isinstance(result, str):

# #         return {

# #             "export_path":

# #             "Export skipped due to execution error."

# #         }

# #     export_path = export_to_csv(

# #         result

# #     )

# #     return {

# #         "export_path": export_path

# #     }

# # # =========================================
# # # BLOCKED NODE
# # # =========================================

# # def blocked_node(state):

# #     return {

# #         "query_result":

# #         f"Blocked Query: "

# #         f"{state['validation_reason']}"

# #     }
# import pandas as pd

# from nlp.query_processor import query_processor

# from database.schema_loader import schema_loader

# from rag.retriever import retrieve_context

# from llm.sql_generator import generate_sql

# from validation.validate_sql import validate_sql

# from database.query_executor import execute_query

# from exports.export import export_to_csv


# # =========================================
# # NLP PREPROCESS NODE
# # =========================================

# def preprocess_node(state):

#     cleaned_query = query_processor(

#         state["question"]

#     )

#     return {

#         **state,

#         "cleaned_query": cleaned_query

#     }


# # =========================================
# # CLARIFICATION NODE
# # =========================================

# def clarification_node(state):

#     question = state["cleaned_query"].lower()

#     clarification_keywords = [

#         "sales",

#         "profit",

#         "revenue"

#     ]

#     has_year = any(

#         year in question

#         for year in [

#             "2023",

#             "2024",

#             "2025",

#             "2026"

#         ]

#     )

#     needs_clarification = (

#         any(

#             keyword in question

#             for keyword in clarification_keywords

#         )

#         and not has_year

#     )

#     if needs_clarification:

#         return {

#             **state,

#             "needs_clarification": True,

#             "clarification_message":

#                 "Please specify the year."

#         }

#     return {

#         **state,

#         "needs_clarification": False,

#         "clarification_message": ""

#     }


# # =========================================
# # SCHEMA NODE
# # =========================================

# def schema_node(state):

#     schema = schema_loader()

#     return {

#         **state,

#         "schema": schema

#     }


# # =========================================
# # RAG NODE
# # =========================================

# def rag_node(state):

#     context = retrieve_context(

#         state["cleaned_query"]

#     )

#     return {

#         **state,

#         "rag_context": context

#     }


# # =========================================
# # SQL GENERATION NODE
# # =========================================

# def sql_node(state):

#     sql_query = generate_sql(

#         question=state["cleaned_query"],

#         schema=state["schema"],

#         rag_context=state["rag_context"]

#     )

#     return {

#         **state,

#         "generated_sql": sql_query

#     }


# # =========================================
# # VALIDATION NODE
# # =========================================

# def validation_node(state):

#     is_valid = validate_sql(

#         state["generated_sql"]

#     )

#     reason = (

#         "Safe SELECT query."

#         if is_valid

#         else "Blocked dangerous query."

#     )

#     return {

#         **state,

#         "is_valid": is_valid,

#         "validation_reason": reason

#     }


# # =========================================
# # EXECUTION NODE
# # =========================================

# def execution_node(state):

#     result = execute_query(

#         state["generated_sql"]

#     )

#     return {

#         **state,

#         "query_result": result

#     }


# # =========================================
# # EXPORT NODE
# # =========================================

# def export_node(state):

#     export_path = export_to_csv(

#         state["query_result"]

#     )

#     return {

#         **state,

#         "export_path": export_path

#     }


# # =========================================
# # BLOCKED NODE
# # =========================================

# def blocked_node(state):

#     return {

#         **state,

#         "query_result":

#             pd.DataFrame(

#                 {

#                     "ERROR": [

#                         "Query blocked for security reasons."

#                     ]

#                 }

#             )

#     }
# =========================================
# IMPORT FUNCTIONS
# =========================================

from nlp.spacy_processor import query_processor

from database.schema_loader import schema_loader

from rag.retriever import retrieve_context

from llm.sql_generator import generate_sql

from llm.clarification_llm import detect_ambiguity

from validation.sql_validator import validate_sql

from database.query_executor import execute_query

from exports.exporter import export_to_csv

# =========================================
# PREPROCESS NODE
# =========================================

def preprocess_node(state):

    cleaned_query = query_processor(

        state["question"]

    )

    return {

        "cleaned_query": cleaned_query

    }

# =========================================
# CLARIFICATION NODE
# =========================================

# def clarification_node(state):

#     result = detect_ambiguity(

#         state["cleaned_query"]

#     )

#     return {

#         "needs_clarification":

#         result["needs_clarification"],

#         "clarification_question":

#         result["clarification_question"]

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
# =========================================
# SCHEMA LOADER NODE
# =========================================

def schema_node(state):

    schema = schema_loader()

    return {

        "schema": schema

    }

# =========================================
# RAG RETRIEVER NODE
# =========================================

def rag_node(state):

    rag_context = retrieve_context(

        state["cleaned_query"]

    )

    return {

        "rag_context": rag_context

    }

# =========================================
# SQL GENERATION NODE
# =========================================

def sql_node(state):

    generated_sql = generate_sql(

        question=state["cleaned_query"],

        schema=state["schema"],

        rag_context=state["rag_context"]

    )

    return {

        "generated_sql": generated_sql

    }

# =========================================
# VALIDATION NODE
# =========================================

def validation_node(state):

    validation_result = validate_sql(

        state["generated_sql"]

    )

    return {

        "is_valid": validation_result["valid"],

        "validation_reason":

        validation_result["reason"]

    }

# =========================================
# QUERY EXECUTION NODE
# =========================================

def execution_node(state):

    result = execute_query(

        state["generated_sql"]

    )

    return {

        "query_result": result

    }

# =========================================
# EXPORT NODE
# =========================================

def export_node(state):

    result = state["query_result"]

    # =====================================
    # SKIP EXPORT IF ERROR
    # =====================================

    if isinstance(result, str):

        return {

            "export_path":

            "Export skipped due to execution error."

        }

    export_path = export_to_csv(

        result

    )

    return {

        "export_path": export_path

    }

# =========================================
# BLOCKED NODE
# =========================================

def blocked_node(state):

    return {

        "query_result":

        f"Blocked Query: "

        f"{state['validation_reason']}"

    }
