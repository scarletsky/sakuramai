import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

import django.core.handlers.wsgi
import sae

os.environ['DJANGO_SETTINGS_MODULE'] = 'sakuramai.settings' 
app = django.core.handlers.wsgi.WSGIHandler()
application = sae.create_wsgi_app(app)
