# Generated by Django 4.2.5 on 2023-11-07 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0012_auto_20230728_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='VTC_Course_Admission_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.IntegerField(unique=True)),
                ('name_of_student', models.CharField(max_length=250)),
                ('address', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('id_number', models.CharField(max_length=250)),
                ('date_of_birth', models.CharField(max_length=250)),
                ('mobile_number', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('admission_fees', models.CharField(max_length=250)),
                ('admission_date', models.CharField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name')),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
                ('principal_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.status')),
            ],
        ),
    ]