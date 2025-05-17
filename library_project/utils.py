import hashlib
import uuid
from datetime import datetime, timedelta

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_id():
    return str(uuid.uuid4())

def today():
    return datetime.today().strftime('%Y-%m-%d')

def due_date(days=14):
    return (datetime.today() + timedelta(days=days)).strftime('%Y-%m-%d')
