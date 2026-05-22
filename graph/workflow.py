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

    "schema"

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
# ENTRY POINT
# =========================================

builder.set_entry_point(

    "preprocess"

)

# =========================================
# COMPILE GRAPH
# =========================================

graph = builder.compile()