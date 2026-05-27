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

# # def execution_node(state):

# #     # result = execute_query(

# #     #     state["generated_sql"]

# #     # )
# #     result = execute_query(

# #     sql_query=state["generated_sql"],

# #     schema=state["schema"]

# # )

# #     return {

# #         "query_result": result

# #     }
# # =========================================
# # QUERY EXECUTION NODE
# # =========================================

# def execution_node(state):

#     result = execute_query(

#         sql_query=state["generated_sql"],

#         schema=state["schema"]

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

from validation.validation_retriever import (
    retrieve_validation_context
)

from validation.validation_agent import (
    validation_agent
)

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
# VALIDATION RAG NODE
# =========================================

def validation_rag_node(state):

    validation_context = (

        retrieve_validation_context(

            state["question"]

        )

    )

    return {

        "validation_context":

        validation_context

    }

# =========================================
# VALIDATION AGENT NODE
# =========================================

def validation_agent_node(state):

    response = validation_agent(

        user_query=state["question"],

        validation_context=state[
            "validation_context"
        ],

        conversation_history=state.get(
            "conversation_history",
            []
        ),

        intent_state=state.get(
            "intent_state",
            {}
        )

    )

    return response

# =========================================
# SCHEMA LOADER NODE
# =========================================

def schema_node(state):

    schema = schema_loader()

    return {

        "schema": schema

    }

# =========================================
# SQL RAG NODE
# =========================================

def rag_node(state):

    rag_context = retrieve_context(

        state["final_refined_query"]

    )

    return {

        "rag_context": rag_context

    }

# =========================================
# SQL GENERATION NODE
# =========================================

def sql_node(state):

    generated_sql = generate_sql(

        question=state[
            "final_refined_query"
        ],

        schema=state["schema"],

        rag_context=state["rag_context"]

    )

    return {

        "generated_sql": generated_sql

    }

# =========================================
# SQL VALIDATION NODE
# =========================================

def validation_node(state):

    validation_result = validate_sql(

        state["generated_sql"]

    )

    # return {

    #     "is_valid":

    #     validation_result["valid"],

    #     "validation_reason":

    #     validation_result["reason"]

    # }
    return {

    "is_valid":

    validation_result.get(

        "valid",

        True

    ),

    "validation_reason":

    validation_result.get(

        "reason",

        "Validation complete."

    ),

    "is_query_actionable":

    validation_result.get(

        "is_query_actionable",

        False

    ),

    "confidence_score":

    validation_result.get(

        "confidence_score",

        0.0

    ),

    "needs_clarification":

    validation_result.get(

        "needs_clarification",

        False

    ),

    "clarification_question":

    validation_result.get(

        "clarification_question",

        ""

    ),

    "final_refined_query":

    validation_result.get(

        "final_refined_query",

        ""

    ),

    "updated_intent_state":

    validation_result.get(

        "updated_intent_state",

        {}

    )}

# =========================================
# QUERY EXECUTION NODE
# =========================================

def execution_node(state):

    result = execute_query(

        sql_query=state["generated_sql"],

        schema=state["schema"]

    )

    return {

        "query_result": result

    }

# =========================================
# EXPORT NODE
# =========================================

def export_node(state):

    result = state["query_result"]

    if isinstance(result, str):

        return {

            "export_path":

            "Export skipped."

        }

    export_path = export_to_csv(

        result

    )

    return {

        "export_path": export_path

    }

# =========================================
# CLARIFICATION NODE
# =========================================

def clarification_node(state):

    return {

        "query_result":

        state["clarification_question"]

    }

# =========================================
# BLOCKED NODE
# =========================================

def blocked_node(state):

    return {

        "query_result":

        "I'm sorry, I can only help "
        "with business analytics "
        "and reporting queries."

    }