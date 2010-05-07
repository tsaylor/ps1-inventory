import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.path.insert(0, '/var/django/inventory_site')
sys.path.insert(0, '/var/django/inventory_site/project')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
