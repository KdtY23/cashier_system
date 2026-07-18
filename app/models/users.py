from app.database.connection import get_database_connection
from app.utils.hashing import hash_password

conn = get_database_connection()
cursor = conn.cursor()

def create_user(role_id, username, password, full_name):    
    hashed_password = hash_password(password)
    cursor.execute(
        """
        INSERT INTO users(
            role_id,
            username,
            password,
            full_name
        )
        VALUES(%s, %s, %s, %s)
        """,
        (
            role_id,
            username,
            hashed_password,
            full_name
        )
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    
def get_user_by_id(id):
    cursor.execute(
        """
        SELECT 
        id,
        password
        FROM users
        WHERE id=%s
        """
        (id,)
    )
    
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
    