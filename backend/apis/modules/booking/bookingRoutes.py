from flask import jsonify, request

from . import bookingControllers


from flask import Blueprint

booking_api = Blueprint('booking_api', __name__)

import sys
import os

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *


# For adding new booking
@booking_api.route('/', methods=['POST'])
def add_route():
    try:
        # Follow business logic for authentication
        booking_info = request.get_json()
        booking_data = bookingControllers.add_control(booking_info)

        if 'error' in booking_data:
            error = booking_data['error']
            return jsonify(error), 400

        return jsonify(booking_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# To find booking by user_id
@booking_api.route('/user/<int:id>', methods=['GET'])
def findbyrating_route(id):
    try:
        booking_data = bookingControllers.findbyUserId_control(id)

        if 'error' in booking_data:
            error = booking_data['error']
            return jsonify(error), 400

        return jsonify(booking_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500