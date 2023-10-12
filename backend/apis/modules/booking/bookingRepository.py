from database import db
from .bookingModel import Booking
from..user.userModel import User
from datetime import date

import os, sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, project_root)

# Now you can import the required module
from utils.errors import *

from datetime import datetime

from ..inventory import inventoryRepository

#add new booking
def add_booking(inventory_id, user_id, ticket_count, date):
    try:
        #inventory_id, user_id, ticket_count, date
      

        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        new_booking = Booking(inventory_id=inventory_id, user_id=user_id, ticket_count=ticket_count, date=date_obj)
        db.session.add(new_booking)
        db.session.commit()
        return new_booking
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }


#find booking by userId
def find_booking_by_userId(user_id):
    try:
        bookings = Booking.query.filter_by(user_id=user_id)
        if bookings:
            return bookings  
        raise Exception(ERROR_MESSAGES["BOOKING_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))

def find_user_with_no_today_booking():
    today = date.today()
    
    # Get all user IDs associated with bookings for today
    user_ids_with_bookings = [booking.user_id for booking in Booking.query.filter_by(date=today)]

    # Get all users
    all_users = User.query.all()

    # Filter users who do not have a booking for today
    users_without_booking = [user for user in all_users if user.id not in user_ids_with_bookings]

    return users_without_booking