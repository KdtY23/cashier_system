from app.database.connection import get_database_connection
from app.models.role import get_role_by_id
from app.utils.hashing import hash_password
from app.services.auth_service import login
from app.session import get_session


def start_program():
 while True:
  get_database_connection()
  try:
    if not get_session():
        print('you have to login first')
        login()
    else:
        print('Login successful')
        break
  except Exception as e:
    print('looks like we cant find your account. Try again')
    continue
      
      
try:
    start_program()
except Exception as e:
    print('looks like we cant find your account. Try again')
    start_program()
    
lagi = input('wanna do something else? (y/n)')

if lagi != 'y':
    print('Goodbye!')
    input('Press Enter to exit...')
    exit()
else:
    print('Okay, let\'s start again!')
    start_program()
    