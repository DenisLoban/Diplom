# Generated by Django 4.1.7 on 2023-04-01 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
