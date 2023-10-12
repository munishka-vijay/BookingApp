from flask import Flask
from flask_cors import CORS
from utils.config import Config
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import db
import redis


from apis.modules.user.userRoutes import user_api
from apis.modules.theatre.theatreRoutes import theatre_api
from apis.modules.show.showRoutes import show_api
from apis.modules.inventory.inventoryRoutes import inventory_api
from apis.modules.booking.bookingRoutes import booking_api


def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Set configuration from object 
    app.config.from_object(Config)


    # Register the user_api blueprint
    app.register_blueprint(user_api, url_prefix='/user')

    # Register the theatre_api blueprint
    app.register_blueprint(theatre_api, url_prefix='/theatre')

    # Register the show_api blueprint
    app.register_blueprint(show_api, url_prefix='/show')

    # Register the inventory_api blueprint
    app.register_blueprint(inventory_api, url_prefix='/inventory')

    # Register the booking_api blueprint
    app.register_blueprint(booking_api, url_prefix='/booking')
    # Initialize a Redis connection pool
    app.redis = redis.Redis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB']
)
    return app

#Instantiate the flask application
app = create_app()

#Setting up database connectivity
db.init_app(app)

with app.app_context():
    db.create_all()



# Hello Route
@app.route('/', methods=['GET'])
def greetings():
    return "Hello, this is me trying to build my Flask app, I am Munishka. Hehehe"

@app.route('/test-db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return 'Successfully connected to the database!'
    except Exception as e:
        return f'Failed to connect to the database. Error: {str(e)}'

if __name__ == "__main__":
    app.run(debug=True)
