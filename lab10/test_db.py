import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345"
    )
    print("Connected")
except Exception as e:
    print("Error:", e)



    # psql -U postgres -d lab10