# Generated by Django 5.0 on 2024-02-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0018_mark_list_registration_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark_list_registration',
            name='result',
            field=models.CharField(blank=True, choices=[('1', 'Passed'), ('2', 'Failed')], max_length=25, null=True),
        ),
    ]