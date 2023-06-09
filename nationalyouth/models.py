"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

from django.db import models





#===================================== Drop down Models =============================================================

#====================================== Type of Accounts Model ====================================
class Type_of_Account(models.Model):
    type_of_account = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type_of_account
#==================================================================================================
#==================================================================================================


#====================================== Particulars Head Model ====================================
class Particulars_Head(models.Model):
    particular_head = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.particular_head
#==================================================================================================
#==================================================================================================


#====================================== Collage Name Model ========================================
class College_Name(models.Model):
    college_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.college_name
#==================================================================================================
#==================================================================================================


#====================================== Course Name Model ========================================
class Course_Name(models.Model):
    course_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.course_name
#==================================================================================================
#==================================================================================================



#====================================== Status Model ==============================================
class Status(models.Model):
    status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status
#==================================================================================================
#==================================================================================================


#====================================== Employee Record Type Model ================================
class Employee_Record_Type(models.Model):
    employee_record_type = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.employee_record_type
#==================================================================================================
#==================================================================================================


#====================================== Work Status Model =========================================
class Work_Status(models.Model):
    work_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.work_status
#==================================================================================================
#==================================================================================================


#====================================== Employee Live / Leave Model ================================
class Employee_Live_and_Leave_Status(models.Model):
    employee_live_and_leave_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.employee_live_and_leave_status
#==================================================================================================
#==================================================================================================


#====================================== Work Assign Office Model ==================================
class Work_Assign_Office(models.Model):
    work_assign_office = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.work_assign_office
#==================================================================================================
#==================================================================================================



#====================================== Exam Fees Type Model ======================================
class Exam_Fees_Type(models.Model):
    exam_fees_type = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.exam_fees_type
#==================================================================================================
#==================================================================================================


#====================================== Mark Enter Clerk Model ====================================
class Mark_Status(models.Model):
    mark_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.mark_status
#==================================================================================================
#==================================================================================================



#====================================== Result Status Model =======================================
class Result_Status(models.Model):
    result_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.result_status
#==================================================================================================
#==================================================================================================


#====================================== Add-on Colleges Model =====================================
class Add_on_College(models.Model):
    add_on_college_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.add_on_college_name
#==================================================================================================
#==================================================================================================



#====================================== Main Courses Model ========================================
class Main_Course(models.Model):
    main_course_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.main_course_name
#==================================================================================================
#==================================================================================================


#====================================== Status of the Institution Model ===========================
class Institution_Status(models.Model):
    institution_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.institution_status
#==================================================================================================
#==================================================================================================



#====================================== Amount Status Model =======================================
class Amount_Status(models.Model):
    amount_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.amount_status
#==================================================================================================
#==================================================================================================



#====================================== Types of Fees Model =======================================
class Fee_Type(models.Model):
    fee_type = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fee_type
#==================================================================================================
#==================================================================================================
#===================================== End Dropdown Model==========================================
#==================================================================================================







#====================================== Admission Registration Model ==============================
class Admission_Registration(models.Model):
    registration_number = models.CharField(max_length=250)
    name_of_student = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    id_number = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    district = models.CharField(max_length=250)     
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    admission_fees = models.CharField(max_length=250)
    admission_month_and_year = models.CharField(max_length=250)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.registration_number
#==================================================================================================
#==================================================================================================




#====================================== Exam Registration Model ====================================
class Exam_Registration(models.Model):
    registration_number = models.CharField(max_length=250)
    exam_fees = models.ForeignKey(Exam_Fees_Type, on_delete = models.CASCADE,null=True,blank=True)     #select option filed
    exam_attendance = models.CharField(max_length=250)
    any_fees_concession = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    principal_code = models.CharField(max_length=250)   
    principal_name = models.CharField(max_length=250)     
    online_fees = models.CharField(max_length=250)
    remark = models.TextField(max_length=250)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.registration_number
#==================================================================================================
#==================================================================================================



