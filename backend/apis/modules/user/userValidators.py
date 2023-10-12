import re
from flask_request_validator import (
    Param,
    validate_params,
    JSON,
    ValidRequest
)
# from flask import request

def validate_username(username):
    username_pattern = re.compile(r'^[a-zA-Z0-9_]+$') #only alphabets, numbers and underscore is allowed
    return username_pattern.match(username)

def validate_password(password):
    password_pattern = re.compile(r'^[a-zA-Z0-9]+$') #only alphabets and numbers are allowed
    return password_pattern.match(password)

def validate_email(email):
    email_pattern = re.compile(r'^[\w.-]+@[a-zA-Z_-]+?\.[a-zA-Z]{2,3}$') #'.','@', alphabets and numbers are allowed 
    return email_pattern.match(email)

def validate_phone(phone):
    phone_pattern = re.compile(r'^\d{10}$') #only 10 digits/numbers are allowed
    return phone_pattern.match(phone)

@validate_params(
    Param('username', JSON, str, required=True),
    Param('email', JSON, str, required=True),
    Param('phone', JSON, str, required=True),
    Param('password', JSON, str, required=True)
)
def signup_auth(valid: ValidRequest):
    data = valid.get_json()
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    errors = {}

    if not validate_username(username):
        errors['username'] = 'Invalid username format. Only letters, numbers, and underscore (_) are allowed.'

    if not validate_email(email):
        errors['email'] = 'Invalid email format.'

    if not validate_phone(phone):
        errors['phone'] = 'Invalid phone number format. It should be a 10-digit number.'

    if not validate_password(password):
        errors['password'] = 'Invalid password format. Only alphanumeric characters are allowed.'

    if errors:
        return {'error': errors}

    return None

@validate_params(
    Param('username', JSON, str, required=True),
    Param('password', JSON, str, required=True)
)
def login_auth(valid: ValidRequest):
    data = valid.get_json()
    username = data.get('username')
    password = data.get('password')

    errors = {}

    if not validate_username(username):
        errors['username'] = 'Invalid username format. Only letters, numbers, and underscore (_) are allowed.'

    if not validate_password(password):
        errors['password'] = 'Invalid password format. Only alphanumeric characters are allowed.'

    if errors:
        return {'error': errors}

    return None

