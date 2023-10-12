from database import db
from datetime import date
from sqlalchemy import and_
from .inventoryModel import Inventory
from ..theatre.theatreRepository import get_theatre_by_id
import os, sys


# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *

from datetime import datetime

#add new inventory
def add_inventory(theatre_id, show_id, date, start_time, end_time, retail_price, selling_price, is_active=True):
    try:
        theatre = get_theatre_by_id(theatre_id)
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        start_time_obj = datetime.strptime(start_time, "%H:%M:%S").time()
        end_time_obj = datetime.strptime(end_time, "%H:%M:%S").time()
    
        new_inventory = Inventory(
            theatre_id=theatre_id,
            show_id=show_id,
            date=date_obj,
            start_time=start_time_obj,
            end_time=end_time_obj,
            retail_price=retail_price,
            selling_price=selling_price,
            is_active=is_active,
            available_seats=theatre.capacity
        )
        db.session.add(new_inventory)
        db.session.commit()
        return new_inventory
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }


#get all inventorys
def get_all_inventorys():
    try:
        inventorys = Inventory.query.filter(Inventory.date >= date.today()).all()
        if inventorys:
            return inventorys  # Return the list of inventory objects
        raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#delete inventory
def delete_inventory_by_id(id):
    try:
        # Check if the inventory with the given ID exists
        inventory_to_delete = Inventory.query.get(id)
        
        if inventory_to_delete:
            db.session.delete(inventory_to_delete)
            db.session.commit()
            return {'success': True, 'message': 'Inventory deleted successfully'}
        else:
            raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        return {'success': False, 'error': str(err)}

# Update inventory by ID
def update_inventory(id, theatre_id, show_id, date, start_time, end_time, retail_price, selling_price, is_active):
    try:
        # Check if the inventory with the given ID exists
        inventory_to_update = Inventory.query.get(id)
        
        if inventory_to_update:
            # Update the inventory attributes
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_time_obj = datetime.strptime(start_time, "%H:%M:%S").time()
            end_time_obj = datetime.strptime(end_time, "%H:%M:%S").time()

            inventory_to_update.theatre_id = theatre_id
            inventory_to_update.show_id = show_id
            inventory_to_update.date = date_obj
            inventory_to_update.start_time = start_time_obj
            inventory_to_update.end_time = end_time_obj
            inventory_to_update.retail_price = retail_price
            inventory_to_update.selling_price = selling_price
            inventory_to_update.is_active = is_active

            db.session.commit()
            return {
                'success': True,
                'message': 'Inventory updated successfully'
            }
        else:
            raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }

# Update inventory by ID
def update_inventory_count(id,count):
    try:
        # Check if the inventory with the given ID exists
        inventory_to_update = Inventory.query.get(id)
        
        if inventory_to_update:
            inventory_to_update.available_seats=count
            db.session.commit()
            return {
                'success': True,
                'message': 'Inventory updated successfully'
            }
        else:
            raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }


#find inventory by theatre
def find_inventory_by_theatre(theatre_id):
    try:
        inventorys = Inventory.query.filter_by(theatre_id=theatre_id)
        if inventorys:
            return inventorys  # Return the list of inventory objects
        raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))


#find inventory by show
def find_inventory_by_show(show_id):
    try:
        inventorys = Inventory.query.filter_by(show_id=show_id)
        if inventorys:
            return inventorys  # Return the list of inventory objects
        raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

#find inventory by start_time
def find_inventory_by_start_time(start_time):
    try:
        start_time_obj = datetime.strptime(start_time, "%H:%M:%S").time()
        inventorys = Inventory.query.filter_by(start_time=start_time_obj)
        if inventorys:
            return inventorys  # Return the list of inventory objects
        raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))


#find inventory by id
def find_inventory_by_id(id):
    try:
        inventory = Inventory.query.get(id)
        if inventory:
            return inventory  # Return the list of inventory objects
        raise Exception(ERROR_MESSAGES["INVENTORY_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))












