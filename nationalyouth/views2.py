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
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from  django.http import JsonResponse



#===================================================================================================
#======================================= Homepage Page =============================================
def homepage(request):
    user_pwd=CustomeUser.objects.all()
   
    # for user in user_pwd:

    #     get_pwd=user.password
    #     if get_pwd[0:9] !="pbkdf2_sh":
    #         if user.password:
    #             hashed_password = make_password(user.password)
    #             print(hashed_password)
    #             user.password = hashed_password
    #             user.save()

    count = None
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()

    data={
        'count':count,
    }
    return render(request,'Main/homepage.html',data)
#===================================================================================================
#===================================================================================================




#====================================================================================================
#======================================= Add New User Page ==========================================


def add_new_user(request):
    error_message = None
    value = None
    all_user_role = User_Role.objects.all()
    if request.method=="POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        get_username = request.POST.get("username")
        get_password = request.POST.get("password")

        get_user_role_id = request.POST.get("user_role")
        get_user_group = request.POST.get("user_group")
        hash_password = make_password(get_password)

        get_user_role = User_Role.objects.get(id=get_user_role_id)

        
        
        # user = CustomeUser.objects.get(username=get_username)

        value = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "username":get_username,
        }
        add_user = CustomeUser(
            username = get_username,
            first_name = fname,
            last_name = lname,
            email = email,
            password = hash_password,
            decrypt_password = get_password,
            user_status = '1',
            user_role = get_user_role,
            is_staff = True,
        )
        if not fname:
            error_message = "User First Name is Required !!"
        elif not lname:
            error_message = "User Last Name is Required !!"
        elif not email:
            error_message = "User Email is Required !!"
        elif not get_username:
            error_message = "Username is Required !!"
        elif not get_password:
            error_message = "User Password is Required !!"
        elif CustomeUser.objects.filter(email=email).exists():
            error_message = "Email Already Exists !!!"
        elif CustomeUser.objects.filter(username=get_username).exists():
            error_message = "Username Already Exists !!!"
        if not error_message:
            add_user.save()
            # add_user.groups.set(user_group)
            messages.success(request, "User Registered Successfully " )
            return redirect('add_new_user')
    data = {
        'user_role':all_user_role,
        'error':error_message,
        'value':value,
    }
    return render(request, 'internal/add_new_user.html', data)

#====================================================================================================




#====================================================================================================
#======================================= Login Page =================================================


def user_login(request):
    error_message = None
    value = None
    if request.method=="POST":
        username = request.POST.get("username")
        get_password = request.POST.get("password")

  
        get_user = CustomeUser.objects.filter(username=username).first()
        has_pwd=check_password(get_password,get_user.password)
        if has_pwd == True and get_user:
            login(request,get_user)
            return redirect('homepage')
        else:
            error_message="Check Username & Password"
        
    return render(request, 'Main/login.html', {'error':error_message,'value':value})

#==================================================================================================================================================
#==================================================================================================================================================



#======================================== Logout Page ==============================================================================================

def user_logout(request):
    logout(request)
    return redirect("/")
    
#=====================================================================================================================================================



#==================================================================================================
#======================================= Forgot Password Page =====================================
def forgot_password(request):
    return render(request,'Main/forgot_password.html')
#=================================================================================================
#=================================================================================================




#==================================================================================================
#======================================= About Page ===============================================
def about_us(request):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()

    data={
        'count':count,
    }
    return render(request,'Main/about.html',data)
#=================================================================================================
#=================================================================================================




#===================================================================================================
#======================================= Gallery Page ==============================================
def gallery(request):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()

    data={
        'count':count,
    }
    return render(request,'Main/skill_photos.html',data)
#=================================================================================================
#=================================================================================================



