from . import inventoryRepository
from flask import jsonify

import sys,json
import os
# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now we can import the required module
from utils.errors import *
from utils.utils import *

def add_control(inventory_info):
   try:
      # Save inventory to the database
      #theatre_id, show_id, date, start_time, end_time, retail_price, selling_price, is_active=True
      
      inventoryAdded = inventoryRepository.add_inventory(inventory_info['theatre_id'], inventory_info['show_id'], inventory_info['date'], inventory_info['start_time'], inventory_info['end_time'], inventory_info['retail_price'], inventory_info['selling_price'], inventory_info['is_active'])
      return {
        '_id': inventoryAdded.id,
        'theatre_id': inventoryAdded.theatre_id,
        'show_id': inventoryAdded.show_id,
        'date': str(inventoryAdded.date),
        'start_time': str(inventoryAdded.start_time),
        'end_time': str(inventoryAdded.end_time),
        'retail_price': inventoryAdded.retail_price,
        'selling_price': inventoryAdded.selling_price,
        'is_active': inventoryAdded.is_active,
        'available_seats':inventoryAdded.available_seats
        }

   except Exception as err:
        raise Exception(str(err))

def getall_control():
    try:
      inventorys= inventoryRepository.get_all_inventorys()

      # Transform the list of inventory objects into a list of dictionaries
      inventorys_list = [{
         '_id': inventory.id,
         'theatre_id': inventory.theatre_id,
         'theatre':{
            'name': inventory.theatre.name,
            'location' : inventory.theatre.location,
            'capacity' : inventory.theatre.capacity
         },
         'show':{
            'name': inventory.show.name,
            'language': inventory.show.language,
            'tag': inventory.show.tag,
            'rating': inventory.show.rating
         },
         'show_id': inventory.show_id,
         'date': str(inventory.date),
         'start_time': str(inventory.start_time),
         'end_time': str(inventory.end_time),
         'retail_price': inventory.retail_price,
         'selling_price': inventory.selling_price,
         'is_active': inventory.is_active,
         'available_seats':inventory.available_seats

      } for inventory in inventorys]
      return inventorys_list

    except Exception as err:
        raise Exception(str(err))

def deleteInventoryById_control(id):
    try:
        result = inventoryRepository.delete_inventory_by_id(id)

        if result['success']:
            return {
                'success': True,
                'message': 'Inventory deleted successfully'
            }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while deleting the inventory')
            }
    except Exception as err:
        raise Exception(str(err))

def update_control(inventory_info):
    try:
        # Update inventory in the database
        result = inventoryRepository.update_inventory(
            inventory_info['_id'],
            inventory_info['theatre_id'],
            inventory_info['show_id'],
            inventory_info['date'],
            inventory_info['start_time'],
            inventory_info['end_time'],
            inventory_info['retail_price'],
            inventory_info['selling_price'],
            inventory_info['is_active']
        )

        if result['success']:
            return {
                'success': True,
                'message': 'Inventory updated successfully'
            }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while updating the inventory')
            }
    except Exception as err:
        raise Exception(str(err))




def findbyTheatreId_control(id):
    try:
        inventorys = inventoryRepository.find_inventory_by_theatre(id)
        # Transform the list of inventory objects into a list of dictionaries
        inventorys_list = [{
         '_id': inventory.id,
         'theatre_id': inventory.theatre_id,
          'theatre':{
            'name': inventory.theatre.name,
            'location' : inventory.theatre.location,
            'capacity' : inventory.theatre.capacity
         },
         'show':{
            'name': inventory.show.name,
            'language': inventory.show.language,
            'tag': inventory.show.tag,
            'rating': inventory.show.rating
         },
         'show_id': inventory.show_id,
         'date': str(inventory.date),
         'start_time': str(inventory.start_time),
         'end_time': str(inventory.end_time),
         'retail_price': inventory.retail_price,
         'selling_price': inventory.selling_price,
         'is_active': inventory.is_active,        
         'available_seats':inventory.available_seats

      } for inventory in inventorys]

        return inventorys_list
    except Exception as err:
        raise Exception(str(err))


def findbyShowId_control(id):
    try:
        inventorys = inventoryRepository.find_inventory_by_show(id)
        # Transform the list of inventory objects into a list of dictionaries
        inventorys_list = [{
         '_id': inventory.id,
         'theatre_id': inventory.theatre_id,
         'show_id': inventory.show_id,
          'theatre':{
            'name': inventory.theatre.name,
            'location' : inventory.theatre.location,
            'capacity' : inventory.theatre.capacity
         },
         'show':{
            'name': inventory.show.name,
            'language': inventory.show.language,
            'tag': inventory.show.tag,
            'rating': inventory.show.rating
         },
         'date': str(inventory.date),
         'start_time': str(inventory.start_time),
         'end_time': str(inventory.end_time),
         'retail_price': inventory.retail_price,
         'selling_price': inventory.selling_price,
         'is_active': inventory.is_active,        
         'available_seats':inventory.available_seats

      } for inventory in inventorys]

        return inventorys_list
    except Exception as err:
        raise Exception(str(err))


def findbyStartTime_control(start_time):
    try:
        inventorys = inventoryRepository.find_inventory_by_start_time(start_time)
        # Transform the list of inventory objects into a list of dictionaries
        inventorys_list = [{
         '_id': inventory.id,
         'theatre_id': inventory.theatre_id,
         'show_id': inventory.show_id,
         'date': str(inventory.date),
          'theatre':{
            'name': inventory.theatre.name,
            'location' : inventory.theatre.location,
            'capacity' : inventory.theatre.capacity
         },
         'show':{
            'name': inventory.show.name,
            'language': inventory.show.language,
            'tag': inventory.show.tag,
            'rating': inventory.show.rating
         },
         'start_time': str(inventory.start_time),
         'end_time': str(inventory.end_time),
         'retail_price': inventory.retail_price,
         'selling_price': inventory.selling_price,
         'is_active': inventory.is_active,
         'available_seats':inventory.available_seats
      } for inventory in inventorys]

        return inventorys_list
    except Exception as err:
        raise Exception(str(err))


