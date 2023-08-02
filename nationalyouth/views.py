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


def generate_roll_number():
    last_roll_number = Admission_Registration.objects.order_by('-id').first()
    if last_roll_number:
        last_roll_number = int(last_roll_number.registration_number)
        new_roll_number = str(last_roll_number + 1)
    else:
        new_roll_number = '1000'
    return new_roll_number

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
            registration_number = generate_roll_number(),
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
        'reg_id':generate_roll_number(),
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
            exmd = Exam_Registration.objects.filter(registration_number=get_search_registration_number).first()
            if exmd:
                register_number_allready="Registration Number already exist in Mark Registration !!"
            if admissions:
                search_student_data = admissions
            else:
                search_student_data_error = "Invalid Registration Number!"



    registration_number=request.POST.get("send_registration_number")
    #registered_student = Admission_Registration.objects.get(registration_number=registration_number)
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
    search_student_data_error = ''
    admissionsFormdata=None
    register_number_allready=""
    get_search_registration_number=request.GET.get("search_registration_number")
    if get_search_registration_number:
        admissions = Admission_Registration.objects.filter(registration_number=get_search_registration_number).first()
        admissionsFormdata = Mark_List_Registration.objects.filter(registration_number=get_search_registration_number).first()

        if admissionsFormdata:
            register_number_allready="Registration Number already exist in Mark Registration !!"
        if admissions:
                search_student_data = admissions
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
    internal_marks_6=request.POST.get("send_internal_marks_6")
    internal_marks_7=request.POST.get("send_internal_marks_7")
    internal_marks_8=request.POST.get("send_internal_marks_8")
    internal_marks_9=request.POST.get("send_internal_marks_9")
    internal_marks_10=request.POST.get("send_internal_marks_10")
    internal_marks_11=request.POST.get("send_internal_marks_11")
    internal_marks_12=request.POST.get("send_internal_marks_12")
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
    viva_mark=request.POST.get("send_viva_mark")
    total_mark_1=request.POST.get("send_total_mark_1")
    total_mark_obtained=request.POST.get("send_total_mark_obtained")
    practical_mark=request.POST.get("send_practical_mark")
    
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
            pc_geting_number_rnd.viva_mark=viva_mark

            pc_geting_number_rnd.total_mark_1=total_mark_1
            pc_geting_number_rnd.total_mark_obtained=total_mark_obtained
            pc_geting_number_rnd.practical_mark=practical_mark
           
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
                internal_marks_1=internal_marks_1,
                internal_marks_2=internal_marks_2,
                internal_marks_3=internal_marks_3,
                internal_marks_4=internal_marks_4,
                internal_marks_5=internal_marks_5,
                internal_marks_6=internal_marks_6,
                internal_marks_7=internal_marks_7,
                internal_marks_8=internal_marks_8,
                internal_marks_9=internal_marks_9,
                internal_marks_10=internal_marks_10,
                internal_marks_11=internal_marks_11,
                internal_marks_12=internal_marks_12,
                external_marks_1=external_marks_1,
                external_marks_2=external_marks_2,
                external_marks_3=external_marks_3,
                external_marks_4=external_marks_4,
                external_marks_5=external_marks_5,
                external_marks_6=external_marks_6,
                external_marks_7=external_marks_7,
                external_marks_8=external_marks_8,
                external_marks_9=external_marks_9,
                external_marks_10=external_marks_10,
                external_marks_11=external_marks_11,
                external_marks_12=external_marks_12,
                mark_obtained_1=mark_obtained_1,
                mark_obtained_2=mark_obtained_2,
                mark_obtained_3=mark_obtained_3,
                mark_obtained_4=mark_obtained_4,
                mark_obtained_5=mark_obtained_5,
                mark_obtained_6=mark_obtained_6,
                mark_obtained_7=mark_obtained_7,
                mark_obtained_8=mark_obtained_8,
                mark_obtained_9=mark_obtained_9,
                mark_obtained_10=mark_obtained_10,
                mark_obtained_11=mark_obtained_11,
                mark_obtained_12=mark_obtained_12,
                total_1=total_1,
                total_2=total_2,
                total_3=total_3,
                total_4=total_4,
                total_5=total_5,
                total_6=total_6,
                total_7=total_7,
                total_8=total_8,
                total_9=total_9,
                total_10=total_10,
                total_11=total_11,
                total_12=total_12,
                viva_mark=viva_mark,
                total_mark_1=total_mark_1,
                total_mark_obtained=total_mark_obtained,
                practical_mark=practical_mark,
            
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
            )
            add_mark_registration.save()
            return HttpResponse("Save")


    data = {
        'all_mark_enter_clerk':all_mark_enter_clerk,
        'all_result_status':all_result_status,
        'search_student_data':search_student_data,
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
            date_of_appointment_1=date_of_appointment_1,
            status_1=status_1,
            information_serial_number_2=information_serial_number_2,
            name_2=name_2,
            designation_2=designation_2,
            qualification_2=qualification_2,
            teaching_experience_2=teaching_experience_2,
            date_of_appointment_2=date_of_appointment_2,
            status_2=status_2,
            information_serial_number_3=information_serial_number_3,
            name_3=name_3,
            designation_3=designation_3,
            qualification_3=qualification_3,
            teaching_experience_3=teaching_experience_3,
            date_of_appointment_3=date_of_appointment_3,
            status_3=status_3,
            information_serial_number_4=information_serial_number_4,
            name_4=name_4,
            designation_4=designation_4,
            qualification_4=qualification_4,
            teaching_experience_4=teaching_experience_4,
            date_of_appointment_4=date_of_appointment_4,
            status_4=status_4,


            center_address=center_address,
            residential_address=residential_address,
            signature=signature,
            form_receive_date=form_receive_date,
            affliation_number=affliation_number,
            total_affliation_fee=total_affliation_fee,
            registration_fee=registration_fee,
            amount_status=amount_status,
            bank_name=bank_name,
            receipt_number=receipt_number,
            date=date,
            education_institution_type=education_institution_type,
            affliation_from_date=affliation_from_date,
            affliation_to_date=affliation_to_date
        )
        application.save()
        return HttpResponse("Save")
    else:
        print("One or more variables do not have a value")
    
    
    data = {
        'all_institution_status':all_institution_status,
        'payment_status':payment_status,
    }

    return render(request,'internal/application_for_affiliation.html',data)