#===================================================================================================
#======================================= Sector Page ===============================================
def sector(request):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()

    data={
        'count':count,
    }
    return render(request,'Main/sectors.html',data)
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= Contact Page ==============================================
def contact_us(request):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()
    error_message = None
    value = None

    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile_number = request.POST.get("mobile_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact_id = random.randint(00000000,99999999)
        value = {
          'full_name' : full_name,
          'email':email,
          'mobile_number':mobile_number,
          'subject':subject,
          'message':message
        }
        save_data = Contact_us(
            contact_id=contact_id,
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            subject=subject,
            message = message,
        )
        if(not full_name):
            error_message = "Full Name is Required !!"
        elif not email:
            error_message = "Email is Required !!"
        elif not mobile_number:
            error_message = "Mobile No. is Required !!"
        elif not subject:
            error_message = "Subject is Required !!"
        elif not message:
            error_message = "Write some Message !!"
        if not error_message:
            save_data.save()
            messages.success(request, 'Your Response Submitted Successfully')
            return redirect('contact_us')

    data={
        'count':count,
        'value':value,
        'error':error_message,
    }
    return render(request,'Main/contact.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Home Contact Page =========================================
def home_contact_us(request):
    error_message = None
    value = None
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile_number = request.POST.get("mobile_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact_id = random.randint(00000000,99999999)
        value = {
          'full_name' : full_name,
          'email':email,
          'mobile_number':mobile_number,
          'subject':subject,
          'message':message
        }
        save_data = Contact_us(
            contact_id=contact_id,
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            subject=subject,
            message = message,
        )
        if(not full_name):
            error_message = "Full Name is Required !!"
        elif not email:
            error_message = "Email is Required !!"
        elif not mobile_number:
            error_message = "Mobile No. is Required !!"
        elif not subject:
            error_message = "Subject is Required !!"
        elif not message:
            error_message = "Write some Message !!"
        if not error_message:
            save_data.save()
            messages.success(request, 'Your Response Submitted Successfully')
            return redirect('/#contact_us')
    data={
        'value':value,
        'error':error_message,
    }
    return render(request,'Main/homepage.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= News Page =================================================
def news(request):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()

    data={
        'count':count,
    }
    return render(request,'Main/latest_updates.html',data)
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= News Detail Page ==========================================
def news_details(request):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWAREDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result)==1:
        print('User Exist')
    elif len(result)>1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count=Visitor_IP.objects.all().count()

    data={
        'count':count,
    }
    return render(request,'Main/news_details.html',data)
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


def generate_admission_roll_number():
    last_roll_number = Admission_Registration.objects.order_by('-id').first()
    if last_roll_number:
        last_roll_number = int(last_roll_number.registration_number)
        new_roll_number = str(last_roll_number + 1)
    else:
        new_roll_number = '555501038'
    return new_roll_number


def generate_vtc_roll_number():
    last_roll_number = VTC_Course_Admission_Registration.objects.order_by('-id').first()
    if last_roll_number:
        last_roll_number = int(last_roll_number.registration_number)
        new_roll_number = str(last_roll_number + 1)
    else:
        new_roll_number = '900363385'
    return new_roll_number

#===================================================================================================
#======================================= Admission Registration Page ===============================
@login_required
def vtc_course_admission(request):
    all_college_name = College_Name.objects.all()
    all_course_name = Course_Name.objects.all()
    all_status = Status.objects.all()
    reg_id = random.randint(00000000, 99999999)
    while Admission_Registration.objects.filter(registration_number=reg_id).exists():
        reg_id = random.randint(00000000, 99999999)
    

    registrationNum=request.POST.get("registrationNum")
    nameOfStudent=request.POST.get("nameOfStudent")
    address=request.POST.get("address")
    idNumber=request.POST.get("idNumber")
    date=request.POST.get("date")
    mobileNumber=request.POST.get("mobileNumber")
    collegeName=request.POST.get("collegeName")
    district=request.POST.get("district")
    courseName=request.POST.get("courseName")
    admissionFees=request.POST.get("admissionFees")
    admission_date=request.POST.get("admission_date")
    principalApproval=request.POST.get("principalApproval")

    if registrationNum and nameOfStudent and address and idNumber and date and mobileNumber and collegeName and district and courseName and admissionFees and admission_date and principalApproval:
        college_name_id=College_Name.objects.get(id=collegeName)
        course_name_id=Course_Name.objects.get(id=courseName)
        principal_approval_id=Status.objects.get(id=principalApproval)
        
        add_vtc_course_admission_registration = VTC_Course_Admission_Registration(
            registration_number = generate_vtc_roll_number(),
            name_of_student = nameOfStudent,
            address = address,
            id_number = idNumber,
            date_of_birth = date,
            mobile_number = mobileNumber,
            college_name = college_name_id,
            district = district,
            course_name = course_name_id,
            admission_fees = admissionFees,
            admission_date = admission_date,
            principal_approval = principal_approval_id,
        )

        add_vtc_course_admission_registration.save()
        return HttpResponse("Save")
    data = {
        'all_college_name':all_college_name,
        'all_course_name':all_course_name,
        'all_status':all_status,
        'reg_id':generate_vtc_roll_number(),
    }
    return render(request,'internal/vtc_course_admission.html',data)
#===================================================================================================
#===================================================================================================





#===================================================================================================
#======================================= Admission Registration Page ===============================
@login_required
def admission_registration(request):
    all_college_name = College_Name.objects.all()
    all_course_name = Course_Name.objects.all()
    all_status = Status.objects.all()
    reg_id = random.randint(00000000, 99999999)
    while Admission_Registration.objects.filter(registration_number=reg_id).exists():
        reg_id = random.randint(00000000, 99999999)
    

    registrationNum=request.POST.get("registrationNum")
    nameOfStudent=request.POST.get("nameOfStudent")
    address=request.POST.get("address")
    idNumber=request.POST.get("idNumber")
    date=request.POST.get("date")
    mobileNumber=request.POST.get("mobileNumber")
    collegeName=request.POST.get("collegeName")
    district=request.POST.get("district")
    courseName=request.POST.get("courseName")
    admissionFees=request.POST.get("admissionFees")
    admission_date=request.POST.get("admission_date")
    principalApproval=request.POST.get("principalApproval")

    if registrationNum and nameOfStudent and address and idNumber and date and mobileNumber and collegeName and district and courseName and admissionFees and admission_date and principalApproval:
        college_name_id=College_Name.objects.get(id=collegeName)
        course_name_id=Course_Name.objects.get(id=courseName)
        principal_approval_id=Status.objects.get(id=principalApproval)
        
        add_admission_registration = Admission_Registration(
            registration_number = generate_admission_roll_number(),
            name_of_student = nameOfStudent,
            address = address,
            id_number = idNumber,
            date_of_birth = date,
            mobile_number = mobileNumber,
            college_name = college_name_id,
            district = district,
            course_name = course_name_id,
            admission_fees = admissionFees,
            admission_date = admission_date,
            principal_approval = principal_approval_id,
        )

        add_admission_registration.save()
        return HttpResponse("Save")
    data = {
        'all_college_name':all_college_name,
        'all_course_name':all_course_name,
        'all_status':all_status,
        'reg_id':generate_admission_roll_number(),
    }
    return render(request,'internal/admission_registration.html',data)
#===================================================================================================
#===================================================================================================





#===================================================================================================
#======================================= Exam Registration Page ====================================
@login_required
def exam_registration(request):
    all_status = Status.objects.all()
    all_exam_fee = Exam_Fees_Type.objects.all()
    search_student_data = ''
    search_student_data_error = ''
    register_number_allready=""
    get_search_registration_number = None
    exmd=None
    if request.method=='GET':
        get_search_registration_number=request.GET.get("search_registration_number")
        if get_search_registration_number:
            admissions = Admission_Registration.objects.filter(registration_number=get_search_registration_number).first()
            vtc_admissions = VTC_Course_Admission_Registration.objects.filter(registration_number=get_search_registration_number).first()
            exmd = Exam_Registration.objects.filter(registration_number=get_search_registration_number).first()
            if exmd:
                register_number_allready="Registration Number already exist in Mark Registration !!"
            if admissions:
                search_student_data = admissions
            elif vtc_admissions:
                search_student_data = vtc_admissions
            else:
                search_student_data_error = "Invalid Registration Number!"



    registration_number=request.POST.get("send_registration_number")
    exam_fees=request.POST.get("send_exam_fees")
    exam_attendance=request.POST.get("send_exam_attendance")
    any_fees_concession=request.POST.get("send_any_fees_concession")
    date=request.POST.get("send_date")
    principal_code=request.POST.get("send_principal_code")
    principal_name=request.POST.get("send_principal_name")
    online_fees=request.POST.get("send_online_fees")
    remark=request.POST.get("send_remark")
    principal_approval=request.POST.get("send_principal_approval")


    if registration_number and exam_fees and exam_attendance and any_fees_concession and date and principal_code and \
        principal_name and online_fees and remark and principal_approval:
        exam_fee_id=Exam_Fees_Type.objects.get(id=exam_fees)
        principal_approval_id=Status.objects.get(id=principal_approval)
        regiter_number_checking=Exam_Registration.objects.filter(registration_number=registration_number).first()
        if regiter_number_checking:
            
            regiter_number_checking.registration_number = registration_number
            regiter_number_checking.exam_fees = exam_fee_id
            regiter_number_checking.exam_attendance = exam_attendance
            regiter_number_checking.any_fees_concession = any_fees_concession
            regiter_number_checking.date = date
            regiter_number_checking.principal_code = principal_code
            regiter_number_checking.principal_name = principal_name
            regiter_number_checking.online_fees = online_fees
            regiter_number_checking.remark = remark
            regiter_number_checking.principal_approval = principal_approval_id
            regiter_number_checking.save()
            return HttpResponse("Save")
            
        else:
            add_exam_registration = Exam_Registration(
                registration_number = registration_number,
                exam_fees = exam_fee_id,
                exam_attendance = exam_attendance,
                any_fees_concession = any_fees_concession,
                date = date,
                principal_code = principal_code,
                principal_name = principal_name,
                online_fees = online_fees,
                remark = remark,
                principal_approval = principal_approval_id,
            )

            add_exam_registration.save()
            return HttpResponse("Save")
    data = {
        'all_status':all_status,
        'all_exam_fee':all_exam_fee,
        'search_student_data':search_student_data,
        'search_student_data_error':search_student_data_error,
        'get_search_registration_number':get_search_registration_number,
        "register_number_allready":register_number_allready,
        "exmd":exmd

    }
    return render(request,'internal/exam_registration.html',data)

#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Mark Registration Page ====================================
@login_required
def mark_registration(request):
    all_mark_enter_clerk = Mark_Status.objects.all()
    all_result_status = Result_Status.objects.all()
    search_student_data = ''
    search_get_exam = ''
    search_student_data_error = ''
    admissionsFormdata=None
    register_number_allready=""
    get_search_registration_number=request.GET.get("search_registration_number")
    if get_search_registration_number:
        admissions = Admission_Registration.objects.filter(registration_number=get_search_registration_number).first()
        get_exam = Exam_Registration.objects.filter(registration_number=get_search_registration_number).first()
        admissionsFormdata = Mark_List_Registration.objects.filter(registration_number=get_search_registration_number).first()
        vtc_admissions = VTC_Course_Admission_Registration.objects.filter(registration_number=get_search_registration_number).first()

        if admissionsFormdata:
            register_number_allready="Registration Number already exist in Mark Registration !!"
        if admissions:
            search_student_data = admissions
            search_get_exam = get_exam
        elif vtc_admissions:
            search_student_data = vtc_admissions
        else:
            search_student_data_error = "Invalid Registration Number!"

       
            
    
    get_registration_number_offix=request.POST.get("get_registration_number_offix")
    send_total_mark_2=request.POST.get("send_total_mark_2")
    mark_enter_clerk_name=request.POST.get("send_mark_enter_clerk_name")
    mark_enter_clerk=request.POST.get("send_mark_enter_clerk")
    mark_check_clerk_name=request.POST.get("send_mark_check_clerk_name")
    send_mark_check_clerk0=request.POST.get("send_mark_check_clerk0")
    second_verified_officer_name=request.POST.get("send_second_verified_officer_name")
    second_verified_officer=request.POST.get("send_second_verified_officer")
    final_mark_verified_officer_name=request.POST.get("send_final_mark_verified_officer_name")
    result_status=request.POST.get("send_result_status")
    result_enter_register_book_number=request.POST.get("send_result_enter_register_book_number")
    mark_obtained=request.POST.get("send_mark_obtained")
    total_mark_2=request.POST.get("send_total_mark_2")


    if get_registration_number_offix and send_total_mark_2 and mark_enter_clerk_name and mark_enter_clerk and \
        mark_check_clerk_name and send_mark_check_clerk0 and second_verified_officer_name and \
        second_verified_officer and final_mark_verified_officer_name and result_status and\
        result_enter_register_book_number and mark_obtained and total_mark_2:
        
    
        geting_number_rnd= Mark_List_Registration.objects.get(registration_number=get_registration_number_offix)
        if geting_number_rnd:
            mark_enter_clerk = Mark_Status.objects.get(id=mark_enter_clerk) #select option filed
            mark_check_clerk =Mark_Status.objects.get(id=send_mark_check_clerk0)
            second_verified_officer = Mark_Status.objects.get(id=second_verified_officer)
            result_status = Result_Status.objects.get(id=result_status) 
            # Update the fields
            geting_number_rnd.total_mark_1 = send_total_mark_2
            geting_number_rnd.mark_enter_clerk_name = mark_enter_clerk_name
            geting_number_rnd.mark_enter_clerk = mark_enter_clerk
            geting_number_rnd.mark_check_clerk_name = mark_check_clerk_name
            geting_number_rnd.mark_check_clerk = mark_check_clerk
            geting_number_rnd.second_verified_officer_name = second_verified_officer_name
            geting_number_rnd.second_verified_officer = second_verified_officer
            geting_number_rnd.final_mark_verified_officer_name = final_mark_verified_officer_name
            geting_number_rnd.result_status = result_status
            geting_number_rnd.result_enter_register_book_number = result_enter_register_book_number
            geting_number_rnd.mark_obtained = mark_obtained
            geting_number_rnd.total_mark_2 = total_mark_2

            # Save the changes
            geting_number_rnd.save()
            return HttpResponse("Save")
        else:
            new_user=Mark_List_Registration(
                total_mark_1 = send_total_mark_2,
                mark_enter_clerk_name = mark_enter_clerk_name,
                mark_enter_clerk = mark_enter_clerk,
                mark_check_clerk_name = mark_check_clerk_name,
                mark_check_clerk = mark_check_clerk,
                second_verified_officer_name = second_verified_officer_name,
                second_verified_officer = second_verified_officer,
                final_mark_verified_officer_name = final_mark_verified_officer_name,
                result_status = result_status,
                result_enter_register_book_number = result_enter_register_book_number,
                mark_obtained = mark_obtained,
                total_mark_2 = total_mark_2
            )
            new_user.save,()
            return HttpResponse("Save")



    registration_number=request.POST.get("send_registration_number")
    date=request.POST.get("send_date")
    subject_1=request.POST.get("send_subject_1")
    subject_2=request.POST.get("send_subject_2")
    subject_3=request.POST.get("send_subject_3")
    subject_4=request.POST.get("send_subject_4")
    subject_5=request.POST.get("send_subject_5")
    subject_6=request.POST.get("send_subject_6")
    subject_7=request.POST.get("send_subject_7")
    subject_8=request.POST.get("send_subject_8")
    subject_9=request.POST.get("send_subject_9")
    subject_10=request.POST.get("send_subject_10")
    subject_11=request.POST.get("send_subject_11")
    subject_12=request.POST.get("send_subject_12")
    internal_marks_1=request.POST.get("send_internal_marks_1")
    internal_marks_2=request.POST.get("send_internal_marks_2")
    internal_marks_3=request.POST.get("send_internal_marks_3")
    internal_marks_4=request.POST.get("send_internal_marks_4")
    internal_marks_5=request.POST.get("send_internal_marks_5")
    print(internal_marks_5,'')
    internal_marks_6=request.POST.get("send_internal_marks_6")
    internal_marks_7=request.POST.get("send_internal_marks_7")
    internal_marks_8=request.POST.get("send_internal_marks_8")
    internal_marks_9=request.POST.get("send_internal_marks_9")
    internal_marks_10=request.POST.get("send_internal_marks_10")
    internal_marks_11=request.POST.get("send_internal_marks_11")
    internal_marks_12=request.POST.get("send_internal_marks_12")
    internal_marks_13=request.POST.get("send_internal_marks_13")
    internal_marks_14=request.POST.get("send_internal_marks_14")
    external_marks_1=request.POST.get("send_external_marks_1")
    external_marks_2=request.POST.get("send_external_marks_2")
    external_marks_3=request.POST.get("send_external_marks_3")
    external_marks_4=request.POST.get("send_external_marks_4")
    external_marks_5=request.POST.get("send_external_marks_5")
    external_marks_6=request.POST.get("send_external_marks_6")
    external_marks_7=request.POST.get("send_external_marks_7")
    external_marks_8=request.POST.get("send_external_marks_8")
    external_marks_9=request.POST.get("send_external_marks_9")
    external_marks_10=request.POST.get("send_external_marks_10")
    external_marks_11=request.POST.get("send_external_marks_11")
    external_marks_12=request.POST.get("send_external_marks_12")
    external_marks_13=request.POST.get("send_external_marks_13")
    external_marks_14=request.POST.get("send_external_marks_14")
    mark_obtained_1=request.POST.get("send_mark_obtained_1")
    mark_obtained_2=request.POST.get("send_mark_obtained_2")
    mark_obtained_3=request.POST.get("send_mark_obtained_3")
    mark_obtained_4=request.POST.get("send_mark_obtained_4")
    mark_obtained_5=request.POST.get("send_mark_obtained_5")
    mark_obtained_6=request.POST.get("send_mark_obtained_6")
    mark_obtained_7=request.POST.get("send_mark_obtained_7")
    mark_obtained_8=request.POST.get("send_mark_obtained_8")
    mark_obtained_9=request.POST.get("send_mark_obtained_9")
    mark_obtained_10=request.POST.get("send_mark_obtained_10")
    mark_obtained_11=request.POST.get("send_mark_obtained_11")
    mark_obtained_12=request.POST.get("send_mark_obtained_12")
    mark_obtained_13=request.POST.get("send_mark_obtained_13")
    mark_obtained_14=request.POST.get("send_mark_obtained_14")
    total_1=request.POST.get("send_total_1")
    total_2=request.POST.get("send_total_2")
    total_3=request.POST.get("send_total_3")
    total_4=request.POST.get("send_total_4")
    total_5=request.POST.get("send_total_5")
    total_6=request.POST.get("send_total_6")
    total_7=request.POST.get("send_total_7")
    total_8=request.POST.get("send_total_8")
    total_9=request.POST.get("send_total_9")
    total_10=request.POST.get("send_total_10")
    total_11=request.POST.get("send_total_11")
    total_12=request.POST.get("send_total_12")
    total_13=request.POST.get("send_total_13")
    total_14=request.POST.get("send_total_14")
    total_mark_1=request.POST.get("send_total_mark_1")
    total_mark_obtained=request.POST.get("send_total_mark_obtained")
    
    grade_1=request.POST.get("send_grade_1")
    grade_2=request.POST.get("send_grade_2")
    grade_3=request.POST.get("send_grade_3")
    grade_4=request.POST.get("send_grade_4")
    grade_5=request.POST.get("send_grade_5")
    grade_6=request.POST.get("send_grade_6")
    grade_7=request.POST.get("send_grade_7")
    grade_8=request.POST.get("send_grade_8")
    grade_9=request.POST.get("send_grade_9")
    grade_10=request.POST.get("send_grade_10")
    grade_11=request.POST.get("send_grade_11")
    grade_12=request.POST.get("send_grade_12")
    grade_13=request.POST.get("send_grade_13")
    grade_14=request.POST.get("send_grade_14")


    if registration_number and date and subject_1 and internal_marks_1 and external_marks_1 and mark_obtained_1 and \
        total_1 and grade_1 :
        pc_geting_number_rnd=Mark_List_Registration.objects.filter(registration_number=registration_number).first()

        if pc_geting_number_rnd:
            pc_geting_number_rnd.date=date
            pc_geting_number_rnd.subject_1=subject_1
            pc_geting_number_rnd.subject_2=subject_2
            pc_geting_number_rnd.subject_3=subject_3
            pc_geting_number_rnd.subject_4=subject_4
            pc_geting_number_rnd.subject_5=subject_5
            pc_geting_number_rnd.subject_6=subject_6
            pc_geting_number_rnd.subject_7=subject_7
            pc_geting_number_rnd.subject_8=subject_8
            pc_geting_number_rnd.subject_9=subject_9
            pc_geting_number_rnd.subject_10=subject_10
            pc_geting_number_rnd.subject_11=subject_11
            pc_geting_number_rnd.subject_12=subject_12
            pc_geting_number_rnd.internal_marks_1=internal_marks_1
            pc_geting_number_rnd.internal_marks_2=internal_marks_2
            pc_geting_number_rnd.internal_marks_3=internal_marks_3
            pc_geting_number_rnd.internal_marks_4=internal_marks_4
            pc_geting_number_rnd.internal_marks_5=internal_marks_5
            pc_geting_number_rnd.internal_marks_6=internal_marks_6
            pc_geting_number_rnd.internal_marks_7=internal_marks_7
            pc_geting_number_rnd.internal_marks_8=internal_marks_8
            pc_geting_number_rnd.internal_marks_9=internal_marks_9
            pc_geting_number_rnd.internal_marks_10=internal_marks_10
            pc_geting_number_rnd.internal_marks_11=internal_marks_11
            pc_geting_number_rnd.internal_marks_12=internal_marks_12
            pc_geting_number_rnd.internal_marks_13=internal_marks_13
            pc_geting_number_rnd.internal_marks_14=internal_marks_14
            pc_geting_number_rnd.external_marks_1=external_marks_1
            pc_geting_number_rnd.external_marks_2=external_marks_2
            pc_geting_number_rnd.external_marks_3=external_marks_3
            pc_geting_number_rnd.external_marks_4=external_marks_4
            pc_geting_number_rnd.external_marks_5=external_marks_5
            pc_geting_number_rnd.external_marks_6=external_marks_6
            pc_geting_number_rnd.external_marks_7=external_marks_7
            pc_geting_number_rnd.external_marks_8=external_marks_8
            pc_geting_number_rnd.external_marks_9=external_marks_9
            pc_geting_number_rnd.external_marks_10=external_marks_10
            pc_geting_number_rnd.external_marks_11=external_marks_11
            pc_geting_number_rnd.external_marks_12=external_marks_12
            pc_geting_number_rnd.external_marks_13=external_marks_13
            pc_geting_number_rnd.external_marks_14=external_marks_14
            pc_geting_number_rnd.mark_obtained_1=mark_obtained_1
            pc_geting_number_rnd.mark_obtained_2=mark_obtained_2
            pc_geting_number_rnd.mark_obtained_3=mark_obtained_3
            pc_geting_number_rnd.mark_obtained_4=mark_obtained_4
            pc_geting_number_rnd.mark_obtained_5=mark_obtained_5
            pc_geting_number_rnd.mark_obtained_6=mark_obtained_6
            pc_geting_number_rnd.mark_obtained_7=mark_obtained_7
            pc_geting_number_rnd.mark_obtained_8=mark_obtained_8
            pc_geting_number_rnd.mark_obtained_9=mark_obtained_9
            pc_geting_number_rnd.mark_obtained_10=mark_obtained_10
            pc_geting_number_rnd.mark_obtained_11=mark_obtained_11
            pc_geting_number_rnd.mark_obtained_12=mark_obtained_12
            pc_geting_number_rnd.mark_obtained_13=mark_obtained_13
            pc_geting_number_rnd.mark_obtained_14=mark_obtained_14
            pc_geting_number_rnd.total_1=total_1
            pc_geting_number_rnd.total_2=total_2
            pc_geting_number_rnd.total_3=total_3
            pc_geting_number_rnd.total_4=total_4
            pc_geting_number_rnd.total_5=total_5
            pc_geting_number_rnd.total_6=total_6
            pc_geting_number_rnd.total_7=total_7
            pc_geting_number_rnd.total_8=total_8
            pc_geting_number_rnd.total_9=total_9
            pc_geting_number_rnd.total_10=total_10
            pc_geting_number_rnd.total_11=total_11
            pc_geting_number_rnd.total_12=total_12
            pc_geting_number_rnd.total_13=total_13
            pc_geting_number_rnd.total_14=total_14

            pc_geting_number_rnd.total_mark_1=total_mark_1
            pc_geting_number_rnd.total_mark_obtained=total_mark_obtained
           
            pc_geting_number_rnd.grade_1=grade_1
            pc_geting_number_rnd.grade_2=grade_2
            pc_geting_number_rnd.grade_3=grade_3
            pc_geting_number_rnd.grade_4=grade_4
            pc_geting_number_rnd.grade_5=grade_5
            pc_geting_number_rnd.grade_6=grade_6
            pc_geting_number_rnd.grade_7=grade_7
            pc_geting_number_rnd.grade_8=grade_8
            pc_geting_number_rnd.grade_9=grade_9
            pc_geting_number_rnd.grade_10=grade_10
            pc_geting_number_rnd.grade_11=grade_11
            pc_geting_number_rnd.grade_12=grade_12
            pc_geting_number_rnd.grade_13=grade_13
            pc_geting_number_rnd.grade_14=grade_14
            pc_geting_number_rnd.save()
            return HttpResponse("Save")
        
        else:
            add_mark_registration = Mark_List_Registration(
                registration_number=registration_number,
                date=date,
                subject_1=subject_1,
                subject_2=subject_2,
                subject_3=subject_3,
                subject_4=subject_4,
                subject_5=subject_5,
                subject_6=subject_6,
                subject_7=subject_7,
                subject_8=subject_8,
                subject_9=subject_9,
                subject_10=subject_10,
                subject_11=subject_11,
                subject_12=subject_12,
                internal_marks_1=internal_marks_1 if internal_marks_1 else 0,
                internal_marks_2=internal_marks_2 if internal_marks_2 else 0,
                internal_marks_3=internal_marks_3 if internal_marks_3 else 0,
                internal_marks_4=internal_marks_4 if internal_marks_4 else 0,
                internal_marks_5=internal_marks_5 if internal_marks_5 else 0,
                internal_marks_6=internal_marks_6 if internal_marks_6 else 0,
                internal_marks_7=internal_marks_7 if internal_marks_7 else 0,
                internal_marks_8=internal_marks_8 if internal_marks_8 else 0,
                internal_marks_9=internal_marks_9 if internal_marks_9 else 0,
                internal_marks_10=internal_marks_10 if internal_marks_10 else 0,
                internal_marks_11=internal_marks_11 if internal_marks_11 else 0,
                internal_marks_12=internal_marks_12 if internal_marks_12 else 0,
                internal_marks_13=internal_marks_13 if internal_marks_13 else 0,
                internal_marks_14=internal_marks_14 if internal_marks_14 else 0,
                external_marks_1=external_marks_1 if external_marks_1 else 0,
                external_marks_2=external_marks_2 if external_marks_2 else 0,
                external_marks_3=external_marks_3 if external_marks_3 else 0,
                external_marks_4=external_marks_4 if external_marks_4 else 0,
                external_marks_5=external_marks_5 if external_marks_5 else 0,
                external_marks_6=external_marks_6 if external_marks_6 else 0,
                external_marks_7=external_marks_7 if external_marks_7 else 0,
                external_marks_8=external_marks_8 if external_marks_8 else 0,
                external_marks_9=external_marks_9 if external_marks_9 else 0,
                external_marks_10=external_marks_10 if external_marks_10 else 0,
                external_marks_11=external_marks_11 if external_marks_11 else 0,
                external_marks_12=external_marks_12 if external_marks_12 else 0,
                external_marks_13=external_marks_13 if external_marks_13 else 0,
                external_marks_14=external_marks_14 if external_marks_14 else 0,
                mark_obtained_1=mark_obtained_1 if mark_obtained_1 else 0,
                mark_obtained_2=mark_obtained_2 if mark_obtained_2 else 0,
                mark_obtained_3=mark_obtained_3 if mark_obtained_3 else 0,
                mark_obtained_4=mark_obtained_4 if mark_obtained_4 else 0,
                mark_obtained_5=mark_obtained_5 if mark_obtained_5 else 0,
                mark_obtained_6=mark_obtained_6 if mark_obtained_6 else 0,
                mark_obtained_7=mark_obtained_7 if mark_obtained_7 else 0,
                mark_obtained_8=mark_obtained_8 if mark_obtained_8 else 0,
                mark_obtained_9=mark_obtained_9 if mark_obtained_9 else 0,
                mark_obtained_10=mark_obtained_10 if mark_obtained_10 else 0,
                mark_obtained_11=mark_obtained_11 if mark_obtained_11 else 0,
                mark_obtained_12=mark_obtained_12 if mark_obtained_12 else 0,
                mark_obtained_13=mark_obtained_13 if mark_obtained_13 else 0,
                mark_obtained_14=mark_obtained_14 if mark_obtained_14 else 0,
                total_1=total_1 if total_1 else 0,
                total_2=total_2 if total_2 else 0,
                total_3=total_3 if total_3 else 0,
                total_4=total_4 if total_4 else 0,
                total_5=total_5 if total_5 else 0,
                total_6=total_6 if total_6 else 0,
                total_7=total_7 if total_7 else 0,
                total_8=total_8 if total_8 else 0,
                total_9=total_9 if total_9 else 0,
                total_10=total_10 if total_10 else 0,
                total_11=total_11 if total_11 else 0,
                total_12=total_12 if total_12 else 0,
                total_13=total_13 if total_13 else 0,
                total_14=total_14 if total_14 else 0,
                total_mark_1=total_mark_1 if total_mark_1 else 0,
                total_mark_obtained=total_mark_obtained if total_mark_obtained else 0,            
                grade_1=grade_1,
                grade_2=grade_2,
                grade_3=grade_3,
                grade_4=grade_4,
                grade_5=grade_5,
                grade_6=grade_6,
                grade_7=grade_7,
                grade_8=grade_8,
                grade_9=grade_9,
                grade_10=grade_10,
                grade_11=grade_11,
                grade_12=grade_12,
                grade_13=grade_13,
                grade_14=grade_14,
            )
            add_mark_registration.save()
            return HttpResponse("Save")


    data = {
        'all_mark_enter_clerk':all_mark_enter_clerk,
        'all_result_status':all_result_status,
        'search_student_data':search_student_data,
        'search_get_exam':search_get_exam,
        'search_student_data_error':search_student_data_error,
        'get_search_registration_number':get_search_registration_number,
        "admissionsFormdata":admissionsFormdata,
        "register_number_allready":register_number_allready
    }
    return render(request,'internal/mark_registration.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Add on Programme Page =====================================
@login_required
def add_on_programme(request):
    all_college_name = Add_on_College.objects.all()
    all_course_name = Course_Name.objects.all()
    all_status = Status.objects.all()
    all_main_course = Main_Course.objects.all()
   
    college_id = request.POST.get('collegeId0')
    course_id = request.POST.get('courseId0')
    course_code = request.POST.get('courseCode0')
    student_name = request.POST.get('studentName0')
    address = request.POST.get('address0')
    id_number = request.POST.get('idNumber0')
    contact_number = request.POST.get('contactNumber0')
    exam_fees = request.POST.get('examFees0')
    amount = request.POST.get('amount0')
    main_course_id = request.POST.get('mainCourseId0')
    college_status_id = request.POST.get('collegeStatusId0')

    if college_id and course_id and course_code and student_name and address and id_number and contact_number and exam_fees and amount and main_course_id and college_status_id:
        add_on_college0 = Add_on_College.objects.get(id=college_id)
        course_name = Course_Name.objects.get(id=course_id)
        main_course = Main_Course.objects.get(id=main_course_id)
        college_coordinator_approval = Status.objects.get(id=college_status_id)

        add_on_programme = Add_on_Programme(
            add_on_College=add_on_college0,
            course_name=course_name,
            course_code=course_code,
            student_name=student_name,
            address=address,
            id_number=id_number,
            contact_number=contact_number,
            exam_fees=exam_fees,
            amount=amount,
            main_course=main_course,
            college_coordinator_approval=college_coordinator_approval,
        )
        add_on_programme.save()
        return HttpResponse("Save")


    data = {
        'all_college_name':all_college_name,
        'all_course_name':all_course_name,
        'all_status':all_status,
        'all_main_course':all_main_course,
    }

    return render(request,'internal/add_on_programme.html',data)
#===================================================================================================

#===================================================================================================



#===================================================================================================
#======================================= Application For Affiliation Page ==========================
@login_required
def application_for_affiliation(request):
    all_institution_status = Institution_Status.objects.all()
    payment_status = Amount_Status.objects.all()
    
    name_of_institution=request.POST.get("name_of_institution")
    mobile_number=request.POST.get("mobile_number")
    status_of_institution=request.POST.get("status_of_institution")
    email=request.POST.get("email")
    status_of_institution_other=request.POST.get("status_of_institution_other")
    year_of_establishment=request.POST.get("year_of_establishment")
    address=request.POST.get("address")
    pincode=request.POST.get("pincode")
    name_mpd=request.POST.get("name_mpd")
    education_qualification=request.POST.get("education_qualification")
    date_of_birth=request.POST.get("date_of_birth")
    designation=request.POST.get("designation")
    profession_experience=request.POST.get("profession_experience")
    postal_address=request.POST.get("postal_address")
    number_of_room_1=request.POST.get("number_of_room_1")
    seating_capacity_1=request.POST.get("seating_capacity_1")
    total_area_1=request.POST.get("total_area_1")
    number_of_room_2=request.POST.get("number_of_room_2")
    seating_capacity_2=request.POST.get("seating_capacity_2")
    total_area_2=request.POST.get("total_area_2")
    number_of_room_3=request.POST.get("number_of_room_3")
    seating_capacity_3=request.POST.get("seating_capacity_3")
    total_area_3=request.POST.get("total_area_3")
    number_of_room_4=request.POST.get("number_of_room_4")
    seating_capacity_4=request.POST.get("seating_capacity_4")
    total_area_4=request.POST.get("total_area_4")
    number_of_room_5=request.POST.get("number_of_room_5")
    seating_capacity_5=request.POST.get("seating_capacity_5")
    total_area_5=request.POST.get("total_area_5")
    number_of_room_6=request.POST.get("number_of_room_6")
    seating_capacity_6=request.POST.get("seating_capacity_6")
    total_area_6=request.POST.get("total_area_6")


    serial_number1=request.POST.get("serial_number1")
    type_of_computer_1=request.POST.get("type_of_computer_1")
    number_terminal_1=request.POST.get("number_terminal_1")
    year_of_purchase_1=request.POST.get("year_of_purchase_1")
    cost_1=request.POST.get("cost_1")
    software_facility_1=request.POST.get("software_facility_1")
    other_facility_1=request.POST.get("other_facility_1")
    serial_number2=request.POST.get("serial_number2")
    type_of_computer_2=request.POST.get("type_of_computer_2")
    number_terminal_2=request.POST.get("number_terminal_2")
    year_of_purchase_2=request.POST.get("year_of_purchase_2")
    cost_2=request.POST.get("cost_2")
    software_facility_2=request.POST.get("software_facility_2")
    other_facility_2=request.POST.get("other_facility_2")
    serial_number3=request.POST.get("serial_number3")
    type_of_computer_3=request.POST.get("type_of_computer_3")
    number_terminal_3=request.POST.get("number_terminal_3")
    year_of_purchase_3=request.POST.get("year_of_purchase_3")
    cost_3=request.POST.get("cost_3")
    software_facility_3=request.POST.get("software_facility_3")
    other_facility_3=request.POST.get("other_facility_3")
    serial_number4=request.POST.get("serial_number4")
    type_of_computer_4=request.POST.get("type_of_computer_4")
    number_terminal_4=request.POST.get("number_terminal_4")
    year_of_purchase_4=request.POST.get("year_of_purchase_4")
    cost_4=request.POST.get("cost_4")
    software_facility_4=request.POST.get("software_facility_4")
    other_facility_4=request.POST.get("other_facility_4")
    serial_number5=request.POST.get("serial_number_5")
    type_of_computer_5=request.POST.get("type_of_computer_5")
    number_terminal_5=request.POST.get("number_terminal_5")
    year_of_purchase_5=request.POST.get("year_of_purchase_5")
    cost_5=request.POST.get("cost_5")
    software_facility_5=request.POST.get("software_facility_5")
    other_facility_5=request.POST.get("other_facility_5")
    serial_number6=request.POST.get("serial_number_6")
    type_of_computer_6=request.POST.get("type_of_computer_6")
    number_terminal_6=request.POST.get("number_terminal_6")
    year_of_purchase_6=request.POST.get("year_of_purchase_6")
    cost_6=request.POST.get("cost_6")
    software_facility_6=request.POST.get("software_facility_6")
    other_facility_6=request.POST.get("other_facility_6")


    information_serial_number_1=request.POST.get("information_serial_number_1")
    name_1=request.POST.get("name_1")
    designation_1=request.POST.get("designation_1")
    qualification_1=request.POST.get("qualification_1")
    teaching_experience_1=request.POST.get("teaching_experience_1")
    date_of_appointment_1=request.POST.get("date_of_appointment_1")
    status_1=request.POST.get("status_1")
    information_serial_number_2=request.POST.get("information_serial_number_2")
    name_2=request.POST.get("name_2")
    designation_2=request.POST.get("designation_2")
    qualification_2=request.POST.get("qualification_2")
    teaching_experience_2=request.POST.get("teaching_experience_2")
    date_of_appointment_2=request.POST.get("date_of_appointment_2")
    status_2=request.POST.get("status_2")
    information_serial_number_3=request.POST.get("information_serial_number_3")
    name_3=request.POST.get("name_3")
    designation_3=request.POST.get("designation_3")
    qualification_3=request.POST.get("qualification_3")
    teaching_experience_3=request.POST.get("teaching_experience_3")
    date_of_appointment_3=request.POST.get("date_of_appointment_3")
    status_3=request.POST.get("status_3")
    information_serial_number_4=request.POST.get("information_serial_number_4")
    name_4=request.POST.get("name_4")
    designation_4=request.POST.get("designation_4")
    qualification_4=request.POST.get("qualification_4")
    teaching_experience_4=request.POST.get("teaching_experience_4")
    date_of_appointment_4=request.POST.get("date_of_appointment_4")
    status_4=request.POST.get("status_4")
    center_address=request.POST.get("center_address")
    residential_address=request.POST.get("residential_address")
    signature=request.POST.get("signature")
    form_receive_date=request.POST.get("form_receive_date")
    affliation_number=request.POST.get("affliation_number")
    total_affliation_fee=request.POST.get("total_affliation_fee")
    registration_fee=request.POST.get("registration_fee")
    amount_status=request.POST.get("amount_status")
    bank_name=request.POST.get("bank_name")
    receipt_number=request.POST.get("receipt_number")
    date=request.POST.get("date")
    education_institution_type=request.POST.get("education_institution_type")
    affliation_from_date=request.POST.get("affliation_from_date")
    affliation_to_date=request.POST.get("affliation_to_date")


    variables = [
        name_of_institution, mobile_number, status_of_institution, email, year_of_establishment,
        address, pincode, name_mpd, education_qualification, date_of_birth, designation, profession_experience,
        postal_address, number_of_room_1, seating_capacity_1, total_area_1, number_of_room_2, seating_capacity_2,
        total_area_2, number_of_room_3, seating_capacity_3, total_area_3, number_of_room_4, seating_capacity_4,
        total_area_4, number_of_room_5, seating_capacity_5, total_area_5, number_of_room_6, seating_capacity_6,
        total_area_6, serial_number1, type_of_computer_1, number_terminal_1, year_of_purchase_1, cost_1,
        software_facility_1, other_facility_1,information_serial_number_1, name_1, designation_1, qualification_1, teaching_experience_1,
        date_of_appointment_1, status_1,center_address,residential_address, signature, form_receive_date, affliation_number, total_affliation_fee, registration_fee,
        amount_status, bank_name, receipt_number, date, education_institution_type, affliation_from_date,
        affliation_to_date,
    ]

    all_variables_have_value = all(variables)

    if all_variables_have_value:
        status_of_institution = Institution_Status.objects.get(id=status_of_institution) #select option filed
        amount_status =Amount_Status.objects.get(id=amount_status) 
        
        application = Application_for_Affliation(
            name_of_institution=name_of_institution,
            mobile_number=mobile_number,
            status_of_institution=status_of_institution,
            email=email,
            status_of_institution_other=status_of_institution_other,
            year_of_establishment=year_of_establishment,
            address=address,
            pincode=pincode,
            name=name_mpd,
            education_qualification=education_qualification,
            date_of_birth=date_of_birth,
            designation=designation,
            profession_experience=profession_experience,
            postal_address=postal_address,


            number_of_room_1=number_of_room_1,
            seating_capacity_1=seating_capacity_1,
            total_area_1=total_area_1,
            number_of_room_2=number_of_room_2,
            seating_capacity_2=seating_capacity_2,
            total_area_2=total_area_2,
            number_of_room_3=number_of_room_3,
            seating_capacity_3=seating_capacity_3,
            total_area_3=total_area_3,
            number_of_room_4=number_of_room_4,
            seating_capacity_4=seating_capacity_4,
            total_area_4=total_area_4,
            number_of_room_5=number_of_room_5,
            seating_capacity_5=seating_capacity_5,
            total_area_5=total_area_5,
            number_of_room_6=number_of_room_6,
            seating_capacity_6=seating_capacity_6,
            total_area_6=total_area_6,


            serial_number_1=serial_number1,
            type_of_computer_1=type_of_computer_1,
            number_terminal_1=number_terminal_1,
            year_of_purchase_1=year_of_purchase_1,
            cost_1=cost_1,
            software_facility_1=software_facility_1,
            other_facility_1=other_facility_1,
            serial_number_2=serial_number2,
            type_of_computer_2=type_of_computer_2,
            number_terminal_2=number_terminal_2,
            year_of_purchase_2=year_of_purchase_2,
            cost_2=cost_2,
            software_facility_2=software_facility_2,
            other_facility_2=other_facility_2,
            serial_number_3=serial_number3,
            type_of_computer_3=type_of_computer_3,
            number_terminal_3=number_terminal_3,
            year_of_purchase_3=year_of_purchase_3,
            cost_3=cost_3,
            software_facility_3=software_facility_3,
            other_facility_3=other_facility_3,
            serial_number_4=serial_number4,
            type_of_computer_4=type_of_computer_4,
            number_terminal_4=number_terminal_4,
            year_of_purchase_4=year_of_purchase_4,
            cost_4=cost_4,
            software_facility_4=software_facility_4,
            other_facility_4=other_facility_4,
            serial_number_5=serial_number5,
            type_of_computer_5=type_of_computer_5,
            number_terminal_5=number_terminal_5,
            year_of_purchase_5=year_of_purchase_5,
            cost_5=cost_5,
            software_facility_5=software_facility_5,
            other_facility_5=other_facility_5,
            serial_number_6=serial_number6,
            type_of_computer_6=type_of_computer_6,
            number_terminal_6=number_terminal_6,
            year_of_purchase_6=year_of_purchase_6,
            cost_6=cost_6,
            software_facility_6=software_facility_6,
            other_facility_6=other_facility_6,


            information_serial_number_1=information_serial_number_1,
            name_1=name_1,
            designation_1=designation_1,
            qualification_1=qualification_1,
            teaching_experience_1=teaching_experience_1,
            date_of_appointment_1=date_of