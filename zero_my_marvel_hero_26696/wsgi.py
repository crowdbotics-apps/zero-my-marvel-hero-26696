"""
WSGI config for zero_my_marvel_hero_26696 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zero_my_marvel_hero_26696.settings')

application = get_wsgi_application()
