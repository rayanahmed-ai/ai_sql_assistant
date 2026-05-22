# # # # =========================================
# # # # LANGGRAPH IMPORTS
# # # # =========================================

# # # from langgraph.graph import StateGraph

# # # # =========================================
# # # # IMPORT STATE
# # # # =========================================

# # # from graph.state import AgentState

# # # # =========================================
# # # # IMPORT NODES
# # # # =========================================

# # # from graph.nodes import (

# # #     preprocess_node,

# # #     schema_node,

# # #     rag_node,

# # #     sql_node,

# # #     validation_node,

# # #     execution_node,

# # #     export_node,

# # #     blocked_node

# # # )

# # # # =========================================
# # # # CREATE GRAPH
# # # # =========================================

# # # builder = StateGraph(AgentState)

# # # # =========================================
# # # # ADD NODES
# # # # =========================================

# # # builder.add_node(

# # #     "preprocess",

# # #     preprocess_node

# # # )

# # # builder.add_node(

# # #     "schema",

# # #     schema_node

# # # )

# # # builder.add_node(

# # #     "rag",

# # #     rag_node

# # # )

# # # builder.add_node(

# # #     "sql_generation",

# # #     sql_node

# # # )

# # # builder.add_node(

# # #     "validation",

# # #     validation_node

# # # )

# # # builder.add_node(

# # #     "execution",

# # #     execution_node

# # # )

# # # builder.add_node(

# # #     "export",

# # #     export_node

# # # )

# # # builder.add_node(

# # #     "blocked",

# # #     blocked_node

# # # )

# # # # =========================================
# # # # ADD EDGES
# # # # =========================================

# # # builder.add_edge(

# # #     "preprocess",

# # #     "schema"

# # # )

# # # builder.add_edge(

# # #     "schema",

# # #     "rag"

# # # )

# # # builder.add_edge(

# # #     "rag",

# # #     "sql_generation"

# # # )

# # # builder.add_edge(

# # #     "sql_generation",

# # #     "validation"

# # # )

# # # # =========================================
# # # # VALIDATION ROUTER
# # # # =========================================

# # # def validation_router(state):

# # #     if state["is_valid"]:

# # #         return "execution"

# # #     return "blocked"

# # # # =========================================
# # # # CONDITIONAL ROUTING
# # # # =========================================

# # # builder.add_conditional_edges(

# # #     "validation",

# # #     validation_router,

# # #     {

# # #         "execution": "execution",

# # #         "blocked": "blocked"

# # #     }

# # # )

# # # # =========================================
# # # # CONTINUE AFTER EXECUTION
# # # # =========================================

# # # builder.add_edge(

# # #     "execution",

# # #     "export"

# # # )

# # # # =========================================
# # # # ENTRY POINT
# # # # =========================================

# # # builder.set_entry_point(

# # #     "preprocess"

# # # )

# # # # =========================================
# # # # COMPILE GRAPH
# # # # =========================================

# # # graph = builder.compile()

# # # =========================================
# # # LANGGRAPH IMPORTS
# # # =========================================

# # from langgraph.graph import StateGraph, END

# # # =========================================
# # # IMPORT STATE
# # # =========================================

# # from graph.state import AgentState

# # # =========================================
# # # IMPORT NODES
# # # =========================================

# # from graph.nodes import (

# #     preprocess_node,

# #     clarification_node,

# #     schema_node,

# #     rag_node,

# #     sql_node,

# #     validation_node,

# #     execution_node,

# #     export_node,

# #     blocked_node

# # )

# # # =========================================
# # # CREATE GRAPH
# # # =========================================

# # builder = StateGraph(AgentState)

# # # =========================================
# # # ADD NODES
# # # =========================================

# # builder.add_node(

# #     "preprocess",

# #     preprocess_node

# # )

# # builder.add_node(

# #     "clarification",

# #     clarification_node

# # )

# # builder.add_node(

# #     "schema",

# #     schema_node

# # )

# # builder.add_node(

# #     "rag",

# #     rag_node

# # )

# # builder.add_node(

# #     "sql_generation",

# #     sql_node

# # )

# # builder.add_node(

# #     "validation",

# #     validation_node

# # )

# # builder.add_node(

# #     "execution",

# #     execution_node

# # )

# # builder.add_node(

# #     "export",

# #     export_node

# # )

# # builder.add_node(

# #     "blocked",

# #     blocked_node

# # )

# # # =========================================
# # # ADD EDGES
# # # =========================================

# # builder.add_edge(

# #     "preprocess",

# #     "clarification"

# # )

# # builder.add_edge(

# #     "schema",

# #     "rag"

# # )

# # builder.add_edge(

