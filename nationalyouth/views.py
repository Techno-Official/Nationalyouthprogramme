"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from nationalyouth.models import *
from django.views import  View
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import random
import time
from django.core.mail import EmailMessage
from django.conf import settings





#===================================================================================================
#======================================= Homepage Page =============================================
def homepage(request):
    return render(request,'Main/homepage.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Login Page ================================================
class Login(View):
    def get(self, request):
        return render(request, 'Main/login.html')

    def post(self, request):
        pass
#=================================================================================================
#=================================================================================================



#==================================================================================================
#======================================= Forgot Password Page =====================================
def forgot_password(request):
    return render(request,'Main/forgot_password.html')
#=================================================================================================
#=================================================================================================




#==================================================================================================
#======================================= About Page ===============================================
def about_us(request):
    return render(request,'Main/about.html')
#=================================================================================================
#=================================================================================================




#===================================================================================================
#======================================= Gallery Page ==============================================
def gallery(request):
    return render(request,'Main/skill_photos.html')
#=================================================================================================
#=================================================================================================



#===================================================================================================
#======================================= Sector Page ===============================================
def sector(request):
    return render(request,'Main/sectors.html')
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= Cotanct Page ==============================================
def contact_us(request):
    return render(request,'Main/contact.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= News Page =================================================
def news(request):
    return render(request,'Main/latest_updates.html')
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= Internal Functions (1) ====================================

#===================================================================================================
#======================================= Course and college Page ===================================
def course_and_college(request):
    return render(request,'internal/course_and_college.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Admission Registration Page ===============================
def admission_registration(request):
    return render(request,'internal/admission_registration.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Exam Registration Page ====================================
def exam_registration(request):
    return render(request,'internal/exam_registration.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Mark Registration Page ====================================
def mark_registration(request):
    return render(request,'internal/mark_registration.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Add on Programme Page =====================================
def add_on_programme(request):
    return render(request,'internal/add_on_programme.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Application For Affiliation Page ==========================
def application_for_affiliation(request):
    return render(request,'internal/application_for_affiliation.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Pay Online Fees Page ======================================
def pay_online_fees(request):
    return render(request,'internal/pay_online_fees.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Office File Sanction Page ===============================
def e_office_file_sanction(request):
    return render(request,'internal/e_office_file_sanction.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= Student Marks Page ========================================
def student_marks(request):
    return render(request,'internal/student_marks.html')
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= Internal Functions (2) ====================================

#===================================================================================================
#======================================= E-Finance and Accounts Page ===============================
def e_finance_and_accounts(request):
    return render(request,'internal/e_finance_and_accounts.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E-Office Accounts Page ====================================
def e_office_accounts(request):
    return render(request,'internal/e-office_accounts.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E-Office Student Register Page ============================
def e_office_student_register(request):
    return render(request,'internal/e_office_students_registration.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E-Office Email Page =======================================
def e_office_email(request):
    return render(request,'internal/e_office_email.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E-Office Queue Files Page =================================
def e_office_queue_files(request):
    return render(request,'internal/e_office_queue_files.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E-Office Files Page =======================================
def e_office_files(request):
    return render(request,'internal/e_office_files.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Employee Records Page ===================================
def e_employee_records(request):
    return render(request,'internal/e_employee_records.html')
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= E Employee Daily Work Statement Page ======================
def e_employee_daily_work_statement(request):
    return render(request,'internal/e_employee_daily_work_statement.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Employee Live Status Page ===============================
def e_employee_live_status(request):
    return render(request,'internal/e_employee_live_status.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Adminstration Page ======================================
def e_adminstations(request):
    return render(request,'internal/e_adminstration.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Student Certificate Verification Page ===================
def e_student_certificate_verification(request):
    return render(request,'internal/e_student_certificate_verification.html')
#===================================================================================================
#===================================================================================================





#============================================ Extra ================================================


#===================================================================================================
#======================================= E Office Student Mark List Registration Page ==============
def e_office_mark_list_registration(request):
    return render(request,'internal/e_office_mark_list_registration.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Office Student Admission Registration Page ==============
def e_office_student_admisiion_registration(request):
    return render(request,'internal/e_office_student_admission_registration.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Office Student Add on Programme Page ====================
def e_office_student_add_on_programme(request):
    return render(request,'internal/e_office_student_add_on_programme.html')
#===================================================================================================
#===================================================================================================