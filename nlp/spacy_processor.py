# import spacy
# def query_processor(query):
#     nlp = spacy.load("en_core_web_sm")

#     # query = "Hi my name is Rayan and Give me the sales of Jack's products"

#     doc = nlp(query)
#     print(doc)
#     processed_query = " ".join(
#         [
#             token.text.lower()
#             for token in doc
            
#         ]
#     )

#     print(processed_query)
#     return processed_query
# import spacy

# # =========================================
# # LOAD SPACY MODEL ONCE
# # =========================================

# nlp = spacy.load(

#     "en_core_web_sm"

# )
# nlp = spacy.blank("en")

# =========================================
# QUERY PREPROCESSOR
# =========================================

def query_processor(query):

    # doc = nlp(query)

    # processed_query = " ".join(

    #     [

    #         token.lemma_.lower()

    #         for token in doc

    #         if not token.is_punct
    #         and not token.is_space

    #     ]

    # )
    return query.lower()