from app.database.connection import get_database_connection

def get_role_by_id(role_id):
    conn = get_database_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT name
        FROM roles
        WHERE id=%s
        """,
        (role_id,)
        
    )
    
    role = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return role
    