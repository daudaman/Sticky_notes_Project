# Operating system commands
import os
# Django WSGI application
from django.core.wsgi import get_wsgi_application

# Django settings file ka path set karo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_project.settings')
# WSGI application banao (server chalane ke liye)
application = get_wsgi_application()
