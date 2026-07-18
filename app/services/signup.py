from app.database.connection import get_database_connection
from app.models.role import get_role_by_id

def signup(requester_role, username, password, full_name, target_role):
    role = get_role_by_id(requester_role)
    