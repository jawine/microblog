from flask import Flask

 # configure flask (__name__) is automatically set to name of module
app = Flask(__name__)


 # import at bottom of file to avoid circular imports (routes.py depends on app.py)
from app import routes




