from database import db
from .userModel import User
import os, sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *

#Check if user already exists
def find_user_by_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        if user:
            return {
                'success': True,
                'data': user,
            }

        raise Exception(ERROR_MESSAGES["USER_NOT_FOUND"])
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }

def find_all_users():
    try:
        return User.query.all()
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }


#add new user
def add_user(username, email, phone, password):
    try:
        new_user = User(username=username, email=email, phone=phone, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }