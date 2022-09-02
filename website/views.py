from flask import Blueprint

views = Blueprint('views', __name__)

# When the path in quotes is hit, run the function 
@views.route('/')
def home():
    return "<hi>Test</h1>"