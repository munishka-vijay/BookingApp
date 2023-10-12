from . import bookingRepository
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
from ..inventory import inventoryRepository


def add_control(booking_info):
   try:
      # Save booking to the database
      #inventory_id, user_id, ticket_count, date
      inventory = inventoryRepository.find_inventory_by_id(booking_info['inventory_id'])
      if inventory.available_seats < booking_info['ticket_count']:
        raise Exception(ERROR_MESSAGES["NO_SEATS_AVAILABLE"])

      bookingAdded = bookingRepository.add_booking(booking_info['inventory_id'], booking_info['user_id'], booking_info['ticket_count'], booking_info['date'])
      inventoryRepository.update_inventory_count(inventory.id,inventory.available_seats-bookingAdded.ticket_count)
      return {
            '_id': bookingAdded.id,
            'inventory_id': bookingAdded.inventory_id,
            'user_id' : bookingAdded.user_id,
            'ticket_count' : bookingAdded.ticket_count,
            'date':bookingAdded.date
        }
   except Exception as err:
        raise Exception(str(err))


def findbyUserId_control(id):
    try:
        bookings = bookingRepository.find_booking_by_userId(id)
        # Transform the list of booking objects into a list of dictionaries
        bookings_list = [{
            '_id': booking.id,
            'inventory_id': booking.inventory_id,
            'user_id' : booking.user_id,
            'ticket_count' : booking.ticket_count,
            'date':booking.date
           
        } for booking in bookings]

        return bookings_list
    except Exception as err:
        raise Exception(str(err))