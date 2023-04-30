"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nationalyouthprogramme.settings')

application = get_asgi_application()
