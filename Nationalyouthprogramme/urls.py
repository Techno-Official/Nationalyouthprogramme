"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

from django.contrib import admin
from django.urls import path
from nationalyouth.views import *
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('dologin', user_login,name='dologin'),
    path('user_logout',user_logout,name='user_logout'),
    path('forgot_password',forgot_password,name='forgot_password'),
    path('about_us',about_us,name='about_us'),
    path('gallery',gallery,name='gallery'),
    path('sector',sector,name='sector'),
    path('contact_us',contact_us,name='contact_us'),
    path('home_contact_us',home_contact_us,name='home_contact_us'),
    path('news',news,name='news'),
    path('news_details',news_details,name='news_details'),


    path('course_and_college',course_and_college,name='course_and_college'),
    path('vtc_course_admission',vtc_course_admission,name='vtc_course_admission'),
    path('admission_registration',admission_registration,name='admission_registration'),
    path('exam_registration',exam_registration,name='exam_registration'),
    path('mark_registration',mark_registration,name='mark_registration'),
    path('add_on_programme',add_on_programme,name='add_on_programme'),
    path('application_for_affiliation',application_for_affiliation,name='application_for_affiliation'),
    path('employee_service_book',employee_service_book,name='employee_service_book'),
    path('pay_online_fees',pay_online_fees,name='pay_online_fees'),
    path('e_office_file_sanction',e_office_file_sanction,name='e_office_file_sanction'),
    path('student_marks',student_marks,name='student_marks'),


    path('e_finance_and_accounts',e_finance_and_accounts,name='se_finance_and_accounts'),
    path('e_office_accounts',e_office_accounts,name='e_office_accounts'),
    path('e_office_student_register',e_office_student_register,name='e_office_student_register'),
    path('e_office_email',e_office_email,name='e_office_email'),
    path('e_office_queue_files',e_office_queue_files,name='e_office_queue_files'),
    path('e_office_files',e_office_files,name='e_office_files'),
    path('e_employee_records',e_employee_records,name='e_employee_records'),
    path('e_employee_live_and_leave_status',e_employee_live_and_leave_status,name='e_employee_live_and_leave_status'),
    path('e_employee_live_status',e_employee_live_status,name='e_employee_live_status'),
    path('e_employee_leave_status',e_employee_leave_status,name='e_employee_leave_status'),
    path('e_employee_daily_work_statement',e_employee_daily_work_statement,name='e_employee_daily_work_statement'),
    path('e_adminstations',e_adminstations,name='e_adminstations'),
    path('e_student_certificate_verification',e_student_certificate_verification,name='e_student_certificate_verification'),



    path('e_office_mark_list_registration',e_office_mark_list_registration,name='e_office_mark_list_registration'),
    path('e_office_student_admisiion_registration',e_office_student_admisiion_registration,name='e_office_student_admisiion_registration'),
    path('e_office_student_add_on_programme',e_office_student_add_on_programme,name='e_office_student_add_on_programme'),


    path('e_office_files_student_mark_list',e_office_files_student_mark_list,name='e_office_files_student_mark_list'),
    path('e_office_files_daily_work_statement',e_office_files_daily_work_statement,name='e_office_files_daily_work_statement'),
    path('e_office_files_employee_live_status',e_office_files_employee_live_status,name='e_office_files_employee_live_status'),
    path('e_office_files_pay_online_fees',e_office_files_pay_online_fees,name='e_office_files_pay_online_fees'),


    path('staff_work_alloted',staff_work_alloted,name='staff_work_alloted'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
