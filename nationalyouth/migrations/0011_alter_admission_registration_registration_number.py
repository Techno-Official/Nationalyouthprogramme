# Generated by Django 3.2.8 on 2023-07-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0010_alter_admission_registration_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission_registration',
            name='registration_number',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]
