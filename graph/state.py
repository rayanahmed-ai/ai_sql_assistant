# from typing import TypedDict

# # =========================================
# # SHARED GRAPH STATE
# # =========================================

# class AgentState(TypedDict):

#     # =====================================
#     # USER INPUT
#     # =====================================

#     question: str

#     # =====================================
#     # NLP OUTPUT
#     # =====================================

#     cleaned_query: str

#     # =====================================
#     # DATABASE SCHEMA
#     # =====================================

#     schema: str

#     # =====================================
#     # RAG CONTEXT
#     # =====================================

#     rag_context: str

#     # =====================================
#     # GENERATED SQL
#     # =====================================

#     generated_sql: str

#     # =====================================
#     # VALIDATION
#     # =====================================

#     is_valid: bool

#     validation_reason: str

#     # =====================================
#     # QUERY RESULT
#     # =====================================

#     query_result: str

#     # =====================================
#     # EXPORT
#     # =====================================

#     export_path: str
from typing import TypedDict, Optional

import pandas as pd

# =========================================
# SHARED GRAPH STATE
# =========================================

class AgentState(TypedDict):

    # =====================================
    # USER INPUT
    # =====================================

    question: str

    cleaned_query: str

    # =====================================
    # VALIDATION LAYER
    # =====================================

    conversation_history: list

    intent_state: dict

    missing_requirements: list

    needs_clarification: bool

    clarification_question: str

    final_refined_query: str

    validation_context: str

    is_relevant: bool

    # =====================================
    # DATABASE SCHEMA
    # =====================================

    schema: str

    # =====================================
    # SQL RAG
    # =====================================

    rag_context: str

    # =====================================
    # GENERATED SQL
    # =====================================

    generated_sql: str

    # =====================================
    # SQL VALIDATION
    # =====================================

    is_valid: bool

    validation_reason: str
    is_query_actionable: bool

    confidence_score: float

    # =====================================
    # QUERY RESULT
    # =====================================

    query_result: Optional[pd.DataFrame]

    # =====================================
    # EXPORT
    # =====================================

    export_path: Optional[str]