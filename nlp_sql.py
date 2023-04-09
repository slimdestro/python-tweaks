# simple implementation of npl2sql
# natural language input => sql query
# @slimdestro

# def init():
    # Load environment variables
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    # Create a nlp2sql object
    nlp2sql_obj = nlp2sql.NLP2SQL()

    # Load a database
    nlp2sql_obj.load_database(db_name, db_user, db_password)

    return nlp2sql_obj

def parser(nlp2sql_obj, query):
    # Parse a natural language query
    sql_query = nlp2sql_obj.parse(query)

    # Print the generated SQL query
    print(sql_query)