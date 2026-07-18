import psycopg

def get_database_connection():
    try:
        conn = psycopg.connect(
            host="localhost",
            port=5432,
            dbname="cashier-system-database",
            user="postgres",
            password="6614ZY5258ZI"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None