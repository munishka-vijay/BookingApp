from flask import jsonify, request

from . import showControllers


from flask import Blueprint

show_api = Blueprint('show_api', __name__)

import sys
import os

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *


# For adding new show
@show_api.route('/', methods=['POST'])
def add_route():
    try:
        # Follow business logic for authentication
        show_info = request.get_json()
        show_data = showControllers.add_control(show_info)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# For getting all show
@show_api.route('/', methods=['GET'])
def getall_route():
    try:
        
        show_data = showControllers.getall_control()

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

# To get show by id
@show_api.route('/<int:id>', methods=['GET'])
def get(id):
    try:
        show_data = showControllers.getShowById_control(id)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# To delete show by id
@show_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        show_data = showControllers.deleteShowById_control(id)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

#update show
@show_api.route('/', methods=['PUT'])
def update():
    try:
        # Follow business logic for authentication
        show_info = request.get_json()
        show_data = showControllers.update_control(show_info)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# To find show by tag
@show_api.route('/tag/<string:tag>', methods=['GET'])
def findbytag_route(tag):
    try:
        show_data = showControllers.findbytag_control(tag)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

# To find show by language
@show_api.route('/language/<string:language>', methods=['GET'])
def findbylanguage_route(language):
    try:
        show_data = showControllers.findbylanguage_control(language)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# To find show by rating
@show_api.route('/rating/<float:rating>', methods=['GET'])
def findbyrating_route(rating):
    try:
        show_data = showControllers.findbyrating_control(rating)

        if 'error' in show_data:
            error = show_data['error']
            return jsonify(error), 400

        return jsonify(show_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500






