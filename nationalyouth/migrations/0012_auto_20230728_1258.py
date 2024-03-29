# Generated by Django 3.2.8 on 2023-07-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0011_alter_admission_registration_registration_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='admission_registration',
            name='registration_number',
            field=models.IntegerField(unique=True),
        ),
    ]
