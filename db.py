import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="test2",
        user="amangoyal",
        password=""
    )
