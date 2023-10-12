import bcrypt
import jwt
from datetime import datetime, timedelta
from .config import Config
from flask_bcrypt import check_password_hash


def get_hashed_password(password):
    # Generate a salt (a random string) to use during hashing
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    # Return the hashed password
    return hashed_password.decode("utf-8")


def generate_jwt_token(user_id, username):
    # Set the expiration time for the token
    expiration = datetime.utcnow() + timedelta(hours=Config.JWT_ACCESS_TOKEN_EXPIRES)

    # Create the payload containing the user ID, username, and expiration time
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': expiration
    }

    # Generate the JWT token using the secret key from the Flask app configuration
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')

    # Return the generated token
    return token

def compare_hash(plaintext, hashed_password):
    return check_password_hash(hashed_password, plaintext)