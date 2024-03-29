import sys
import os
import imp
from django.core.handlers.wsgi import WSGIHandler

# assume we are ./apps/mainsite/manage.py
APPS_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)
TOP_DIR = os.path.dirname(APPS_DIR)
# assume that the virtualenv is a directory named 'env' sibling to TOP_DIR
ENV_DIR = os.path.join(os.path.dirname(TOP_DIR), 'env')

# if virtualenv exists, activate it
activate_this = os.path.join(ENV_DIR, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

# determine the settings file to load, if we are invoked as django_something, we will trying to load mainsite.settings_something
settings_name = 'mainsite.settings'
if '_' in sys.argv[0]:
    base, suffix = sys.argv[0].split('_',1)
    settings_name += '_'+os.path.splitext(suffix)[0]

# call through to the django application
os.environ['DJANGO_SETTINGS_MODULE'] = settings_name
application = WSGIHandler()

