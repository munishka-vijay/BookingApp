# celeryconfig.py
from celery import Celery
from datetime import timedelta

app = Celery(
    'Movie-Ticket-Booking-System',  
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=['backendtasks'], 
)

# Set the timezone to Indian Standard Time (IST)
app.conf.timezone = 'Asia/Kolkata'
