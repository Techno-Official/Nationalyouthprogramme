# Generated by Django 5.0 on 2024-04-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0020_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/download/uploads/news_image/'),
        ),
    ]
