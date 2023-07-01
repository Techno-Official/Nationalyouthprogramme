# Generated by Django 3.2.8 on 2023-07-01 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_on_College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_on_college_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Amount_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='College_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Live_and_Leave_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_live_and_leave_status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Record_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_record_type', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Fees_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_fees_type', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fee_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_type', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_course_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mark_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Particulars_Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular_head', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_account', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Assign_Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_assign_office', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff_work_allotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_employee', models.CharField(max_length=250)),
                ('work_start_date', models.CharField(max_length=250)),
                ('work_start_time', models.CharField(max_length=250)),
                ('work_name', models.CharField(max_length=250)),
                ('upload_work', models.CharField(max_length=250)),
                ('work_finishing_date', models.CharField(max_length=250)),
                ('work_finishing_time', models.CharField(max_length=250)),
                ('work_head_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('current_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.work_status')),
                ('work_assign_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.work_assign_office')),
            ],
        ),
        migrations.CreateModel(
            name='Pay_Online_Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=250)),
                ('type_of_fees', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('remark', models.CharField(max_length=250)),
                ('transaction_id', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('type_of_other_fees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.fee_type')),
            ],
        ),
        migrations.CreateModel(
            name='Mark_List_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('subject_1', models.CharField(max_length=250)),
                ('subject_2', models.CharField(max_length=250)),
                ('subject_3', models.CharField(max_length=250)),
                ('subject_4', models.CharField(max_length=250)),
                ('internal_marks_1', models.CharField(max_length=250)),
                ('internal_marks_2', models.CharField(max_length=250)),
                ('internal_marks_3', models.CharField(max_length=250)),
                ('internal_marks_4', models.CharField(max_length=250)),
                ('mark_obtained_1', models.CharField(max_length=250)),
                ('mark_obtained_2', models.CharField(max_length=250)),
                ('mark_obtained_3', models.CharField(max_length=250)),
                ('mark_obtained_4', models.CharField(max_length=250)),
                ('total_1', models.CharField(max_length=250)),
                ('total_2', models.CharField(max_length=250)),
                ('total_3', models.CharField(max_length=250)),
                ('total_4', models.CharField(max_length=250)),
                ('viva_mark', models.CharField(max_length=250)),
                ('grade', models.CharField(max_length=250)),
                ('mark_enter_clerk_name', models.CharField(max_length=250)),
                ('mark_check_clerk_name', models.CharField(max_length=250)),
                ('second_verified_officer_name', models.CharField(max_length=250)),
                ('final_mark_verified_officer_name', models.CharField(max_length=250)),
                ('result_enter_register_book_number', models.CharField(max_length=250)),
                ('mark_obtained', models.CharField(max_length=250)),
                ('total_mark', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('mark_check_clerk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mark_check_cleark_status', to='nationalyouth.mark_status')),
                ('mark_enter_clerk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.mark_status')),
                ('result_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.result_status')),
                ('second_verified_officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_verified_officer_status', to='nationalyouth.mark_status')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=250)),
                ('exam_attendance', models.CharField(max_length=250)),
                ('any_fees_concession', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('principal_code', models.CharField(max_length=250)),
                ('principal_name', models.CharField(max_length=250)),
                ('online_fees', models.CharField(max_length=250)),
                ('remark', models.TextField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('exam_fees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.exam_fees_type')),
                ('principal_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.status')),
            ],
        ),
        migrations.CreateModel(
            name='E_Office_Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_number', models.CharField(max_length=250)),
                ('file_subject', models.CharField(max_length=250)),
                ('remark', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('approval_first_officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approval_first_officer', to='nationalyouth.status')),
                ('approval_second_officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approval_second_officer', to='nationalyouth.status')),
            ],
        ),
        migrations.CreateModel(
            name='E_Office_File_Sanction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docket_number', models.CharField(max_length=250)),
                ('employee_code', models.CharField(max_length=250)),
                ('employee_name', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=250)),
                ('file_name', models.CharField(max_length=250)),
                ('note_file', models.TextField(max_length=250)),
                ('general_note_sanction_order', models.TextField(max_length=250)),
                ('order_number', models.CharField(max_length=250)),
                ('remark', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('officer_grade_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer_grade_1_status', to='nationalyouth.status')),
                ('officer_grade_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer_grade_2_status', to='nationalyouth.status')),
                ('sanction_clerk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sanction_clerk_status', to='nationalyouth.status')),
            ],
        ),
        migrations.CreateModel(
            name='E_Office_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_number', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('bank_name', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('transaction_number', models.CharField(max_length=250)),
                ('remark', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('amount2', models.CharField(max_length=250)),
                ('file_referral_number', models.CharField(max_length=250)),
                ('office_registration_number', models.CharField(max_length=250)),
                ('pan_card_number', models.CharField(max_length=250)),
                ('officer_incharge_name', models.CharField(max_length=250)),
                ('secretary_name', models.CharField(max_length=250)),
                ('remark_staff_approval', models.CharField(max_length=250)),
                ('remark_officer_approval', models.CharField(max_length=250)),
                ('office_referral_number', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name')),
                ('officer_incharge_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer_incharge_status', to='nationalyouth.status')),
                ('particular_head', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.particulars_head')),
                ('secretary_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secretry_status', to='nationalyouth.status')),
                ('type_of_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.type_of_account')),
            ],
        ),
        migrations.CreateModel(
            name='E_Employee_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('employee_code', models.CharField(max_length=250)),
                ('office_address', models.TextField(max_length=250)),
                ('home_address', models.TextField(max_length=250)),
                ('contact_number', models.CharField(max_length=250)),
                ('aadhar_number', models.CharField(max_length=250)),
                ('husband_or_wife_name', models.CharField(max_length=250)),
                ('father_name', models.CharField(max_length=250)),
                ('age_of_father', models.CharField(max_length=250)),
                ('mother_name', models.CharField(max_length=250)),
                ('age_of_mother', models.CharField(max_length=250)),
                ('child_name_1', models.CharField(max_length=250)),
                ('age_of_child_1', models.CharField(max_length=250)),
                ('child_name_2', models.CharField(max_length=250)),
                ('age_of_child_2', models.CharField(max_length=250)),
                ('child_name_3', models.CharField(max_length=250)),
                ('age_of_child_3', models.CharField(max_length=250)),
                ('scale_of_pay', models.CharField(max_length=250)),
                ('employee_liablity', models.CharField(max_length=250)),
                ('employee_promotion', models.CharField(max_length=250)),
                ('employee_grade', models.CharField(max_length=250)),
                ('salary', models.CharField(max_length=250)),
                ('advance', models.CharField(max_length=250)),
                ('bonus', models.CharField(max_length=250)),
                ('loan', models.CharField(max_length=250)),
                ('note', models.TextField(max_length=250)),
                ('remark', models.TextField(max_length=250)),
                ('suspension', models.CharField(max_length=250)),
                ('showcase_notice', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('employee_record_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.employee_record_type')),
            ],
        ),
        migrations.CreateModel(
            name='E_employee_live_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id_number', models.CharField(max_length=250)),
                ('employee_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('employee_live_or_leave_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.employee_live_and_leave_status')),
            ],
        ),
        migrations.CreateModel(
            name='E_employee_daily_work_statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=250)),
                ('work_start_time', models.CharField(max_length=250)),
                ('employee_code', models.CharField(max_length=250)),
                ('work_end_time', models.CharField(max_length=250)),
                ('serial_number_1', models.CharField(max_length=250)),
                ('file_number_1', models.CharField(max_length=250)),
                ('work_name_1', models.CharField(max_length=250)),
                ('serial_number_2', models.CharField(max_length=250)),
                ('file_number_2', models.CharField(max_length=250)),
                ('work_name_2', models.CharField(max_length=250)),
                ('serial_number_3', models.CharField(max_length=250)),
                ('file_number_3', models.CharField(max_length=250)),
                ('work_name_3', models.CharField(max_length=250)),
                ('serial_number_4', models.CharField(max_length=250)),
                ('file_number_4', models.CharField(max_length=250)),
                ('work_name_4', models.CharField(max_length=250)),
                ('serial_number_5', models.CharField(max_length=250)),
                ('file_number_5', models.CharField(max_length=250)),
                ('work_name_5', models.CharField(max_length=250)),
                ('serial_number_6', models.CharField(max_length=250)),
                ('file_number_6', models.CharField(max_length=250)),
                ('work_name_6', models.CharField(max_length=250)),
                ('serial_number_7', models.CharField(max_length=250)),
                ('file_number_7', models.CharField(max_length=250)),
                ('work_name_7', models.CharField(max_length=250)),
                ('serial_number_8', models.CharField(max_length=250)),
                ('file_number_8', models.CharField(max_length=250)),
                ('work_name_8', models.CharField(max_length=250)),
                ('serial_number_9', models.CharField(max_length=250)),
                ('file_number_9', models.CharField(max_length=250)),
                ('work_name_9', models.CharField(max_length=250)),
                ('serial_number_10', models.CharField(max_length=250)),
                ('file_number_10', models.CharField(max_length=250)),
                ('work_name_10', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('charge_officer_name', models.CharField(max_length=250)),
                ('chief_executive_officer_name', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('status_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_1', to='nationalyouth.status')),
                ('status_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_2', to='nationalyouth.status')),
                ('work_status_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_1', to='nationalyouth.work_status')),
                ('work_status_10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_10', to='nationalyouth.work_status')),
                ('work_status_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_2', to='nationalyouth.work_status')),
                ('work_status_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_3', to='nationalyouth.work_status')),
                ('work_status_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_4', to='nationalyouth.work_status')),
                ('work_status_5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_5', to='nationalyouth.work_status')),
                ('work_status_6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_6', to='nationalyouth.work_status')),
                ('work_status_7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_7', to='nationalyouth.work_status')),
                ('work_status_8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_8', to='nationalyouth.work_status')),
                ('work_status_9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_status_9', to='nationalyouth.work_status')),
            ],
        ),
        migrations.CreateModel(
            name='Application_for_Affliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_institution', models.CharField(max_length=250)),
                ('mobile_number', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('status_of_institution_other', models.CharField(max_length=250)),
                ('year_of_establishment', models.CharField(max_length=250)),
                ('address', models.TextField(max_length=250)),
                ('pincode', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('education_qualification', models.CharField(max_length=250)),
                ('date_of_birth', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('profession_experience', models.CharField(max_length=250)),
                ('postal_address', models.CharField(max_length=250)),
                ('staff_room', models.CharField(max_length=250)),
                ('number_of_room_1', models.CharField(max_length=250)),
                ('seating_capacity_1', models.CharField(max_length=250)),
                ('total_area_1', models.CharField(max_length=250)),
                ('class_room', models.CharField(max_length=250)),
                ('number_of_room_2', models.CharField(max_length=250)),
                ('seating_capacity_2', models.CharField(max_length=250)),
                ('total_area_2', models.CharField(max_length=250)),
                ('laboratary', models.CharField(max_length=250)),
                ('number_of_room_3', models.CharField(max_length=250)),
                ('seating_capacity_3', models.CharField(max_length=250)),
                ('total_area_3', models.CharField(max_length=250)),
                ('reception', models.CharField(max_length=250)),
                ('number_of_room_4', models.CharField(max_length=250)),
                ('seating_capacity_4', models.CharField(max_length=250)),
                ('total_area_4', models.CharField(max_length=250)),
                ('toilet', models.CharField(max_length=250)),
                ('number_of_room_5', models.CharField(max_length=250)),
                ('seating_capacity_5', models.CharField(max_length=250)),
                ('total_area_5', models.CharField(max_length=250)),
                ('any_other', models.CharField(max_length=250)),
                ('number_of_room_6', models.CharField(max_length=250)),
                ('seating_capacity_6', models.CharField(max_length=250)),
                ('total_area_6', models.CharField(max_length=250)),
                ('type_of_computer_1', models.CharField(max_length=250)),
                ('number_terminal_1', models.CharField(max_length=250)),
                ('year_of_purchase_1', models.CharField(max_length=250)),
                ('cost_1', models.CharField(max_length=250)),
                ('software_facility_1', models.CharField(max_length=250)),
                ('other_facility_1', models.CharField(max_length=250)),
                ('type_of_computer_2', models.CharField(max_length=250)),
                ('number_terminal_2', models.CharField(max_length=250)),
                ('year_of_purchase_2', models.CharField(max_length=250)),
                ('cost_2', models.CharField(max_length=250)),
                ('software_facility_2', models.CharField(max_length=250)),
                ('other_facility_2', models.CharField(max_length=250)),
                ('type_of_computer_3', models.CharField(max_length=250)),
                ('number_terminal_3', models.CharField(max_length=250)),
                ('year_of_purchase_3', models.CharField(max_length=250)),
                ('cost_3', models.CharField(max_length=250)),
                ('software_facility_3', models.CharField(max_length=250)),
                ('other_facility_3', models.CharField(max_length=250)),
                ('type_of_computer_4', models.CharField(max_length=250)),
                ('number_terminal_4', models.CharField(max_length=250)),
                ('year_of_purchase_4', models.CharField(max_length=250)),
                ('cost_4', models.CharField(max_length=250)),
                ('software_facility_4', models.CharField(max_length=250)),
                ('other_facility_4', models.CharField(max_length=250)),
                ('serial_number_5', models.CharField(max_length=250)),
                ('type_of_computer_5', models.CharField(max_length=250)),
                ('number_terminal_5', models.CharField(max_length=250)),
                ('year_of_purchase_5', models.CharField(max_length=250)),
                ('cost_5', models.CharField(max_length=250)),
                ('software_facility_5', models.CharField(max_length=250)),
                ('other_facility_5', models.CharField(max_length=250)),
                ('serial_number_6', models.CharField(max_length=250)),
                ('type_of_computer_6', models.CharField(max_length=250)),
                ('number_terminal_6', models.CharField(max_length=250)),
                ('year_of_purchase_6', models.CharField(max_length=250)),
                ('cost_6', models.CharField(max_length=250)),
                ('software_facility_6', models.CharField(max_length=250)),
                ('other_facility_6', models.CharField(max_length=250)),
                ('serial_number_1', models.CharField(max_length=250)),
                ('name_1', models.CharField(max_length=250)),
                ('designation_1', models.CharField(max_length=250)),
                ('qualification_1', models.CharField(max_length=250)),
                ('teaching_experience_1', models.CharField(max_length=250)),
                ('date_of_appointment_1', models.CharField(max_length=250)),
                ('status_1', models.CharField(max_length=250)),
                ('serial_number_2', models.CharField(max_length=250)),
                ('name_2', models.CharField(max_length=250)),
                ('designation_2', models.CharField(max_length=250)),
                ('qualification_2', models.CharField(max_length=250)),
                ('teaching_experience_2', models.CharField(max_length=250)),
                ('date_of_appointment_2', models.CharField(max_length=250)),
                ('status_2', models.CharField(max_length=250)),
                ('serial_number_3', models.CharField(max_length=250)),
                ('name_3', models.CharField(max_length=250)),
                ('designation_3', models.CharField(max_length=250)),
                ('qualification_3', models.CharField(max_length=250)),
                ('teaching_experience_3', models.CharField(max_length=250)),
                ('date_of_appointment_3', models.CharField(max_length=250)),
                ('status_3', models.CharField(max_length=250)),
                ('serial_number_4', models.CharField(max_length=250)),
                ('name_4', models.CharField(max_length=250)),
                ('designation_4', models.CharField(max_length=250)),
                ('qualification_4', models.CharField(max_length=250)),
                ('teaching_experience_4', models.CharField(max_length=250)),
                ('date_of_appointment_4', models.CharField(max_length=250)),
                ('status_4', models.CharField(max_length=250)),
                ('center_address', models.CharField(max_length=250)),
                ('residential_address', models.CharField(max_length=250)),
                ('signature', models.CharField(max_length=250)),
                ('form_receive_date', models.CharField(max_length=250)),
                ('affliation_number', models.CharField(max_length=250)),
                ('total_affliation_fee', models.CharField(max_length=250)),
                ('registration_fee', models.CharField(max_length=250)),
                ('bank_name', models.CharField(max_length=250)),
                ('receipt_number', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('education_institution_type', models.CharField(max_length=250)),
                ('affliation_from_date', models.CharField(max_length=250)),
                ('affliation_to_date', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('amount_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.amount_status')),
                ('status_of_institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.institution_status')),
            ],
        ),
        migrations.CreateModel(
            name='Admission_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=250)),
                ('name_of_student', models.CharField(max_length=250)),
                ('address', models.TextField(max_length=250)),
                ('id_number', models.CharField(max_length=250)),
                ('date_of_birth', models.CharField(max_length=250)),
                ('mobile_number', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('admission_fees', models.CharField(max_length=250)),
                ('admission_month_and_year', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name')),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
                ('principal_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.status')),
            ],
        ),
        migrations.CreateModel(
            name='Add_on_Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=250)),
                ('student_name', models.CharField(max_length=250)),
                ('address', models.TextField(max_length=250)),
                ('id_number', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=250)),
                ('exam_fees', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('add_on_College', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.add_on_college')),
                ('college_coordinator_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.status')),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
                ('main_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.main_course')),
            ],
        ),
    ]