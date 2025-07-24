import sys
import os


project_home = '/home/shreyanthsureshkrishnaa/flask_app'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path


os.environ['FLASK_APP'] = 'app.py'

from app import app as application  
