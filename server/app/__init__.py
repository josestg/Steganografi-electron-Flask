from flask import Flask

# init the app
app = Flask(__name__,instance_relative_config=True)
# we can use app.config.from_object('config')

# Load the views
from app import views

# Load the config file
app.config.from_object('config')