from flask import jsonify, request

from . import userValidators
from . import userControllers

# from . import user_api

from flask import Blueprint

user_api = Blueprint('user_api', __name__)

# from .userRoutes import *

import sys
import os

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *


# For sign-up
@user_api.route('/signup', methods=['POST'])
def signup_route():
    try:

        # Validate request body
        validated = userValidators.signup_auth()
        if validated is not None: # Because None will be returned if there is no error
            if validated.get('error'):
                error = {
                    'message': ERROR_MESSAGES["INVALID_REQUEST"]
                    }
                return jsonify(error), 400

        # Follow business logic for authentication
        user_info = request.get_json()
        user_data = userControllers.signup_control(user_info)

        if 'error' in user_data:
            error = user_data['error']
            return jsonify(error), 400

        return jsonify(user_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# For login
@user_api.route('/login', methods=['POST'])
def login_route():
    try:
        # Validate request body
        validated = userValidators.login_auth()
        if validated is not None: 
            if validated.get('error'):
                error = {
                    'message': ERROR_MESSAGES["INVALID_REQUEST"]
                    }
                return jsonify(error), 400

        # Follow business logic for authentication
        user_info = request.get_json()
        user_data = userControllers.login_control(user_info)

        return jsonify(user_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500





