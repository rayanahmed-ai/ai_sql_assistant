# =========================================
# IMPORT FUNCTIONS
# =========================================

from nlp.spacy_processor import query_processor

from database.schema_loader import schema_loader

from rag.retriever import retrieve_context

from validation.validation_retriever import (

    retrieve_validation_context

)

from validation.validation_agent import (

    validation_agent

)

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
# VALIDATION RAG NODE
# =========================================

def validation_rag_node(state):

    validation_context = (

        retrieve_validation_context(

            state["cleaned_query"]

        )

    )

    return {

        "validation_context":

        validation_context

    }

# =========================================
# VALIDATION / CLARIFICATION NODE
# =========================================

def clarification_node(state):

    clarification_result = validation_agent(

        user_query=state["cleaned_query"],

        validation_context=

        state["validation_context"],

        conversation_history=

        state.get(

            "conversation_history",

            []

        ),

        intent_state=

        state.get(

            "intent_state",

            {}

        )

    )

    return {

        "is_relevant":

        clarification_result.get(

            "is_relevant",

            True

        ),

        "is_query_actionable":

        clarification_result.get(

            "is_query_actionable",

            False

        ),

        "confidence_score":

        clarification_result.get(

            "confidence_score",

            0.0

        ),

        "needs_clarification":

        clarification_result.get(

            "needs_clarification",

            False

        ),

        "clarification_question":

        clarification_result.get(

            "clarification_question",

            ""

        ),

        "final_refined_query":

        clarification_result.get(

            "final_refined_query",

            state["cleaned_query"]

        ),

        "updated_intent_state":

        clarification_result.get(

            "updated_intent_state",

            {}

        ),

        "missing_requirements":

        clarification_result.get(

            "missing_requirements",

            []

        )

    }

# =========================================
# SQL GENERATION NODE
# =========================================

def sql_node(state):

    generated_sql = generate_sql(

        question=state.get(

            "final_refined_query",

            state["cleaned_query"]

        ),

        schema=state["schema"],

        rag_context=state["rag_context"]

    )

    return {

        "generated_sql":

        generated_sql

    }

# =========================================
# SQL VALIDATION NODE
# =========================================

def validation_node(state):

    validation_result = validate_sql(

        state["generated_sql"]

    )

    return {

        "is_valid":

        validation_result.get(

            "valid",

            True

        ),

        "validation_reason":

        validation_result.get(

            "reason",

            "SQL validated."

        )

    }

# =========================================
# QUERY EXECUTION NODE
# =========================================

def execution_node(state):

    result = execute_query(

        sql_query=state["generated_sql"],

        schema=state["schema"]

    )

    return {

        "query_result":

        result

    }

# =========================================
# EXPORT NODE
# =========================================

def export_node(state):

    result = state["query_result"]

    # =====================================
    # SKIP EXPORT ON ERROR
    # =====================================

    if isinstance(

        result,

        str

    ):

        return {

            "export_path":

            "Export skipped due to execution error."

        }

    export_path = export_to_csv(

        result

    )

    return {

        "export_path":

        export_path

    }

# =========================================
# BLOCKED NODE
# =========================================

def blocked_node(state):

    # =====================================
    # CLARIFICATION RESPONSE
    # =====================================

    if state.get(

        "needs_clarification",

        False

    ):

        return {

            "query_result":

            state.get(

                "clarification_question",

                "Please clarify your request."

            )

        }

    # =====================================
    # IRRELEVANT QUERY
    # =====================================

    if not state.get(

        "is_relevant",

        True

    ):

        return {

            "query_result":

            "I'm sorry, I can only help "
            "with business analytics "
            "and reporting queries."

        }

    # =====================================
    # SQL VALIDATION FAILURE
    # =====================================

    return {

        "query_result":

        f"Blocked Query: "

        f"{state.get('validation_reason', 'Validation failed')}"

    }