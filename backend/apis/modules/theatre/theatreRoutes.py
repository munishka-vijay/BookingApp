from flask import jsonify, request


from . import theatreControllers



from flask import Blueprint

theatre_api = Blueprint('theatre_api', __name__)


import sys
import os

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *


# For adding new theatre
@theatre_api.route('/', methods=['POST'])
def add_route():
    try:
        # Follow business logic for authentication
        theatre_info = request.get_json()
        theatre_data = theatreControllers.add_control(theatre_info)

        if 'error' in theatre_data:
            error = theatre_data['error']
            return jsonify(error), 400

        return jsonify(theatre_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# For getting all theatre
@theatre_api.route('/', methods=['GET'])
def getall_route():
    try:
        
        theatre_data = theatreControllers.getall_control()

        if 'error' in theatre_data:
            error = theatre_data['error']
            return jsonify(error), 400

        return jsonify(theatre_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

# To find theatre by location
@theatre_api.route('/location/<string:location>', methods=['GET'])
def findbylocation_route(location):
    try:
        
        theatre_data = theatreControllers.findbylocation_control(location)

        if 'error' in theatre_data:
            error = theatre_data['error']
            return jsonify(error), 400

        return jsonify(theatre_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

# To delete theatre by id
@theatre_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        theatre_data = theatreControllers.deleteTheatreById_control(id)

        if 'error' in theatre_data:
            error = theatre_data['error']
            return jsonify(error), 400

        return jsonify(theatre_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

# To get theatre by id
@theatre_api.route('/<int:id>', methods=['GET'])
def get(id):
    try:
        theatre_data = theatreControllers.getTheatreById_control(id)

        if 'error' in theatre_data:
            error = theatre_data['error']
            return jsonify(error), 400

        return jsonify(theatre_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

#update theatre
@theatre_api.route('/', methods=['PUT'])
def update():
    try:
        # Follow business logic for authentication
        theatre_info = request.get_json()
        theatre_data = theatreControllers.update_control(theatre_info)

        if 'error' in theatre_data:
            error = theatre_data['error']
            return jsonify(error), 400

        return jsonify(theatre_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500




