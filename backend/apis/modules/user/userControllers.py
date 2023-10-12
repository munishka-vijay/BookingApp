from . import userRepository
from flask import jsonify

import sys
import os

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now we can import the required module
from utils.errors import *
from utils.utils import *

def signup_control(user_info):
   try:
      user_exists = userRepository.find_user_by_username(user_info['username'])

      if user_exists['success']:
            error = {
                'message': ERROR_MESSAGES["USERNAME_TAKEN"]
            }
            return error         
        
      # Hash password
      hashedPassword = get_hashed_password(user_info['password'])
      
      # Save user to the database
      print("HI")
      userAdded = userRepository.add_user(user_info['username'], user_info['email'], user_info['phone'], hashedPassword)
      print(userAdded)
      # Generate JWT Token
      token = generate_jwt_token(userAdded.id, userAdded.username)
      return {
            '_id': userAdded.id,
            'username': userAdded.username,
            'token': token,
            'role':userAdded.role
        }
   except Exception as err:
        raise Exception(str(err))


def login_control(user_info):
    try:
        userExists = userRepository.find_user_by_username(user_info['username'])

        # Return error if user doesn't exist
        if not userExists['success']:
            raise Exception(ERROR_MESSAGES["AUTH_FAILED"])

        # Check if passwords match
        isPasswordCorrect = compare_hash(user_info['password'], userExists['data'].password)

        if not isPasswordCorrect:
            raise Exception(ERROR_MESSAGES["AUTH_FAILED"])

        # Generate JWT Token
        token = generate_jwt_token(userExists['data'].id, userExists['data'].username)

        return {
            '_id': userExists['data'].id,
            'username': userExists['data'].username,
            'token': token,
            'role':userExists['data'].role
        }

    except Exception as err:
        raise Exception(str(err))







    
