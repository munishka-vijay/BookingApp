from database import db
from .theatreModel import Theatre
import os, sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *

#add new theatre
def add_theatre(name, location, capacity):
    try:
        new_theatre = Theatre(name=name, location=location, capacity=capacity)
        db.session.add(new_theatre)
        db.session.commit()
        return new_theatre
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }

#find theatre by location
def find_theatre_by_location(location):
    try:
        theatres = Theatre.query.filter_by(location=location)
        if theatres:
            return theatres  # Return the list of Theatre objects
        raise Exception(ERROR_MESSAGES["THEATRE_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#get all theatres
def get_all_theatres():
    try:
        theatres = Theatre.query.all()
        if theatres:
            return theatres  # Return the list of Theatre objects
        raise Exception(ERROR_MESSAGES["THEATRE_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#delete theatre
def delete_theatre_by_id(id):
    try:
        # Check if the theatre with the given ID exists
        theatre_to_delete = Theatre.query.get(id)
        
        if theatre_to_delete:
            db.session.delete(theatre_to_delete)
            db.session.commit()
            return {'success': True, 'message': 'Theatre deleted successfully'}
        else:
            raise Exception(ERROR_MESSAGES["THEATRE_NOT_FOUND"])
    except Exception as err:
        return {'success': False, 'error': str(err)}

#get theatre by id
def get_theatre_by_id(id):
    try:
        # Check if the theatre with the given ID exists
        theatre_to_get = Theatre.query.get(id)
        if theatre_to_get:
            return theatre_to_get
        else:
            raise Exception(ERROR_MESSAGES["THEATRE_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

# Update theatre by ID
def update_theatre(id, name, location, capacity):
    try:
        # Check if the theatre with the given ID exists
        theatre_to_update = Theatre.query.get(id)
        
        if theatre_to_update:
            # Update the theatre attributes
            theatre_to_update.name = name
            theatre_to_update.location = location
            theatre_to_update.capacity = capacity

            db.session.commit()
            return {
                'success': True,
                'message': 'Theatre updated successfully'
            }
        else:
            raise Exception(ERROR_MESSAGES["THEATRE_NOT_FOUND"])
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }









