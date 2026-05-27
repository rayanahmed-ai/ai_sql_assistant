
import sqlparse

# =========================================
# VALIDATE SQL
# =========================================

def validate_sql(sql_query):

    sql_upper = sql_query.upper()

    blocked = [

        "INSERT",

        "UPDATE",

        "DELETE",

        "DROP",

        "ALTER",

        "TRUNCATE"

    ]

    for keyword in blocked:

        if keyword in sql_upper:

            return {

                "valid": False,

                "reason":

                f"Blocked dangerous keyword: {keyword}"

            }

    parsed = sqlparse.parse(sql_query)

    if not parsed:

        return {

            "valid": False,

            "reason": "Invalid SQL syntax"

        }

    return {

        "valid": True,

        "reason": "Safe SELECT query."

    }
