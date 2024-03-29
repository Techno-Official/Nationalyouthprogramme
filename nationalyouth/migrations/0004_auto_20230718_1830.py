# Generated by Django 3.2.8 on 2023-07-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0003_alter_e_employee_live_status_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark_list_registration',
            name='grade',
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='external_marks_1',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='external_marks_2',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='external_marks_3',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='external_marks_4',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='grade_1',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='grade_2',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='grade_3',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='mark_list_registration',
            name='grade_4',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='mark_list_registration',
            name='mark_obtained_1',
            field=models.CharField(default='', max_length=250),
        ),
    ]
