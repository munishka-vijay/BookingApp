from . import theatreRepository
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

def add_control(theatre_info):
   try:
      
      # Save theatre to the database
      theatreAdded = theatreRepository.add_theatre(theatre_info['name'], theatre_info['location'], theatre_info['capacity'])

      return {
            '_id': theatreAdded.id,
            'name': theatreAdded.name,
            'location' : theatreAdded.location,
            'capacity' : theatreAdded.capacity
        }
   except Exception as err:
        raise Exception(str(err))

def getall_control():
    try:
        theatres = theatreRepository.get_all_theatres()

        # Transform the list of theatre objects into a list of dictionaries
        theatres_list = [{
            '_id': theatre.id,
            'name': theatre.name,
            'location': theatre.location,
            'capacity': theatre.capacity
        } for theatre in theatres]

        return theatres_list
    except Exception as err:
        raise Exception(str(err))

def findbylocation_control(location):
    try:
        theatres = theatreRepository.find_theatre_by_location(location)
        # Transform the list of theatre objects into a list of dictionaries
        theatres_list = [{
            '_id': theatre.id,
            'name': theatre.name,
            'location': theatre.location,
            'capacity': theatre.capacity
        } for theatre in theatres]

        return theatres_list
    except Exception as err:
        raise Exception(str(err))

def deleteTheatreById_control(id):
    try:
        result = theatreRepository.delete_theatre_by_id(id)

        if result['success']:
            return {
                'success': True,
                'message': 'Theatre deleted successfully'
            }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while deleting the theatre')
            }
    except Exception as err:
        raise Exception(str(err))

def getTheatreById_control(id):
    try:
        theatre = theatreRepository.get_theatre_by_id(id)

        return {
            '_id': theatre.id,
            'name': theatre.name,
            'location' : theatre.location,
            'capacity' : theatre.capacity
        }
    except Exception as err:
        raise Exception(str(err))

def update_control(theatre_info):
    try:
        # Update theatre in the database
        result = theatreRepository.update_theatre(theatre_info['_id'], theatre_info['name'], theatre_info['location'], theatre_info['capacity'])
        if result['success']:
            return {
                'success': True,
                'message': 'Theatre updated successfully'
                }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while updating the theatre')
                }
    except Exception as err:
        raise Exception(str(err))