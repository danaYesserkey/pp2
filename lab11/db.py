import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="lab11",
        user="postgres",
        password="12345"
    )