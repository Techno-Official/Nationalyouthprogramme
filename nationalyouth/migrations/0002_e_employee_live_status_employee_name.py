# Generated by Django 3.2.8 on 2023-07-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='e_employee_live_status',
            name='employee_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
