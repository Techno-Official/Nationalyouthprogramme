# Generated by Django 3.2.8 on 2023-07-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0002_e_employee_live_status_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_employee_live_status',
            name='employee_name',
            field=models.CharField(max_length=250),
        ),
    ]
