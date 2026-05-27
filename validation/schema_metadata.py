from sqlalchemy import text

from database.connection import get_db

# =========================================
# EXTRACT DATABASE METADATA
# =========================================

def extract_metadata():

    engine = get_db()

    metadata_docs = []

    # =====================================
    # GET ALL TABLES
    # =====================================

    tables_query = """

    SELECT TABLE_NAME

    FROM INFORMATION_SCHEMA.TABLES

    WHERE TABLE_TYPE = 'BASE TABLE'

    """

    with engine.connect() as conn:

        tables = conn.execute(

            text(tables_query)

        ).fetchall()

        # =================================
        # LOOP THROUGH TABLES
        # =================================

        for table in tables:

            table_name = table[0]

            # =============================
            # GET COLUMNS
            # =============================

            columns_query = f"""

            SELECT

                COLUMN_NAME,

                DATA_TYPE

            FROM INFORMATION_SCHEMA.COLUMNS

            WHERE TABLE_NAME = '{table_name}'

            """

            columns = conn.execute(

                text(columns_query)

            ).fetchall()

            column_descriptions = []

            for col in columns:

                column_descriptions.append(

                    f"{col[0]} ({col[1]})"

                )

            # =============================
            # GET SAMPLE VALUES
            # =============================

            sample_values = []

            try:

                sample_query = f"""

                SELECT TOP 3 *

                FROM {table_name}

                """

                sample_rows = conn.execute(

                    text(sample_query)

                ).fetchall()

                for row in sample_rows:

                    sample_values.append(

                        str(row)

                    )

            except Exception:

                pass

            # =============================
            # CREATE METADATA DOCUMENT
            # =============================

            doc = f"""

            ====================================
            TABLE: {table_name}
            ====================================

            COLUMNS:
            {", ".join(column_descriptions)}

            SAMPLE ROWS:
            {" | ".join(sample_values)}

            """

            metadata_docs.append(doc)

    return metadata_docs

# =========================================
# TEST
# =========================================

if __name__ == "__main__":

    docs = extract_metadata()

    for doc in docs:

        print(doc)

        print("\n")