#===================================================================================================
#===================================================================================================
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= Employee Service Book Page ================================
def employee_service_book(request):
    return render(request,'internal/employee_service_book.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= Pay Online Fees Page ======================================
def pay_online_fees(request):
    all_type_fees = Fee_Type.objects.all()
    
    CollegeName = request.POST.get("CollegeName")
    Typeoffee = request.POST.get("Typeoffee")
    typeofFeeOther = request.POST.get("typeofFeeOther")
    amount = request.POST.get("amount")
    datepicker = request.POST.get("datepicker")
    remarks = request.POST.get("remarks")
    Transactionid = request.POST.get("Transactionid")

    if CollegeName and Typeoffee and amount and datepicker and remarks and Transactionid:
        typeoffee = Fee_Type.objects.get(id=Typeoffee)
        
        Pay_Online_Fees(
            college_name=CollegeName,
            type_of_fees=typeoffee,
            type_of_other_fees=typeofFeeOther,
            amount=amount,
            date=datepicker,
            remark=remarks,
            transaction_id=Transactionid
        ).save()
        return HttpResponse("Save")
    data = {
        'all_type_fees':all_type_fees,
    }

    return render(request,'internal/pay_online_fees.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Office File Sanction Page ===============================
@login_required
def e_office_file_sanction(request):
    all_status = Status.objects.all()
    docket_number = request.POST.get("docket_number")
    employee_code = request.POST.get("employee_code")
    employee_name = request.POST.get("employee_name")
    file_number = request.POST.get("file_number")
    file_name = request.POST.get("file_name")
    sanction_clerk = request.POST.get("sanction_clerk")
    officer_grade_1 = request.POST.get("officer_grade_1")
    officer_grade_2 = request.POST.get("officer_grade_2")
    note_file = request.POST.get("note_file")
    general_note_sanction_order = request.POST.get("general_note_sanction_order")
    order_number = request.POST.get("order_number")
    remark = request.POST.get("remark")
    
    if docket_number and employee_code and employee_name and file_number and file_name and sanction_clerk and officer_grade_1 and officer_grade_2 and note_file and general_note_sanction_order and order_number and remark:
        sanction_clerk_id=Status.objects.get(id=sanction_clerk)
        officer_grade_1_id=Status.objects.get(id=officer_grade_1)
        officer_grade_2_id=Status.objects.get(id=officer_grade_2)
        
        your_model_instance = E_Office_File_Sanction(
            docket_number=docket_number,
            employee_code=employee_code,
            employee_name=employee_name,
            file_number=file_number,
            file_name=file_name,
            sanction_clerk=sanction_clerk_id,
            officer_grade_1=officer_grade_1_id,
            officer_grade_2=officer_grade_2_id,
            note_file=note_file,
            general_note_sanction_order=general_note_sanction_order,
            order_number=order_number,
            remark=remark
        )

        your_model_instance.save()
        return HttpResponse("Save")

    data = {
        'all_status':all_status,
    }
    return render(request,'internal/e_office_file_sanction.html',data)
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
    all_e_finance_and_accounts = E_Office_Account.objects.all()
    data = {
        'all_e_finance_and_accounts':all_e_finance_and_accounts,
    }
    return render(request,'internal/e_finance_and_accounts.html',data)
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E-Office Accounts Page ====================================
@login_required
def e_office_accounts(request):
    all_type_account = Type_of_Account.objects.all()
    all_particular_head = Particulars_Head.objects.all()
    all_college_name = College_Name.objects.all()
    all_status = Status.objects.all()
  
    type_of_account = request.POST.get("type_of_account")

    voucher_number = request.POST.get("voucher_number")

    particular_head = request.POST.get("particular_head")

    date = request.POST.get("date")

    amount = request.POST.get("amount")

    bank_name = request.POST.get("bank_name")

    amount_detail = request.POST.get("amount_detail")

    transaction_id = request.POST.get("transaction_id")

    remark = request.POST.get("remark")

    details_name = request.POST.get("details_name")

    college_name = request.POST.get("college_name")

    address = request.POST.get("address")

    amount2 = request.POST.get("amount2")

    file_referral_number = request.POST.get("file_referral_number")

    o_office_register_number = request.POST.get("o_office_register_number")

    pan_card_number = request.POST.get("pan_card_number")

    officer_incharge_name = request.POST.get("officer_incharge_name")

    secretary_name = request.POST.get("secretary_name")

    officer_incharge_status = request.POST.get("officer_incharge_status")

    secretary_status = request.POST.get("secretary_status")

    remark_staff_approval = request.POST.get("remark_staff_approval")

    remark_officer_approval = request.POST.get("remark_officer_approval")

    office_referral_number = request.POST.get("office_referral_number")

    description = request.POST.get("description")

    if type_of_account and particular_head and date and voucher_number and details_name and college_name and address and file_referral_number and o_office_register_number and officer_incharge_name and secretary_name and officer_incharge_status and secretary_status and remark_staff_approval and remark_officer_approval and office_referral_number:
        type_of_account = Type_of_Account.objects.get(id=type_of_account)
        particular_head = Particulars_Head.objects.get(id=particular_head)
        college_name = College_Name.objects.get(id=college_name)
        officer_incharge_status = Status.objects.filter(id=officer_incharge_status).first()
        secretary_status=Status.objects.filter(id=secretary_status).first()
        e_office_account = E_Office_Account(
            type_of_account=type_of_account,
            voucher_number=voucher_number,
            particular_head=particular_head,
            date=date,
            amount=amount,
            bank_name=bank_name,
            amount_detail=amount_detail,
            transaction_number=transaction_id,
            remark=remark,
            name=details_name,
            college_name=college_name,
            address=address,
            amount2=amount2,
            file_referral_number=file_referral_number,
            office_registration_number=o_office_register_number,
            pan_card_number=pan_card_number,
            officer_incharge_name=officer_incharge_name,
            secretary_name=secretary_name,
            officer_incharge_status=officer_incharge_status,
            secretary_status=secretary_status,
            remark_staff_approval=remark_staff_approval,
            remark_officer_approval=remark_officer_approval,
            office_referral_number=office_referral_number,
            description=description
        )
        e_office_account.save()
        return HttpResponse("Save")
    


    data = {
        'all_type': all_type_account,
        'all_heads' : all_particular_head,
        'all_college' : all_college_name,
        'all_status':all_status,
    }
    return render(request,'internal/e-office_accounts.html',data)
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
@login_required
def e_office_queue_files(request):
    all_status = Status.objects.all()
    queue_number = request.POST.get("queue_number")
    file_subject = request.POST.get("file_subject")
    remark = request.POST.get("remark")
    approval_first_officer = request.POST.get("approval_first_officer")
    approval_second_officer = request.POST.get("approval_second_officer")

    if queue_number and file_subject:
        get_approval_first_officer = Status.objects.filter(id=approval_first_officer).first()
        get_approval_second_officer = Status.objects.filter(id=approval_second_officer).first()
        add_e_office_queue_files = E_Office_Queue(
            queue_number=queue_number,
            file_subject=file_subject,
            remark=remark,
            approval_first_officer=get_approval_first_officer,
            approval_second_officer=get_approval_second_officer,
        )

        # Save the instance
        add_e_office_queue_files.save()
        return HttpResponse("Save")

    data = {
        'all_status':all_status,
    }
    return render(request,'internal/e_office_queue_files.html',data)
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
@login_required
def e_employee_records(request):
    all_employee_record = Employee_Record_Type.objects.all()
    employee_record_type = request.POST.get("employee_record_type")
    name = request.POST.get("name")
    designation = request.POST.get("designation")
    employee_code = request.POST.get("employee_code")
    office_address = request.POST.get("office_address")
    home_address = request.POST.get("home_address")
    contact_number = request.POST.get("contact_number")
    aadhar_number = request.POST.get("aadhar_number")
    husband_or_wife_name = request.POST.get("husband_or_wife_name")
    father_name = request.POST.get("father_name")
    age_of_father = request.POST.get("age_of_father")
    mother_name = request.POST.get("mother_name")
    age_of_mother = request.POST.get("age_of_mother")
    child_name_1 = request.POST.get("child_name_1")
    age_of_child_1 = request.POST.get("age_of_child_1")
    child_name_2 = request.POST.get("child_name_2")
    age_of_child_2 = request.POST.get("age_of_child_2")
    child_name_3 = request.POST.get("child_name_3")
    age_of_child_3 = request.POST.get("age_of_child_3")
    scale_of_pay = request.POST.get("scale_of_pay")
    employee_liablity = request.POST.get("employee_liablity")
    employee_promotion = request.POST.get("employee_promotion")
    employee_grade = request.POST.get("employee_grade")
    salary = request.POST.get("salary")
    advance = request.POST.get("advance")
    bonus = request.POST.get("bonus")
    loan = request.POST.get("loan")
    note = request.POST.get("note")
    remark = request.POST.get("remark")
    suspension = request.POST.get("suspension")
    showcase_notice = request.POST.get("showcase_notice")

    if employee_record_type and name and designation and employee_code and office_address and home_address and \
        contact_number and aadhar_number and husband_or_wife_name and father_name and age_of_father and \
        mother_name and age_of_mother and child_name_1 and age_of_child_1 and scale_of_pay and employee_liablity and \
        employee_promotion and employee_grade and salary and advance and bonus and loan and note and remark and suspension and showcase_notice:
        get_employee_record_type = Employee_Record_Type.objects.get(id=employee_record_type)
        add_employee_record = E_Employee_Record(
            employee_record_type=get_employee_record_type,
            name=name,
            designation=designation,
            employee_code=employee_code,
            office_address=office_address,
            home_address=home_address,
            contact_number=contact_number,
            aadhar_number=aadhar_number,
            husband_or_wife_name=husband_or_wife_name,
            father_name=father_name,
            age_of_father=age_of_father,
            mother_name=mother_name,
            age_of_mother=age_of_mother,
            child_name_1=child_name_1,
            age_of_child_1=age_of_child_1,
            child_name_2=child_name_2,
            age_of_child_2=age_of_child_2,
            child_name_3=child_name_3,
            age_of_child_3=age_of_child_3,
            scale_of_pay=scale_of_pay,
            employee_liablity=employee_liablity,
            employee_promotion=employee_promotion,
            employee_grade=employee_grade,
            salary=salary,
            advance=advance,
            bonus=bonus,
            loan=loan,
            note=note,
            remark=remark,
            suspension=suspension,
            showcase_notice=showcase_notice,
        )
        add_employee_record.save()
        return HttpResponse("Save")

    data = {
        "all_employee_record":all_employee_record,
    }
    return render(request,'internal/e_employee_records.html',data)
#===================================================================================================
#===================================================================================================




#===================================================================================================
#======================================= E Employee Daily Work Statement Page ======================
@login_required
def e_employee_daily_work_statement(request):
    all_status = Status.objects.all()
    all_work_status = Work_Status.objects.all()

    employee_name = request.POST.get("employee_name")
    work_start_time = request.POST.get("work_start_time")
    employee_code = request.POST.get("employee_code")
    work_end_time = request.POST.get("work_end_time")
    serial_number_1 = request.POST.get("serial_number_1")
    file_number_1 = request.POST.get("file_number_1")
    work_name_1 = request.POST.get("work_name_1")
    work_status_1 = request.POST.get("work_status_1")
    serial_number_2 = request.POST.get("serial_number_2")
    file_number_2 = request.POST.get("file_number_2")
    work_name_2 = request.POST.get("work_name_2")
    work_status_2 = request.POST.get("work_status_2")
    serial_number_3 = request.POST.get("serial_number_3")
    file_number_3 = request.POST.get("file_number_3")
    work_name_3 = request.POST.get("work_name_3")
    work_status_3 = request.POST.get("work_status_3")
    serial_number_4 = request.POST.get("serial_number_4")
    file_number_4 = request.POST.get("file_number_4")
    work_name_4 = request.POST.get("work_name_4")
    work_status_4 = request.POST.get("work_status_4")
    serial_number_5 = request.POST.get("serial_number_5")
    file_number_5 = request.POST.get("file_number_5")
    work_name_5 = request.POST.get("work_name_5")
    work_status_5 = request.POST.get("work_status_5")
    serial_number_6 = request.POST.get("serial_number_6")
    file_number_6 = request.POST.get("file_number_6")
    work_name_6 = request.POST.get("work_name_6")
    work_status_6 = request.POST.get("work_status_6")
    serial_number_7 = request.POST.get("serial_number_7")
    file_number_7 = request.POST.get("file_number_7")
    work_name_7 = request.POST.get("work_name_7")
    work_status_7 = request.POST.get("work_status_7")
    serial_number_8 = request.POST.get("serial_number_8")
    file_number_8 = request.POST.get("file_number_8")
    work_name_8 = request.POST.get("work_name_8")
    work_status_8 = request.POST.get("work_status_8")
    serial_number_9 = request.POST.get("serial_number_9")
    file_number_9 = request.POST.get("file_number_9")
    work_name_9 = request.POST.get("work_name_9")
    work_status_9 = request.POST.get("work_status_9")
    serial_number_10 = request.POST.get("serial_number_10")
    file_number_10 = request.POST.get("file_number_10")
    work_name_10 = request.POST.get("work_name_10")
    work_status_10 = request.POST.get("work_status_10")
    date = request.POST.get("date")
    charge_officer_name = request.POST.get("charge_officer_name")
    status_1 = request.POST.get("status_1")
    chief_executive_officer_name = request.POST.get("chief_executive_officer_name")
    status_2 = request.POST.get("status_2")

    if employee_name and work_start_time and employee_code and work_end_time and serial_number_1 and file_number_1 and \
        work_name_1 and work_status_1:
        get_work_status_1 = Work_Status.objects.get(id=work_status_1)
        get_work_status_2 = Work_Status.objects.get(id=work_status_2)
        get_work_status_3 = Work_Status.objects.get(id=work_status_3)
        get_work_status_4 = Work_Status.objects.get(id=work_status_4)
        get_work_status_5 = Work_Status.objects.get(id=work_status_5)
        get_work_status_6 = Work_Status.objects.get(id=work_status_6)
        get_work_status_7 = Work_Status.objects.get(id=work_status_7)
        get_work_status_8 = Work_Status.objects.get(id=work_status_8)
        get_work_status_9 = Work_Status.objects.get(id=work_status_9)
        get_work_status_10 = Work_Status.objects.get(id=work_status_10)
        get_status_1 = Status.objects.get(id=status_1)
        get_status_2 = Status.objects.get(id=status_2)

        add_employee_daily_work_statement = E_employee_daily_work_statement(
            employee_name=employee_name,
            work_start_time=work_start_time,
            employee_code=employee_code,
            work_end_time=work_end_time,
            serial_number_1=serial_number_1,
            file_number_1=file_number_1,
            work_name_1=work_name_1,
            work_status_1=get_work_status_1,
            serial_number_2=serial_number_2,
            file_number_2=file_number_2,
            work_name_2=work_name_2,
            work_status_2=get_work_status_2,
            serial_number_3=serial_number_3,
            file_number_3=file_number_3,
            work_name_3=work_name_3,
            work_status_3=get_work_status_3,
            serial_number_4=serial_number_4,
            file_number_4=file_number_4,
            work_name_4=work_name_4,
            work_status_4=get_work_status_4,
            serial_number_5=serial_number_5,
            file_number_5=file_number_5,
            work_name_5=work_name_5,
            work_status_5=get_work_status_5,
            serial_number_6=serial_number_6,
            file_number_6=file_number_6,
            work_name_6=work_name_6,
            work_status_6=get_work_status_6,
            serial_number_7=serial_number_7,
            file_number_7=file_number_7,
            work_name_7=work_name_7,
            work_status_7=get_work_status_7,
            serial_number_8=serial_number_8,
            file_number_8=file_number_8,
            work_name_8=work_name_8,
            work_status_8=get_work_status_8,
            serial_number_9=serial_number_9,
            file_number_9=file_number_9,
            work_name_9=work_name_9,
            work_status_9=get_work_status_9,
            serial_number_10=serial_number_10,
            file_number_10=file_number_10,
            work_name_10=work_name_10,
            work_status_10=get_work_status_10,
            date=date,
            charge_officer_name=charge_officer_name,
            status_1=get_status_1,
            chief_executive_officer_name=chief_executive_officer_name,
            status_2=get_status_2,
        )
        add_employee_daily_work_statement.save()
        return HttpResponse("Save")
    data={
        'all_status':all_status,
        'all_work_status':all_work_status,
    }
    return render(request,'internal/e_employee_daily_work_statement.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Employee Live and Leave Status Page =====================
@login_required
def e_employee_live_and_leave_status(request):
    all_employee_live_status = Employee_Live_and_Leave_Status.objects.all()
    all_status = Status.objects.all()
    all_nature_of_leave = Nature_of_Leave.objects.all()
    
    Employee_Live = request.POST.get("Employee_Live")
    Employee_ID_Number = request.POST.get("Employee_ID_Number")
    Employee_Namec = request.POST.get("Employee_Namec")
    if Employee_Live and Employee_ID_Number and Employee_Namec:
        if Employee_Live=='None':
            Employee_Live_id = None
        else:
            Employee_Live_id=Employee_Live_and_Leave_Status.objects.get(id=Employee_Live)
            
        your_module = Employee_Status(
            employee_live_or_leave_status=Employee_Live_id,
            employee_id_number=Employee_ID_Number,
            employee_name=Employee_Namec,
        )
        your_module.save()
        return HttpResponse("Save")
    data = {
        'employee_live':all_employee_live_status,
        'all_status':all_status,
        'all_nature_of_leave':all_nature_of_leave,
    }
    return render(request,'internal/e_employee_live_status.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Employee Live Status Page ===============================
@login_required
def e_employee_live_status(request):
    all_employee_live_status = Employee_Live_and_Leave_Status.objects.all()
    all_status = Status.objects.all()
    all_nature_of_leave = Nature_of_Leave.objects.all()
    
    get_Employee_Live = request.POST.get("send_Employee_Live")
    get_Employee_ID_Number = request.POST.get("send_Employee_ID_Number")
    get_Employee_Namec = request.POST.get("send_Employee_Namec")
    get_nature_of_leave = request.POST.get("send_nature_of_leave")
    get_remark2 = request.POST.get("send_remark2")
    get_datepicker = request.POST.get("send_datepicker")
    get_current_status2 = request.POST.get("send_current_status2")


    # Check if all variables have a value
    if get_Employee_Live and get_Employee_ID_Number and get_Employee_Namec and get_nature_of_leave and get_remark2 and get_datepicker and get_current_status2:
        status = Status.objects.filter(id=get_current_status2).first() #select option filed 
        employee_live_or_leave_status = Employee_Live_and_Leave_Status.objects.filter(id=2).first() 
        nature_of_leave = Nature_of_Leave.objects.filter(id=get_nature_of_leave).first()

        save_live_status_data = E_employee_live_status(
            employee_live_or_leave_status=employee_live_or_leave_status,
            employee_id_number=get_Employee_ID_Number,
            employee_name=get_Employee_Namec,
            nature_of_leave=nature_of_leave,
            remark=get_remark2,
            date=get_datepicker,
            status=status,
        )
        save_live_status_data.save()
        return HttpResponse("Save")
    else:
        print("One or more variables are missing a value.")



    
    data = {
        'employee_live':all_employee_live_status,
        'all_status':all_status,
        'all_nature_of_leave':all_nature_of_leave,
    }
    return render(request,'internal/e_employee_live_status.html',data)
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Employee Leave Status Page ==============================
@login_required
def e_employee_leave_status(request):
    all_employee_live_status = Employee_Live_and_Leave_Status.objects.all()
    all_status = Status.objects.all()
    all_nature_of_leave = Nature_of_Leave.objects.all()
    
    #get_Employee_Live = request.POST.get("Employee_ID_Number2")
    get_Employee_ID_Number = request.POST.get("send_Employee_ID_Number2")
    get_Employee_Namec = request.POST.get("send_Employee_Name2")
    get_purpose_1 = request.POST.get("send_purpose1")
    get_distance_walking_1 = request.POST.get("send_walking_distance1")
    get_purpose_2 = request.POST.get("send_purpose2")
    get_distance_walking_2 = request.POST.get("send_walking_distance2")
    get_purpose_3 = request.POST.get("send_purpose3")
    get_distance_walking_3 = request.POST.get("send_walking_distance3")
    get_staff_out_time = request.POST.get("send_staff_out_time")
    get_staff_in_time = request.POST.get("send_staff_in_time")
    get_status3 = request.POST.get("send_current_status3")
    get_remark = request.POST.get("send_remark")

    if get_Employee_ID_Number and get_Employee_Namec and get_purpose_1 and get_distance_walking_1 and get_staff_out_time and get_staff_in_time and get_status3 and get_remark:
        get_Employee_Live_id=Employee_Live_and_Leave_Status.objects.get(id=1)
        status = Status.objects.get(id=get_status3)
            
        save_leave_status_data = E_employee_leave_status(
            employee_live_or_leave_status = get_Employee_Live_id,
            employee_id_number = get_Employee_ID_Number,
            employee_name = get_Employee_Namec,
            purpose_1 = get_purpose_1,
            distance_walking_1 = get_distance_walking_1,
            purpose_2 = get_purpose_2,
            distance_walking_2 = get_distance_walking_2,
            purpose_3 = get_purpose_3,
            distance_walking_3 = get_distance_walking_3,
            staff_out_time = get_staff_out_time,
            staff_in_time = get_staff_in_time,
            status = status,
            remark = get_remark,
        )
        save_leave_status_data.save()
        return HttpResponse("Save")
    data = {
        'employee_live':all_employee_live_status,
        'all_status':all_status,
        'all_nature_of_leave':all_nature_of_leave,
    }
    return render(request,'internal/e_employee_live_status.html',data)
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





#============================================ Extra 1 ==============================================


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






#============================================ Extra 2 ==============================================


#===================================================================================================
#======================================= E Office Files Mark List Page =============================
def e_office_files_student_mark_list(request):
    return render(request,'internal/e_office_files_student_mark_list.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Office Files Daily Work Statement Page ==================
def e_office_files_daily_work_statement(request):
    return render(request,'internal/e_office_files_daily_work_statement.html')
#===================================================================================================
#===================================================================================================


#===================================================================================================
#======================================= E Office Files Employee Live Status Page ==================
def e_office_files_employee_live_status(request):
    return render(request,'internal/e_office_files_employee_live_status.html')
#===================================================================================================
#===================================================================================================



#===================================================================================================
#======================================= E Office Files Pay Online Fees Page =======================
def e_office_files_pay_online_fees(request):
    return render(request,'internal/e_office_files_pay_online_fees.html')
#===================================================================================================
#===================================================================================================



#============================================ Extra 3 ==============================================


#===================================================================================================
#======================================= E Office Files Staff work Allotment Page ==================
@login_required
def staff_work_alloted(request):
    all_work_assign_office = Work_Assign_Office.objects.all()
    all_work_status = Work_Status.objects.all()

    work_assign_office = request.POST.get("send_work_assign_office")
    name_of_employee = request.POST.get("send_name_of_employee")
    work_start_date = request.POST.get("send_work_start_date")
    work_start_time = request.POST.get("send_work_start_time")
    work_name = request.POST.get("send_work_name")
    upload_work = request.POST.get("send_myFileInput")
    work_finishing_date = request.POST.get("send_work_finishing_date")
    work_finishing_time = request.POST.get("send_work_finishing_time")
    work_head_name = request.POST.get("send_work_head_name")
    current_status = request.POST.get("send_current_status")

    if work_assign_office and name_of_employee and work_start_date and work_start_time and work_name and upload_work and \
        work_finishing_date and work_finishing_time and work_head_name and current_status:
        get_work_assign_office_id = Work_Assign_Office.objects.get(id=work_assign_office)
        get_current_status_id = Work_Status.objects.get(id=current_status)
        save_data = Staff_work_allotment(
            work_assign_office = get_work_assign_office_id,
            name_of_employee = name_of_employee,
            work_start_date = work_start_date,
            work_start_time = work_start_time,
            work_name = work_name,
            upload_work = upload_work,
            work_finishing_date = work_finishing_date,
            work_finishing_time = work_finishing_time,
            work_head_name = work_head_name,
            current_status = get_current_status_id,
        )
        save_data.save()
        return HttpResponse("Save")
    data = {
        'all_work_assign_office':all_work_assign_office,
        'all_work_status':all_work_status,
    }
    return render(request,'internal/staff_work_alloted.html',data)
#===================================================================================================
#===================================================================================================