import os
import sys
from django.core.handlers.wsgi import WSGIHandler
sys.path.append("/home/scarlex/sae/sakuramai/1")
os.environ["DJANGO_SETTINGS_MODULE"] = "sakuramai.settings"
application = WSGIHandler()