#====================================== Mark List Registration Model ==============================
class Mark_List_Registration(models.Model):
    registration_number = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    subject_1 = models.CharField(max_length=250)
    subject_2 = models.CharField(max_length=250)   
    subject_3 = models.CharField(max_length=250)
    subject_4 = models.CharField(max_length=250)
    internal_marks_1 = models.CharField(max_length=250)
    internal_marks_2 = models.CharField(max_length=250)
    internal_marks_3 = models.CharField(max_length=250)
    internal_marks_4 = models.CharField(max_length=250)
    mark_obtained_1 = models.CharField(max_length=250)
    mark_obtained_2 = models.CharField(max_length=250)
    mark_obtained_3 = models.CharField(max_length=250)
    mark_obtained_4 = models.CharField(max_length=250)
    total_1 = models.CharField(max_length=250)
    total_2 = models.CharField(max_length=250)
    total_3 = models.CharField(max_length=250)
    total_4 = models.CharField(max_length=250)
    viva_mark = models.CharField(max_length=250)
    total_mark = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)

    #========================Office use=================
    mark_enter_clerk_name = models.CharField(max_length=250)   
    mark_enter_clerk = models.ForeignKey(Mark_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    mark_check_clerk_name = models.CharField(max_length=250)   
    mark_check_clerk = models.ForeignKey(Mark_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='mark_check_cleark_status') #select option filed
    second_verified_officer_name = models.CharField(max_length=250)   
    second_verified_officer = models.ForeignKey(Mark_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='second_verified_officer_status') #select option filed
    final_mark_verified_officer_name = models.CharField(max_length=250)   
    result_status = models.ForeignKey(Result_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    result_enter_register_book_number = models.CharField(max_length=250)
    mark_obtained = models.CharField(max_length=250)
    total_mark = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.registration_number
#==================================================================================================
#==================================================================================================



#====================================== Add On Programme(College) Model ============================
class Add_on_Programme(models.Model):
    add_on_College = models.ForeignKey(Add_on_College, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    course_code = models.CharField(max_length=250)
    student_name = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    id_number = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=250)   
    exam_fees = models.CharField(max_length=250)     
    amount = models.CharField(max_length=250)
    main_course = models.ForeignKey(Main_Course, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    college_coordinator_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================



#====================================== Application for affliation Model ==========================
class Application_for_Affliation(models.Model):
    name_of_institution = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)
    status_of_institution = models.ForeignKey(Institution_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    email = models.CharField(max_length=250)
    status_of_institution_other = models.CharField(max_length=250)
    year_of_establishment = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    pincode = models.CharField(max_length=250)
    
    #===========Information about management =============
    name = models.CharField(max_length=250)
    education_qualification = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    profession_experience = models.CharField(max_length=250)
    postal_address = models.CharField(max_length=250)

    #===========Infrastructure Facility =================
    staff_room = models.CharField(max_length=250)
    number_of_room_1 = models.CharField(max_length=250)
    seating_capacity_1 = models.CharField(max_length=250)
    total_area_1 = models.CharField(max_length=250)
    class_room = models.CharField(max_length=250)
    number_of_room_2 = models.CharField(max_length=250)
    seating_capacity_2 = models.CharField(max_length=250)
    total_area_2 = models.CharField(max_length=250)
    laboratary = models.CharField(max_length=250)
    number_of_room_3 = models.CharField(max_length=250)
    seating_capacity_3 = models.CharField(max_length=250)
    total_area_3 = models.CharField(max_length=250)
    reception = models.CharField(max_length=250)
    number_of_room_4 = models.CharField(max_length=250)
    seating_capacity_4 = models.CharField(max_length=250)
    total_area_4 = models.CharField(max_length=250)
    toilet = models.CharField(max_length=250)
    number_of_room_5 = models.CharField(max_length=250)
    seating_capacity_5 = models.CharField(max_length=250)
    total_area_5 = models.CharField(max_length=250)
    any_other = models.CharField(max_length=250)
    number_of_room_6 = models.CharField(max_length=250)
    seating_capacity_6 = models.CharField(max_length=250)
    total_area_6 = models.CharField(max_length=250)
    
    #===========Computer Facility =================
    serial_number_1 = models.CharField(max_length=250)
    type_of_computer_1 = models.CharField(max_length=250)
    number_terminal_1 = models.CharField(max_length=250)
    year_of_purchase_1 = models.CharField(max_length=250)
    cost_1 = models.CharField(max_length=250)
    software_facility_1 = models.CharField(max_length=250)
    other_facility_1 = models.CharField(max_length=250)

    serial_number_2 = models.CharField(max_length=250)
    type_of_computer_2 = models.CharField(max_length=250)
    number_terminal_2 = models.CharField(max_length=250)
    year_of_purchase_2 = models.CharField(max_length=250)
    cost_2 = models.CharField(max_length=250)
    software_facility_2 = models.CharField(max_length=250)
    other_facility_2 = models.CharField(max_length=250)

    serial_number_3 = models.CharField(max_length=250)
    type_of_computer_3 = models.CharField(max_length=250)
    number_terminal_3 = models.CharField(max_length=250)
    year_of_purchase_3 = models.CharField(max_length=250)
    cost_3 = models.CharField(max_length=250)
    software_facility_3 = models.CharField(max_length=250)
    other_facility_3 = models.CharField(max_length=250)

    serial_number_4 = models.CharField(max_length=250)
    type_of_computer_4 = models.CharField(max_length=250)
    number_terminal_4 = models.CharField(max_length=250)
    year_of_purchase_4 = models.CharField(max_length=250)
    cost_4 = models.CharField(max_length=250)
    software_facility_4 = models.CharField(max_length=250)
    other_facility_4 = models.CharField(max_length=250)

    serial_number_5 = models.CharField(max_length=250)
    type_of_computer_5 = models.CharField(max_length=250)
    number_terminal_5 = models.CharField(max_length=250)
    year_of_purchase_5 = models.CharField(max_length=250)
    cost_5 = models.CharField(max_length=250)
    software_facility_5 = models.CharField(max_length=250)
    other_facility_5 = models.CharField(max_length=250)

    serial_number_6 = models.CharField(max_length=250)
    type_of_computer_6 = models.CharField(max_length=250)
    number_terminal_6 = models.CharField(max_length=250)
    year_of_purchase_6 = models.CharField(max_length=250)
    cost_6 = models.CharField(max_length=250)
    software_facility_6 = models.CharField(max_length=250)
    other_facility_6 = models.CharField(max_length=250)

    #===========Information about Facility =================
    serial_number_1 = models.CharField(max_length=250)
    name_1 = models.CharField(max_length=250)
    designation_1 = models.CharField(max_length=250)
    qualification_1 = models.CharField(max_length=250)
    teaching_experience_1 = models.CharField(max_length=250)
    date_of_appointment_1 = models.CharField(max_length=250)
    status_1 = models.CharField(max_length=250)

    serial_number_2 = models.CharField(max_length=250)
    name_2 = models.CharField(max_length=250)
    designation_2 = models.CharField(max_length=250)
    qualification_2 = models.CharField(max_length=250)
    teaching_experience_2 = models.CharField(max_length=250)
    date_of_appointment_2 = models.CharField(max_length=250)
    status_2 = models.CharField(max_length=250)

    serial_number_3 = models.CharField(max_length=250)
    name_3 = models.CharField(max_length=250)
    designation_3 = models.CharField(max_length=250)
    qualification_3 = models.CharField(max_length=250)
    teaching_experience_3 = models.CharField(max_length=250)
    date_of_appointment_3 = models.CharField(max_length=250)
    status_3 = models.CharField(max_length=250)

    serial_number_4 = models.CharField(max_length=250)
    name_4 = models.CharField(max_length=250)
    designation_4 = models.CharField(max_length=250)
    qualification_4 = models.CharField(max_length=250)
    teaching_experience_4 = models.CharField(max_length=250)
    date_of_appointment_4 = models.CharField(max_length=250)
    status_4 = models.CharField(max_length=250)

    center_address = models.CharField(max_length=250)
    residential_address = models.CharField(max_length=250)
    signature = models.CharField(max_length=250)

    #===========Head Office use ===============
    form_receive_date = models.CharField(max_length=250)
    affliation_number = models.CharField(max_length=250)
    total_affliation_fee = models.CharField(max_length=250)
    registration_fee = models.CharField(max_length=250)
    amount_status = models.ForeignKey(Amount_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    bank_name = models.CharField(max_length=250)
    receipt_number = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    education_institution_type = models.CharField(max_length=250)
    affliation_from_date = models.CharField(max_length=250)
    affliation_to_date = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    
    

#==================================================================================================
#==================================================================================================



#====================================== Pay Online Fees Model =====================================
class Pay_Online_Fees(models.Model):
    college_name = models.CharField(max_length=250)
    type_of_fees = models.CharField(max_length=250)
    type_of_other_fees = models.ForeignKey(Fee_Type, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    amount = models.CharField(max_length=250)
    date = models.CharField(max_length=250)   
    remark = models.CharField(max_length=250)     
    transaction_id = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================















#====================================== Official and Administration ===============================
#==================================================================================================

#====================================== E Office Account Model ====================================
class E_Office_Account(models.Model):
    type_of_account = models.ForeignKey(Type_of_Account, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    voucher_number = models.CharField(max_length=250)
    particular_head = models.ForeignKey(Particulars_Head, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date = models.CharField(max_length=250)   
    amount = models.CharField(max_length=250)

    #===========Online Payment Details ===============
    bank_name = models.CharField(max_length=250)   
    amount = models.CharField(max_length=250)     
    transaction_number = models.CharField(max_length=250)   
    remark = models.CharField(max_length=250)   
    name = models.CharField(max_length=250)   
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    address = models.CharField(max_length=250)   
    amount2 = models.CharField(max_length=250)     
    file_referral_number = models.CharField(max_length=250)
    office_registration_number = models.CharField(max_length=250)     
    pan_card_number = models.CharField(max_length=250)

    #===========Approval ======================
    officer_incharge_name = models.CharField(max_length=250)   
    secretary_name = models.CharField(max_length=250)     
    officer_incharge_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_incharge_status') #select option filed
    secretary_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='secretry_status') #select option filed
    remark_staff_approval = models.CharField(max_length=250)   
    remark_officer_approval = models.CharField(max_length=250)
    office_referral_number = models.CharField(max_length=250) 
    description = models.TextField(max_length=250)   # Doubt in field
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================



#====================================== E Office Queue Model ======================================
class E_Office_Queue(models.Model):
    queue_number = models.CharField(max_length=250)
    file_subject = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    approval_first_officer = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='approval_first_officer') #select option filed
    approval_second_officer = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='approval_second_officer') #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================



#====================================== E Employee Record Model ===================================
class E_Employee_Record(models.Model):
    employee_record_type = models.ForeignKey(Employee_Record_Type, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    employee_code = models.CharField(max_length=250)
    office_address = models.TextField(max_length=250)
    home_address = models.TextField(max_length=250)
    contact_number = models.CharField(max_length=250)
    aadhar_number = models.CharField(max_length=250)
    husband_or_wife_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    age_of_father = models.CharField(max_length=250)
    mother_name = models.CharField(max_length=250)
    age_of_mother = models.CharField(max_length=250)
    child_name_1 = models.CharField(max_length=250)
    age_of_child_1 = models.CharField(max_length=250)
    child_name_2 = models.CharField(max_length=250)
    age_of_child_2 = models.CharField(max_length=250)
    child_name_3 = models.CharField(max_length=250)
    age_of_child_3 = models.CharField(max_length=250)
    scale_of_pay = models.CharField(max_length=250)
    employee_liablity = models.CharField(max_length=250)
    employee_promotion = models.CharField(max_length=250)
    employee_grade = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    advance = models.CharField(max_length=250)
    bonus = models.CharField(max_length=250)
    loan = models.CharField(max_length=250)
    note = models.TextField(max_length=250)
    remark = models.TextField(max_length=250)
    suspension = models.CharField(max_length=250)
    showcase_notice = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================


#====================================== E Office File Sanction Model ==============================
class E_Office_File_Sanction(models.Model):
    docket_number = models.CharField(max_length=250)
    employee_code = models.CharField(max_length=250)
    employee_name = models.CharField(max_length=250)
    file_number = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    sanction_clerk = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='sanction_clerk_status') #select option filed 
    officer_grade_1 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_grade_1_status') #select option filed 
    officer_grade_2 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_grade_2_status') #select option filed 
    note_file = models.TextField(max_length=250)
    general_note_sanction_order = models.TextField(max_length=250)
    order_number = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)   
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================



#====================================== E Employee Daily Work Statement Model =====================
class E_employee_daily_work_statement(models.Model):
    employee_name = models.CharField(max_length=250)  
    work_start_time = models.CharField(max_length=250)
    employee_code = models.CharField(max_length=250)
    work_end_time = models.CharField(max_length=250)
    serial_number_1 = models.CharField(max_length=250)
    file_number_1 = models.CharField(max_length=250)
    work_name_1 = models.CharField(max_length=250)
    work_status_1 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_1') #select option filed 
    serial_number_2 = models.CharField(max_length=250)
    file_number_2 = models.CharField(max_length=250)
    work_name_2 = models.CharField(max_length=250)
    work_status_2 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_2') #select option filed 
    serial_number_3 = models.CharField(max_length=250)
    file_number_3 = models.CharField(max_length=250)
    work_name_3 = models.CharField(max_length=250)
    work_status_3 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_3') #select option filed 
    serial_number_4 = models.CharField(max_length=250)
    file_number_4 = models.CharField(max_length=250)
    work_name_4 = models.CharField(max_length=250)
    work_status_4 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_4') #select option filed 
    serial_number_5 = models.CharField(max_length=250)
    file_number_5 = models.CharField(max_length=250)
    work_name_5 = models.CharField(max_length=250)
    work_status_5 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_5') #select option filed 
    serial_number_6 = models.CharField(max_length=250)
    file_number_6 = models.CharField(max_length=250)
    work_name_6 = models.CharField(max_length=250)
    work_status_6 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_6') #select option filed 
    serial_number_7 = models.CharField(max_length=250)
    file_number_7 = models.CharField(max_length=250)
    work_name_7 = models.CharField(max_length=250)
    work_status_7 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_7') #select option filed 
    serial_number_8 = models.CharField(max_length=250)
    file_number_8 = models.CharField(max_length=250)
    work_name_8 = models.CharField(max_length=250)
    work_status_8 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_8') #select option filed 
    serial_number_9 = models.CharField(max_length=250)
    file_number_9 = models.CharField(max_length=250)
    work_name_9 = models.CharField(max_length=250)
    work_status_9 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_9') #select option filed 
    serial_number_10 = models.CharField(max_length=250)
    file_number_10 = models.CharField(max_length=250)
    work_name_10 = models.CharField(max_length=250)
    work_status_10 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_10') #select option filed 
    date = models.CharField(max_length=250)
    charge_officer_name = models.CharField(max_length=250)
    status_1 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='status_1') #select option filed 
    chief_executive_officer_name = models.CharField(max_length=250)  
    status_2 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='status_2') #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================


#====================================== E Employee Live Status Model ==============================
class E_employee_live_status(models.Model):
    employee_live_or_leave_status = models.ForeignKey(Employee_Live_and_Leave_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    employee_id_number = models.CharField(max_length=250)
    employee_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================



#====================================== Staff Work Allotment Model ================================
class Staff_work_allotment(models.Model):
    work_assign_office = models.ForeignKey(Work_Assign_Office, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    name_of_employee = models.CharField(max_length=250)
    work_start_date = models.CharField(max_length=250)
    work_start_time = models.CharField(max_length=250)
    work_name = models.CharField(max_length=250)
    upload_work = models.CharField(max_length=250)
    work_finishing_date = models.CharField(max_length=250)
    work_finishing_time= models.CharField(max_length=250)
    work_head_name = models.CharField(max_length=250)
    current_status = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
#==================================================================================================
#==================================================================================================