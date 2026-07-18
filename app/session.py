current_user = None

def set_session(user):
    global current_user
    current_user = user
    
def get_session():
    if current_user is None:
        print("No user is logged in.")
    else:
        return current_user

def clear_session():
    global current_user
    current_user = None