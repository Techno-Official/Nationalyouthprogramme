"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """


from django.urls import path
from nationalyouth.views import *

urlpatterns = [
    
    path('',homepage,name='homepage'),
]
