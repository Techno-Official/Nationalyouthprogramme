"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nationalyouthprogramme.settings')

application = get_wsgi_application()
