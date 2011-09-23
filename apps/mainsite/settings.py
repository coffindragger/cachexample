import sys
import os


# assume we are ./apps/mainsite/settings.py
APPS_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)

from mainsite import import_settings


settings_global = globals()

# import settings from settings_project and add them to globals
settings_project = import_settings('mainsite.settings_project')
if settings_project is None:
    raise IOError("Could not import settings_project django settings.")
settings_global.update(settings_project)

settings_local = import_settings('mainsite.settings_local')
if settings_local is None:
    raise IOError("Could not import settings_local django settings.")
settings_global.update(settings_local)