# #     "rag",

# #     "sql_generation"

# # )

# # builder.add_edge(

# #     "sql_generation",

# #     "validation"

# # )

# # # =========================================
# # # CLARIFICATION ROUTER
# # # =========================================

# # def clarification_router(state):

# #     if state["needs_clarification"]:

# #         return "stop"

# #     return "continue"

# # # =========================================
# # # CLARIFICATION CONDITIONAL FLOW
# # # =========================================

# # builder.add_conditional_edges(

# #     "clarification",

# #     clarification_router,

# #     {

# #         "stop": END,

# #         "continue": "schema"

# #     }

# # )

# # # =========================================
# # # VALIDATION ROUTER
# # # =========================================

# # def validation_router(state):

# #     if state["is_valid"]:

# #         return "execution"

# #     return "blocked"

# # # =========================================
# # # VALIDATION CONDITIONAL FLOW
# # # =========================================

# # builder.add_conditional_edges(

# #     "validation",

# #     validation_router,

# #     {

# #         "execution": "execution",

# #         "blocked": "blocked"

# #     }

# # )

# # # =========================================
# # # CONTINUE AFTER EXECUTION
# # # =========================================

# # builder.add_edge(

# #     "execution",

# #     "export"

# # )

# # # =========================================
# # # FINISH WORKFLOW
# # # =========================================

# # builder.add_edge(

# #     "export",

# #     END

# # )

# # builder.add_edge(

# #     "blocked",

# #     END

# # )

# # # =========================================
# # # ENTRY POINT
# # # =========================================

# # builder.set_entry_point(

# #     "preprocess"

# # )

# # # =========================================
# # # COMPILE GRAPH
# # # =========================================

# # graph = builder.compile()
# from langgraph.graph import StateGraph, END

# from graph.state import AgentState

# from graph.nodes import (

#     preprocess_node,

#     clarification_node,

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

# builder = StateGraph(

#     AgentState

# )

# # =========================================
# # ADD NODES
# # =========================================

# builder.add_node(

#     "preprocess",

#     preprocess_node

# )

# builder.add_node(

#     "clarification",

#     clarification_node

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
# # EDGES
# # =========================================

# builder.add_edge(

#     "preprocess",

#     "clarification"

# )

# # =========================================
# # CLARIFICATION ROUTER
# # =========================================

# def clarification_router(state):

#     if state["needs_clarification"]:

#         return "stop"

#     return "continue"

# builder.add_conditional_edges(

#     "clarification",

#     clarification_router,

#     {

#         "stop": END,

#         "continue": "schema"

#     }

# )

# # =========================================
# # MAIN FLOW
# # =========================================

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

# builder.add_conditional_edges(

#     "validation",

#     validation_router,

#     {

#         "execution": "execution",

#         "blocked": "blocked"

#     }

# )

# # =========================================
# # EXECUTION FLOW
# # =========================================

# builder.add_edge(

#     "execution",

#     "export"

# )

# # =========================================
# # END STATES
# # =========================================

# builder.add_edge(

#     "export",

#     END

# )

# builder.add_edge(

#     "blocked",

#     END

# )

# # =========================================
# # ENTRY POINT
# # =========================================

# builder.set_entry_point(

#     "preprocess"

# )

# # =========================================
# # COMPILE
# # =========================================

# graph = builder.compile()
# =========================================
# LANGGRAPH IMPORTS
# =========================================

from langgraph.graph import StateGraph, END

# =========================================
# IMPORT STATE
# =========================================

from graph.state import AgentState

# =========================================
# IMPORT NODES
# =========================================

from graph.nodes import (

    preprocess_node,

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
# ENTRY FLOW
# =========================================

builder.add_edge(

    "preprocess",

    "clarification"

)

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
# CLARIFICATION ROUTER
# =========================================

def clarification_router(state):

    if state.get(

        "needs_clarification",

        False

    ):

        return "stop"

    return "continue"

# =========================================
# CLARIFICATION CONDITIONAL FLOW
# =========================================

builder.add_conditional_edges(

    "clarification",

    clarification_router,

    {

        "stop": END,

        "continue": "schema"

    }

)

# =========================================
# VALIDATION ROUTER
# =========================================

def validation_router(state):

    if state["is_valid"]:

        return "execution"

    return "blocked"

# =========================================
# VALIDATION CONDITIONAL FLOW
# =========================================

builder.add_conditional_edges(

    "validation",

    validation_router,

    {

        "execution": "execution",

        "blocked": "blocked"

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
# FINISH WORKFLOW
# =========================================

builder.add_edge(

    "export",

    END

)

builder.add_edge(

    "blocked",

    END

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
