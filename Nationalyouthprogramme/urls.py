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


    path('course_and_college',course_and_college,name='course_and_college'),
    path('admission_registration',admission_registration,name='admission_registration'),
    path('exam_registration',exam_registration,name='exam_registration'),
    path('mark_registration',mark_registration,name='mark_registration'),
    path('add_on_programme',add_on_programme,name='add_on_programme'),
    path('application_for_affiliation',application_for_affiliation,name='application_for_affiliation'),
    path('pay_online_fees',pay_online_fees,name='pay_online_fees'),
    path('e_office_file_sanction',e_office_file_sanction,name='e_office_file_sanction'),
    path('student_marks',student_marks,name='student_marks'),
]
