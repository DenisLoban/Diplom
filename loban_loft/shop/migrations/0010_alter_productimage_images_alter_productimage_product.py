# Generated by Django 4.1.7 on 2023-03-12 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_image_productimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ProductImages', to='shop.product'),
        ),
    ]
