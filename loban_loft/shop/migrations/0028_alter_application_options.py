# Generated by Django 4.1.7 on 2023-03-30 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_application'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'заявка', 'verbose_name_plural': 'заявки'},
        ),
    ]
