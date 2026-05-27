# =========================================
# LANGGRAPH IMPORTS
# =========================================

from langgraph.graph import StateGraph

# =========================================
# IMPORT STATE
# =========================================

from graph.state import AgentState

# =========================================
# IMPORT NODES
# =========================================

from graph.nodes import (

    preprocess_node,

    schema_node,

    rag_node,

    validation_rag_node,

    clarification_node,

    sql_node,

    validation_node,

    execution_node,

    export_node,

    blocked_node

)

# =========================================
# CREATE GRAPH
# =========================================

builder = StateGraph(

    AgentState

)

# =========================================
# ADD NODES
# =========================================

builder.add_node(

    "preprocess",

    preprocess_node

)

builder.add_node(

    "schema",

    schema_node

)

builder.add_node(

    "rag",

    rag_node

)

builder.add_node(

    "validation_rag",

    validation_rag_node

)

builder.add_node(

    "clarification",

    clarification_node

)

builder.add_node(

    "sql_generation",

    sql_node

)

builder.add_node(

    "validation",

    validation_node

)

builder.add_node(

    "execution",

    execution_node

)

builder.add_node(

    "export",

    export_node

)

builder.add_node(

    "blocked",

    blocked_node

)

# =========================================
# ADD EDGES
# =========================================

builder.add_edge(

    "preprocess",

    "schema"

)

builder.add_edge(

    "schema",

    "rag"

)

builder.add_edge(

    "rag",

    "validation_rag"

)

builder.add_edge(

    "validation_rag",

    "clarification"

)

# =========================================
# CLARIFICATION ROUTER
# =========================================

def clarification_router(state):

    # =====================================
    # IRRELEVANT QUERY
    # =====================================

    if not state.get(

        "is_relevant",

        True

    ):

        return "blocked"

    # =====================================
    # NEEDS CLARIFICATION
    # =====================================

    if (

        state.get(

            "needs_clarification",

            False

        )

        and

        not state.get(

            "is_query_actionable",

            False

        )

        and

        state.get(

            "confidence_score",

            0

        ) < 0.75

    ):

        return "blocked"

    # =====================================
    # ACTIONABLE QUERY
    # =====================================

    return "sql_generation"

# =========================================
# CONDITIONAL ROUTING
# =========================================

builder.add_conditional_edges(

    "clarification",

    clarification_router,

    {

        "sql_generation":

        "sql_generation",

        "blocked":

        "blocked"

    }

)

# =========================================
# SQL VALIDATION FLOW
# =========================================

builder.add_edge(

    "sql_generation",

    "validation"

)

# =========================================
# VALIDATION ROUTER
# =========================================

def validation_router(state):

    if state["is_valid"]:

        return "execution"

    return "blocked"

# =========================================
# CONDITIONAL ROUTING
# =========================================

builder.add_conditional_edges(

    "validation",

    validation_router,

    {

        "execution":

        "execution",

        "blocked":

        "blocked"

    }

)

# =========================================
# CONTINUE AFTER EXECUTION
# =========================================

builder.add_edge(

    "execution",

    "export"

)

# =========================================
# ENTRY POINT
# =========================================

builder.set_entry_point(

    "preprocess"

)

# =========================================
# COMPILE GRAPH
# =========================================

graph = builder.compile()