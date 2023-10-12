from database import db
from .showModel import Show
import os, sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *

#add new show
def add_show(name, language, tag, rating):
    try:
        new_show = Show(name=name, language=language, tag=tag, rating=rating)
        db.session.add(new_show)
        db.session.commit()
        return new_show
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }

#get all shows
def get_all_shows():
    try:
        shows = Show.query.all()
        if shows:
            return shows  # Return the list of show objects
        raise Exception(ERROR_MESSAGES["SHOW_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

# get show by id
def get_show_by_id(id):
    try:
        # Check if the show with the given ID exists
        show_to_get = Show.query.get(id)
        if show_to_get:
            return {
                '_id': show_to_get.id,
                'name': show_to_get.name,
                'language': show_to_get.language,
                'tag': show_to_get.tag,
                'rating': show_to_get.rating
            }
        else:
            raise Exception(ERROR_MESSAGES["SHOW_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#delete show
def delete_show_by_id(id):
    try:
        # Check if the show with the given ID exists
        show_to_delete = Show.query.get(id)
        
        if show_to_delete:
            db.session.delete(show_to_delete)
            db.session.commit()
            return {'success': True, 'message': 'Show deleted successfully'}
        else:
            raise Exception(ERROR_MESSAGES["SHOW_NOT_FOUND"])
    except Exception as err:
        return {'success': False, 'error': str(err)}

# Update show by ID
def update_show(id, name, language, tag, rating):
    try:
        # Check if the show with the given ID exists
        show_to_update = Show.query.get(id)
        
        if show_to_update:
            # Update the show attributes
            show_to_update.name = name
            show_to_update.language = language
            show_to_update.tag = tag
            show_to_update.rating = rating

            db.session.commit()
            return {
                'success': True,
                'message': 'Show updated successfully'
            }
        else:
            raise Exception(ERROR_MESSAGES["SHOW_NOT_FOUND"])
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }

#find show by tag
def find_show_by_tag(tag):
    try:
        shows = Show.query.filter_by(tag=tag)
        if shows:
            return shows  # Return the list of show objects
        raise Exception(ERROR_MESSAGES["show_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#find show by language
def find_show_by_language(language):
    try:
        shows = Show.query.filter_by(language=language)
        if shows:
            return shows  # Return the list of show objects
        raise Exception(ERROR_MESSAGES["show_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#find show by rating
def find_show_by_rating(rating):
    try:
        shows = Show.query.filter_by(rating=rating)
        if shows:
            return shows  # Return the list of show objects
        raise Exception(ERROR_MESSAGES["show_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))










