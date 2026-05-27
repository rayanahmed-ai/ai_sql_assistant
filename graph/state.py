from typing import TypedDict

# =========================================
# SHARED GRAPH STATE
# =========================================

class AgentState(TypedDict):

    # =====================================
    # USER INPUT
    # =====================================

    question: str

    # =====================================
    # CONVERSATION
    # =====================================

    conversation_history: list

    intent_state: dict

    # =====================================
    # NLP OUTPUT
    # =====================================

    cleaned_query: str

    # =====================================
    # DATABASE SCHEMA
    # =====================================

    schema: str

    # =====================================
    # RAG CONTEXT
    # =====================================

    rag_context: str

    validation_context: str

    # =====================================
    # VALIDATION AGENT
    # =====================================

    is_relevant: bool

    is_query_actionable: bool

    confidence_score: float

    needs_clarification: bool

    clarification_question: str

    final_refined_query: str

    updated_intent_state: dict

    missing_requirements: list

    # =====================================
    # GENERATED SQL
    # =====================================

    generated_sql: str

    # =====================================
    # SQL VALIDATION
    # =====================================

    is_valid: bool

    validation_reason: str

    # =====================================
    # QUERY RESULT
    # =====================================

    query_result: str

    # =====================================
    # EXPORT
    # =====================================

    export_path: str