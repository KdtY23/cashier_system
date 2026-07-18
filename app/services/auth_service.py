from app.models.users import get_user_by_id
from app.utils.hashing import check_password
from app.database.connection import get_database_connection
from app.session import set_session
from app.models.role import get_role_by_id

def login():
  while True:
    id = input("Enter your ID: ")
    password = input("Enter your password: ")
    
    conn = get_database_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT id,username, password, role_id FROM users
        WHERE id=%s
        """,
        (id,)
    )
    
    
    user = cursor.fetchone()
    role_name = get_role_by_id(user[3])
    cursor.close()
    conn.close()
    if user:
        print(f"User {user[1]} logged in successfully as {role_name}")
    
        set_session({
            "id": user[0],
            "username": user[1],
            "role_id": user[3],
        })
        return True
    else:
        print('ID or password is incorrect')
        response = input('Do you want to try again? (y/n): ')
        if response == 'y':
            login()
            return False