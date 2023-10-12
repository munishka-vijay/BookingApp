from celery import Celery
from datetime import date
from celery.schedules import crontab
from mailer.dailymail import daily_user_mail
from mailer.dailymail import monthly_user_mail
from app import create_app  # Import your Flask app factory function
from apis.modules.booking import bookingRepository
from apis.modules.user import userRepository
from flask import Flask
from database import db
from utils.config import Config
app_celery = Celery('tasks', broker='redis://localhost:6379/0')

# Create a Flask app instance within the Celery worker
def create_celery_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Replace with your config class

    # Initialize SQLAlchemy with the app
    db.init_app(app)
    
    return app

@app_celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # This schedules the task to run every 5 minutes
    sender.add_periodic_task(
        crontab(minute='*/3'),
        daily_reminder_mail.s(),
    )
    sender.add_periodic_task(
        crontab(minute='*/1'),
        monthly_entertainment_report.s(),
    )

@app_celery.task
def daily_reminder_mail():
    print("Task daily_reminder_mail is executing.")
    app = create_celery_app()
    app.app_context().push()
    users_without_booking = bookingRepository.find_user_with_no_today_booking()

    print(users_without_booking)

    for user in users_without_booking:
        # Send a reminder to the user using your notification function
        daily_user_mail(user.email, "Reminder Mail", "Book your favorite movies today. Visit us at http://localhost:8080/ ")

@app_celery.task
def monthly_entertainment_report():
    print("Monthly Entertainment Report")
    app = create_celery_app()
    app.app_context().push()
    all_users =userRepository.find_all_users()
    print(all_users)
    for user in all_users :
        booking_detail=bookingRepository.find_booking_by_userId(user.id)
        bookings_list = [{
            '_id': booking.id,
            'inventory_id': booking.inventory_id,
            'user_id' : booking.user_id,
            'user_name':booking.user.username,
            'ticket_count' : booking.ticket_count,
            'date':booking.date,
            'movie name':booking.inventory.show.name,
            'tag':booking.inventory.show.tag,
            'rating':booking.inventory.show.rating,
            
            
           
        } for booking in booking_detail]
        monthly_user_mail(user.email, "Monthly Entertainment Report",bookings_list)

if __name__ == '__main__':
    app_celery.start()
