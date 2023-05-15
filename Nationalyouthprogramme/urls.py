"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

from django.contrib import admin
from django.urls import path
from nationalyouth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('dologin', Login.as_view(),name='dologin'),
    path('forgot_password',forgot_password,name='forgot_password'),
    path('about_us',about_us,name='about_us'),
    path('gallery',gallery,name='gallery'),
    path('sector',sector,name='sector'),
    path('contact_us',contact_us,name='contact_us'),
    path('news',news,name='news'),
]
