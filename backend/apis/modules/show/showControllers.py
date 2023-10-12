from . import showRepository
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

def add_control(show_info):
   try:
      
      # Save show to the database
      showAdded = showRepository.add_show(show_info['name'], show_info['language'], show_info['tag'], show_info['rating'])

      return {
            '_id': showAdded.id,
            'name': showAdded.name,
            'language' : showAdded.language,
            'tag' : showAdded.tag,
            'rating':showAdded.rating
        }
   except Exception as err:
        raise Exception(str(err))

def getall_control():
    try:
        shows = showRepository.get_all_shows()

        # Transform the list of show objects into a list of dictionaries
        shows_list = [{
            '_id': show.id,
            'name': show.name,
            'language': show.language,
            'tag': show.tag,
            'rating': show.rating
        } for show in shows]

        return shows_list
    except Exception as err:
        raise Exception(str(err))


def getShowById_control(id):
    try:
        show = showRepository.get_show_by_id(id)

        # Ensure you're returning a model object, not a dictionary
        return show
    except Exception as err:
        raise Exception(str(err))



def deleteShowById_control(id):
    try:
        result = showRepository.delete_show_by_id(id)

        if result['success']:
            return {
                'success': True,
                'message': 'show deleted successfully'
            }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while deleting the show')
            }
    except Exception as err:
        raise Exception(str(err))

def update_control(show_info):
    try:
        # Update show in the database
        result = showRepository.update_show(show_info['_id'], show_info['name'], show_info['language'], show_info['tag'], show_info['rating'])
        if result['success']:
            return {
                'success': True,
                'message': 'Show updated successfully'
                }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while updating the show')
                }
    except Exception as err:
        raise Exception(str(err))


def findbytag_control(tag):
    try:
        shows = showRepository.find_show_by_tag(tag)
        # Transform the list of show objects into a list of dictionaries
        shows_list = [{
            '_id': show.id,
            'name': show.name,
            'language': show.language,
            'tag': show.tag,
            'rating': show.rating
        } for show in shows]

        return shows_list
    except Exception as err:
        raise Exception(str(err))

def findbylanguage_control(language):
    try:
        shows = showRepository.find_show_by_language(language)
        # Transform the list of show objects into a list of dictionaries
        shows_list = [{
            '_id': show.id,
            'name': show.name,
            'language': show.language,
            'tag': show.tag,
            'rating': show.rating
        } for show in shows]

        return shows_list
    except Exception as err:
        raise Exception(str(err))

def findbyrating_control(rating):
    try:
        shows = showRepository.find_show_by_rating(rating)
        # Transform the list of show objects into a list of dictionaries
        shows_list = [{
            '_id': show.id,
            'name': show.name,
            'language': show.language,
            'tag': show.tag,
            'rating': show.rating
        } for show in shows]

        return shows_list
    except Exception as err:
        raise Exception(str(err))