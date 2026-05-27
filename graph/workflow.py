# # =========================================
# # LANGGRAPH IMPORTS
# # =========================================

# from langgraph.graph import StateGraph

# # =========================================
# # IMPORT STATE
# # =========================================

# from graph.state import AgentState

# # =========================================
# # IMPORT NODES
# # =========================================

# from graph.nodes import (

#     preprocess_node,

#     schema_node,

#     rag_node,

#     sql_node,

#     validation_node,

#     execution_node,

#     export_node,

#     blocked_node

# )

# # =========================================
# # CREATE GRAPH
# # =========================================

# builder = StateGraph(AgentState)

# # =========================================
# # ADD NODES
# # =========================================

# builder.add_node(

#     "preprocess",

#     preprocess_node

# )

# builder.add_node(

#     "schema",

#     schema_node

# )

# builder.add_node(

#     "rag",

#     rag_node

# )

# builder.add_node(

#     "sql_generation",

#     sql_node

# )

# builder.add_node(

#     "validation",

#     validation_node

# )

# builder.add_node(

#     "execution",

#     execution_node

# )

# builder.add_node(

#     "export",

#     export_node

# )

# builder.add_node(

#     "blocked",

#     blocked_node

# )

# # =========================================
# # ADD EDGES
# # =========================================

# builder.add_edge(

#     "preprocess",

#     "schema"

# )

# builder.add_edge(

#     "schema",

#     "rag"

# )

# builder.add_edge(

#     "rag",

#     "sql_generation"

# )

# builder.add_edge(

#     "sql_generation",

#     "validation"

# )

# # =========================================
# # VALIDATION ROUTER
# # =========================================

# def validation_router(state):

#     if state["is_valid"]:

#         return "execution"

#     return "blocked"

# # =========================================
# # CONDITIONAL ROUTING
# # =========================================

# builder.add_conditional_edges(

#     "validation",

#     validation_router,

#     {

#         "execution": "execution",

#         "blocked": "blocked"

#     }

# )

# # =========================================
# # CONTINUE AFTER EXECUTION
# # =========================================

# builder.add_edge(

#     "execution",

#     "export"

# )

# # =========================================
# # ENTRY POINT
# # =========================================

# builder.set_entry_point(

#     "preprocess"

# )

# # =========================================
# # COMPILE GRAPH
# # =========================================

# graph = builder.compile()
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

    validation_rag_node,

    validation_agent_node,

    clarification_node,

    schema_node,

    rag_node,

    sql_node,

    validation_node,

    execution_node,

    export_node,

    blocked_node

)

# =========================================
# CREATE GRAPH
# =========================================

builder = StateGraph(AgentState)

# =========================================
# ADD NODES
# =========================================

builder.add_node(

    "preprocess",

    preprocess_node

)

builder.add_node(

    "validation_rag",

    validation_rag_node

)

builder.add_node(

    "validation_agent",

    validation_agent_node

)

builder.add_node(

    "clarification",

    clarification_node

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

    "validation_rag"

)

builder.add_edge(

    "validation_rag",

    "validation_agent"

)

# =========================================
# VALIDATION AGENT ROUTER
# =========================================

def clarification_router(state):

    if not state["is_relevant"]:

        return "blocked"

    if state["needs_clarification"]:

        return "clarification"

    return "schema"

# =========================================
# CONDITIONAL ROUTING
# =========================================

builder.add_conditional_edges(

    "validation_agent",

    clarification_router,

    {

        "schema": "schema",

        "clarification": "clarification",

        "blocked": "blocked"

    }

)

# =========================================
# SQL FLOW
# =========================================

builder.add_edge(

    "schema",

    "rag"

)

builder.add_edge(

    "rag",

    "sql_generation"

)

builder.add_edge(

    "sql_generation",

    "validation"

)

# =========================================
# SQL VALIDATION ROUTER
# =========================================

def validation_router(state):

    if state["is_valid"]:

        return "execution"

    return "blocked"

builder.add_conditional_edges(

    "validation",

    validation_router,

    {

        "execution": "execution",

        "blocked": "blocked"

    }

)

# =========================================
# FINAL FLOW
# =========================================

builder.add_edge(

    "execution",

    "export"

)

# =========================================
# ENTRY
# =========================================

builder.set_entry_point(

    "preprocess"

)

# =========================================
# FINISH POINTS
# =========================================

builder.set_finish_point(

    "export"

)

builder.set_finish_point(

    "clarification"

)

builder.set_finish_point(

    "blocked"

)

# =========================================
# COMPILE
# =========================================

graph = builder.compile()