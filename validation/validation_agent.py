from groq import Groq
import json
import os

from dotenv import load_dotenv

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# GROQ CLIENT
# =========================================

client = Groq(

    api_key=os.getenv("GROQ_API_KEY")

)

# =========================================
# VALIDATION AGENT
# =========================================

def validation_agent(

    user_query,

    validation_context,

    conversation_history,

    intent_state

):

#     prompt = f"""

#     You are an enterprise BI validation agent.

#     =====================================
#     DATABASE CONTEXT
#     =====================================

#     {validation_context}

#     =====================================
#     CONVERSATION HISTORY
#     =====================================

#     {conversation_history}

#     =====================================
#     CURRENT INTENT STATE
#     =====================================

#     {intent_state}

#     =====================================
#     USER QUERY
#     =====================================

#     {user_query}

#     =====================================
#     YOUR JOB
#     =====================================

#     1. Understand the user's business intent

#     2. Update the intent state

#     3. Detect missing requirements

#     4. Ask ONLY ONE clarification question

#     5. If user response is vague,
#        ask again more specifically

#     6. If user changes topic,
#        rebuild intent state

#     7. If complete,
#        generate FINAL_REFINED_QUERY

#     8. Reject unrelated queries
#        like celebrities, movies, sports

#     =====================================
#     IMPORTANT
#     =====================================

#     - DO NOT generate SQL

#     - DO NOT hallucinate schema

#     - ONLY ask one question at a time

#     - Every response from the user
#       may change the intent completely

#     Ask clarification questions ONLY when
#     the missing information would significantly
#     change the generated SQL query.

#     If a reasonable SQL query can already
#     be generated safely,
#     DO NOT ask more questions.

#     Optional filters such as:
#     - region
#     - branch
#     - status
#     - customer category

#     should NOT be mandatory unless the user
#     explicitly implies them.

#     Stop clarification once the query
#     is sufficiently actionable.

#     Determine whether the query is
#     sufficiently actionable to generate
#     a meaningful SQL query.

#     Also generate a confidence score
#     between 0 and 1.

#     Confidence should represent:
#     - clarity of business intent
#     - completeness of semantic meaning
#     - ability to generate safe SQL

#     If confidence is high enough,
#     DO NOT ask clarification questions.

#     Only ask clarification when ambiguity
#     would significantly change SQL meaning.

#     =====================================
#     RESPONSE FORMAT
#     =====================================

#     RELEVANT: YES or NO

#     IS_QUERY_ACTIONABLE: YES or NO

#     CONFIDENCE_SCORE:
#     float between 0 and 1

#     NEEDS_CLARIFICATION: YES or NO

#     CLARIFICATION_QUESTION:
#     question or NONE

#     FINAL_REFINED_QUERY:
#     query or NONE

#     UPDATED_INTENT_STATE:
#     valid JSON only

#     MISSING_REQUIREMENTS:
#     valid JSON list only

