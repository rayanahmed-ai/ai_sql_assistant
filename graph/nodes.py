# # =========================================
# # IMPORT FUNCTIONS
# # =========================================

# from nlp.spacy_processor import query_processor

# from database.schema_loader import schema_loader

# from rag.retriever import retrieve_context

# from llm.sql_generator import generate_sql

# from validation.sql_validator import validate_sql

# from database.query_executor import execute_query

# from exports.exporter import export_to_csv

# # =========================================
# # PREPROCESS NODE
# # =========================================

# def preprocess_node(state):

#     cleaned_query = query_processor(

#         state["question"]

#     )

#     return {

#         "cleaned_query": cleaned_query

#     }

# # =========================================
# # SCHEMA LOADER NODE
# # =========================================

# def schema_node(state):

#     schema = schema_loader()

#     return {

#         "schema": schema

#     }

# # =========================================
# # RAG RETRIEVER NODE
# # =========================================

# def rag_node(state):

#     rag_context = retrieve_context(

#         state["cleaned_query"]

#     )

#     return {

#         "rag_context": rag_context

#     }

# # =========================================
# # SQL GENERATION NODE
# # =========================================

# def sql_node(state):

#     generated_sql = generate_sql(

#         question=state["cleaned_query"],

#         schema=state["schema"],

#         rag_context=state["rag_context"]

#     )

#     return {

#         "generated_sql": generated_sql

#     }

# # =========================================
# # VALIDATION NODE
# # =========================================

# def validation_node(state):

#     validation_result = validate_sql(

#         state["generated_sql"]

#     )

#     return {

#         "is_valid": validation_result["valid"],

#         "validation_reason":

#         validation_result["reason"]

#     }

# # =========================================
# # QUERY EXECUTION NODE
# # =========================================

# def execution_node(state):

#     result = execute_query(

#         state["generated_sql"]

#     )

#     return {

#         "query_result": result

#     }

# # =========================================
# # EXPORT NODE
# # =========================================

# # def export_node(state):

# #     export_path = export_to_csv(

# #         state["query_result"]

# #     )

# #     return {

# #         "export_path": export_path

# #     }
# def export_node(state):

#     result = state["query_result"]

#     # =====================================
#     # SKIP EXPORT IF ERROR
#     # =====================================

#     if isinstance(result, str):

#         return {

#             "export_path":

#             "Export skipped due to execution error."

#         }

#     export_path = export_to_csv(

#         result

#     )

#     return {

#         "export_path": export_path

#     }

# # =========================================
# # BLOCKED NODE
# # =========================================

# def blocked_node(state):

#     return {

#         "query_result":

#         f"Blocked Query: "

#         f"{state['validation_reason']}"

#     }
# =========================================
# IMPORT FUNCTIONS
# =========================================

from nlp.spacy_processor import query_processor

from database.schema_loader import schema_loader

from rag.retriever import retrieve_context

from llm.sql_generator import generate_sql

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

def clarification_node(state):

    query = state["cleaned_query"]

    clarification_question = ""

    needs_clarification = False

    # =====================================
    # SALES WITHOUT DATE
    # =====================================

    if "sales" in query:

        if (

            "2025" not in query

            and "2024" not in query

            and "month" not in query

            and "year" not in query

        ):

            clarification_question = (

                "Do you want sales for a "

                "specific year or all years?"

            )

            needs_clarification = True

    # =====================================
    # REGION CHECK
    # =====================================

    elif "region" in query:

        if (

            "north" not in query

            and "south" not in query

            and "east" not in query

            and "west" not in query

        ):

            clarification_question = (

                "Do you want all regions "

                "or a specific region?"

            )

            needs_clarification = True

    # =====================================
    # CUSTOMER ANALYTICS
    # =====================================

    elif "customer" in query:

        if "sales" not in query and "purchase" not in query:

            clarification_question = (

                "Do you want customer details "

                "or customer sales analysis?"

            )

            needs_clarification = True

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
