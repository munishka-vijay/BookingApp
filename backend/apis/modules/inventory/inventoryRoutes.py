from flask import jsonify, request

from . import inventoryControllers

from flask import Blueprint

inventory_api = Blueprint('inventory_api', __name__)

import sys
import os
import json
from flask import current_app

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *


# For adding new inventory
@inventory_api.route('/', methods=['POST'])
def add_route():
    try:
        redis_connection = current_app.redis

        # Follow business logic for authentication
        inventory_info = request.get_json()
        inventory_data = inventoryControllers.add_control(inventory_info)
        inventorys= inventoryControllers.getall_control()
        serialized_list = json.dumps(inventorys)
        redis_connection.setex("inv", 3600, serialized_list)
        if 'error' in inventory_data:
            error = inventory_data['error']
            return jsonify(error), 400

        return jsonify(inventory_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# For getting all inventory
@inventory_api.route('/', methods=['GET'])
def getall_route():
    try:
      inventorys=[]
      redis_connection = current_app.redis
      if redis_connection.get("inv") is None:
        inventorys= inventoryControllers.getall_control()
        serialized_list = json.dumps(inventorys)
        redis_connection.setex("inv", 3600, serialized_list)
      else:
        inventorys=json.loads(redis_connection.get("inv"))

        if 'error' in inventorys:
            error = inventorys['error']
            return jsonify(error), 400

        return jsonify(inventorys), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# To delete inventory by id
@inventory_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        inventory_data = inventoryControllers.deleteInventoryById_control(id)

        if 'error' in inventory_data:
            error = inventory_data['error']
            return jsonify(error), 400

        return jsonify(inventory_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

#update inventory
@inventory_api.route('/', methods=['PUT'])
def update():
    try:
        # Follow business logic for authentication
        inventory_info = request.get_json()
        inventory_data = inventoryControllers.update_control(inventory_info)

        if 'error' in inventory_data:
            error = inventory_data['error']
            return jsonify(error), 400

        return jsonify(inventory_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500


# To find inventory by tateatre id
@inventory_api.route('/theatre/<int:theatreId>', methods=['GET'])
def findbytheatre_route(theatreId):
    try:
        inventory_data = inventoryControllers.findbyTheatreId_control(theatreId)

        if 'error' in inventory_data:
            error = inventory_data['error']
            return jsonify(error), 400

        return jsonify(inventory_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500



# To find inventory by show id
@inventory_api.route('/show/<int:showId>', methods=['GET'])
def findbyshow_route(showId):
    try:
        inventory_data = inventoryControllers.findbyShowId_control(showId)

        if 'error' in inventory_data:
            error = inventory_data['error']
            return jsonify(error), 400

        return jsonify(inventory_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

# To find inventory by start_time
@inventory_api.route('/start_time/<string:start_time>', methods=['GET'])
def findbytime_route(start_time):
    try:
        inventory_data = inventoryControllers.findbyStartTime_control(start_time)

        if 'error' in inventory_data:
            error = inventory_data['error']
            return jsonify(error), 400

        return jsonify(inventory_data), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500

        







