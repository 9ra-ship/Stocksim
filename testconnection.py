import psycopg2

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        dbname="stocksim-db",
        user="postgres",
        password="stockproject",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print("Connection successful! PostgreSQL version:")
    print(cursor.fetchone())
    cursor.close()
    connection.close()
except Exception as e:
    print("Connection failed! Error:")
    print(e)