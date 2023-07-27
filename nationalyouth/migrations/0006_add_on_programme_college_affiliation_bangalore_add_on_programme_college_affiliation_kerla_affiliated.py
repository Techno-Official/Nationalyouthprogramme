# Generated by Django 3.2.8 on 2023-07-24 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0005_auto_20230720_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocational_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('add_on_exam_fees', models.IntegerField(default=0)),
                ('admission_fee_1', models.IntegerField(default=0)),
                ('exam_fee_1', models.IntegerField(default=0)),
                ('transcript_fee_1', models.IntegerField(default=0)),
                ('total_fee_1', models.IntegerField(default=0)),
                ('admission_fee_2', models.IntegerField(default=0)),
                ('exam_fee_2', models.IntegerField(default=0)),
                ('transcript_fee_2', models.IntegerField(default=0)),
                ('total_fee_2', models.IntegerField(default=0)),
                ('yearly_exam_fee', models.IntegerField(default=0)),
                ('gst', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
            ],
        ),
        migrations.CreateModel(
            name='PG_Diploma_Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('add_on_exam_fees', models.IntegerField(default=0)),
                ('admission_fee_1', models.IntegerField(default=0)),
                ('exam_fee_1', models.IntegerField(default=0)),
                ('transcript_fee_1', models.IntegerField(default=0)),
                ('total_fee_1', models.IntegerField(default=0)),
                ('admission_fee_2', models.IntegerField(default=0)),
                ('exam_fee_2', models.IntegerField(default=0)),
                ('transcript_fee_2', models.IntegerField(default=0)),
                ('total_fee_2', models.IntegerField(default=0)),
                ('gst', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('remark', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
            ],
        ),
        migrations.CreateModel(
            name='Diploma_Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('add_on_exam_fees', models.IntegerField(default=0)),
                ('admission_fee_1', models.IntegerField(default=0)),
                ('exam_fee_1', models.IntegerField(default=0)),
                ('transcript_fee_1', models.IntegerField(default=0)),
                ('total_fee_1', models.IntegerField(default=0)),
                ('gst', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('remark', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('add_on_exam_fees', models.IntegerField(default=0)),
                ('admission_fee_1', models.IntegerField(default=0)),
                ('exam_fee_1', models.IntegerField(default=0)),
                ('transcript_fee_1', models.IntegerField(default=0)),
                ('total_fee_1', models.IntegerField(default=0)),
                ('gst', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('remark', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
            ],
        ),
        migrations.CreateModel(
            name='Affiliated_Vocational_Training_College_Kerla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('affiliation_number', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('principal_id', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('current_status', models.CharField(blank=True, choices=[('1', 'ACTIVE'), ('2', 'INACTIVE')], default='', max_length=25, null=True)),
                ('college_type', models.CharField(blank=True, choices=[('1', 'AIDED'), ('2', 'UN-AIDED')], default='', max_length=25, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name')),
            ],
        ),
        migrations.CreateModel(
            name='Add_on_Programme_College_Affiliation_Kerla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('district', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('affiliation_number', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('principal_id', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name')),
            ],
        ),
        migrations.CreateModel(
            name='Add_on_Programme_College_Affiliation_Bangalore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('district', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('affiliation_number', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('principal_id', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name')),
            ],
        ),
    ]
