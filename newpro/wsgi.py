"""
WSGI config for newpro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application # GUNCELLENDI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newpro.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod") # EKLENDI



application = get_wsgi_application()
