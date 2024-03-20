# Generated by Django 5.0 on 2024-01-24 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0016_remove_mark_list_registration_practical_mark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_registration',
            name='address',
            field=models.TextField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='admission_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='admission_fees',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='college_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.college_name'),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='course_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name'),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='district',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='id_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exam_registration',
            name='name_of_student',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]