#     """
    prompt = f"""

    You are an enterprise BI validation agent.

    =====================================
    DATABASE CONTEXT
    =====================================

    {validation_context}

    =====================================
    CONVERSATION HISTORY
    =====================================

    {conversation_history}

    =====================================
    CURRENT INTENT STATE
    =====================================

    {intent_state}

    =====================================
    USER QUERY
    =====================================

    {user_query}

    =====================================
    YOUR ROLE
    =====================================

    You are responsible for:

    1. Understanding the user's business intent

    2. Detecting whether the request is:
    - complete
    - incomplete
    - ambiguous
    - unrelated

    3. Updating the intent state

    4. Asking ONLY ONE clarification question
    when absolutely necessary

    5. Generating a refined business query
    when enough information exists

    6. Rejecting unrelated questions
    such as:
    - celebrities
    - movies
    - sports
    - politics
    - general chit-chat

    =====================================
    IMPORTANT RULES
    =====================================

    - DO NOT generate SQL

    - DO NOT hallucinate schema

    - ONLY ask one clarification question
    at a time

    - Every user response may change
    the intent completely

    - Before asking clarification questions,
    carefully check whether the user has
    already provided the required information
    explicitly or implicitly

    Examples:

    - "May 2025" already includes:
    month + year

    - "last year" already defines:
    a valid time period

    - "region-wise sales" already defines:
    grouping by region

    - "monthly sales" already defines:
    monthly aggregation

    DO NOT ask for information
    that already exists in the query.

    =====================================
    ACTIONABILITY RULE
    =====================================

    Determine whether the query is
    sufficiently actionable to generate
    a meaningful SQL query safely.

    A query is ACTIONABLE if:

    - a reasonable SQL query can already
    be generated safely

    - the business meaning is clear enough

    - the missing information would NOT
    significantly change SQL meaning

    If the query is already actionable:

    DO NOT ask clarification questions.

    =====================================
    CLARIFICATION RULE
    =====================================

    ONLY ask clarification questions if:

    - ambiguity significantly changes
    SQL meaning

    - business intent is unclear

    - aggregation target is unclear

    - grouping meaning is unclear

    - the requested report cannot be safely
    generated

    Optional filters such as:

    - region
    - branch
    - status
    - customer category
    - product category

    should NOT be mandatory unless the user
    explicitly implies them.

    =====================================
    CONFIDENCE SCORE
    =====================================

    Generate a confidence score
    between 0 and 1.

    Confidence should represent:

    - clarity of business intent
    - completeness of semantic meaning
    - confidence in safe SQL generation

    Examples:

    0.95 = highly actionable

    0.80 = actionable with small ambiguity

    0.50 = partially ambiguous

    0.20 = highly unclear

    =====================================
    SPECIAL CASES
    =====================================

    If the user changes topic completely:

    - discard previous intent state

    - rebuild intent understanding

    If the user gives vague clarification:

    ask a more specific follow-up question.

    =====================================
    RESPONSE FORMAT
    =====================================

    RELEVANT: YES or NO

    IS_QUERY_ACTIONABLE: YES or NO

    CONFIDENCE_SCORE:
    float between 0 and 1

    NEEDS_CLARIFICATION: YES or NO

    CLARIFICATION_QUESTION:
    question or NONE

    FINAL_REFINED_QUERY:
    query or NONE

    UPDATED_INTENT_STATE:
    valid JSON only

    MISSING_REQUIREMENTS:
    valid JSON list only

    =====================================
    EXAMPLES
    =====================================

    Example 1:

    User:
    "Show total sales for May 2025"

    Response:

    RELEVANT: YES

    IS_QUERY_ACTIONABLE: YES

    CONFIDENCE_SCORE:
    0.97

    NEEDS_CLARIFICATION: NO

    CLARIFICATION_QUESTION:
    NONE

    FINAL_REFINED_QUERY:
    Show total sales for May 2025

    UPDATED_INTENT_STATE:
    {{

    "metric": "sales",

    "aggregation": "total",

    "time_period": "May 2025"

    }}

    MISSING_REQUIREMENTS:
    []

    =====================================

    Example 2:

    User:
    "Show performance"

    Response:

    RELEVANT: YES

    IS_QUERY_ACTIONABLE: NO

    CONFIDENCE_SCORE:
    0.31

    NEEDS_CLARIFICATION: YES

    CLARIFICATION_QUESTION:
    What type of performance would you like to analyze?

    FINAL_REFINED_QUERY:
    NONE

    UPDATED_INTENT_STATE:
    {{}}

    MISSING_REQUIREMENTS:
    ["metric"]

    =====================================

    Now analyze the current user query.

    """
    # =====================================
    # GROQ RESPONSE
    # =====================================

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {

                "role": "user",

                "content": prompt

            }

        ],

        temperature=0

    )

    output = (

        response.choices[0]

        .message.content

    )

    print(output)

    # =====================================
    # DEFAULT VALUES
    # =====================================

    relevant = False

    is_query_actionable = False

    confidence_score = 0.0

    needs_clarification = False

    clarification_question = ""

    final_refined_query = ""

    updated_intent_state = {}

    missing_requirements = []

    # =====================================
    # PARSE RELEVANT
    # =====================================

    if "RELEVANT: YES" in output:

        relevant = True

    # =====================================
    # PARSE ACTIONABILITY
    # =====================================

    if "IS_QUERY_ACTIONABLE: YES" in output:

        is_query_actionable = True

    # =====================================
    # PARSE CONFIDENCE SCORE
    # =====================================

    try:

        confidence_text = (

            output.split(

                "CONFIDENCE_SCORE:"

            )[-1]

            .split(

                "NEEDS_CLARIFICATION:"

            )[0]

            .strip()

        )

        confidence_score = float(

            confidence_text

        )

    except:

        confidence_score = 0.0

    # =====================================
    # PARSE CLARIFICATION
    # =====================================

    if "NEEDS_CLARIFICATION: YES" in output:

        needs_clarification = True

    # =====================================
    # PARSE QUESTION
    # =====================================

    try:

        clarification_question = (

            output.split(

                "CLARIFICATION_QUESTION:"

            )[-1]

            .split(

                "FINAL_REFINED_QUERY:"

            )[0]

            .strip()

        )

    except:

        clarification_question = ""

    # =====================================
    # PARSE FINAL QUERY
    # =====================================

    try:

        final_refined_query = (

            output.split(

                "FINAL_REFINED_QUERY:"

            )[-1]

            .split(

                "UPDATED_INTENT_STATE:"

            )[0]

            .strip()

        )

    except:

        final_refined_query = ""

    # =====================================
    # PARSE INTENT STATE
    # =====================================

    try:

        intent_text = (

            output.split(

                "UPDATED_INTENT_STATE:"

            )[-1]

            .split(

                "MISSING_REQUIREMENTS:"

            )[0]

            .strip()

        )

        updated_intent_state = json.loads(

            intent_text

        )

    except:

        updated_intent_state = {}

    # =====================================
    # PARSE MISSING REQUIREMENTS
    # =====================================

    try:

        missing_text = (

            output.split(

                "MISSING_REQUIREMENTS:"

            )[-1]

            .strip()

        )

        missing_requirements = json.loads(

            missing_text

        )

    except:

        missing_requirements = []

    # =====================================
    # SAFETY OVERRIDE
    # =====================================

    if (

        is_query_actionable

        and confidence_score >= 0.75

    ):

        needs_clarification = False

    # =====================================
    # RETURN STRUCTURED RESPONSE
    # =====================================

    return {

        "is_relevant":

        relevant,

        "is_query_actionable":

        is_query_actionable,

        "confidence_score":

        confidence_score,

        "needs_clarification":

        needs_clarification,

        "clarification_question":

        clarification_question,

        "final_refined_query":

        final_refined_query,

        "updated_intent_state":

        updated_intent_state,

        "missing_requirements":

        missing_requirements

    }