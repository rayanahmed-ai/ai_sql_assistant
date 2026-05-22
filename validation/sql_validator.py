# def validate_sql(query: str):

#     forbidden_keywords = [

#         "INSERT",
#         "UPDATE",
#         "DELETE",
#         "DROP",
#         "ALTER",
#         "TRUNCATE"

#     ]

#     query_upper = query.upper()

#     for keyword in forbidden_keywords:

#         if keyword in query_upper:

#             return False

#     return True
# =========================================
# VALIDATE GENERATED SQL
# =========================================

def validate_sql(query: str):

    forbidden_keywords = [

        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "TRUNCATE"

    ]

    query_upper = query.upper()

    for keyword in forbidden_keywords:

        if keyword in query_upper:

            return {

                "valid": False,

                "reason": f"{keyword} statements are not allowed."

            }

    return {

        "valid": True,

        "reason": "Safe SELECT query."

    }