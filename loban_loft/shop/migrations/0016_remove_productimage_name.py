# Generated by Django 4.1.7 on 2023-03-17 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_productimage_options_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='name',
        ),
    ]
