# Generated by Django 4.1.7 on 2023-03-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_category_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'фото к товару', 'verbose_name_plural': 'фото к товару'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(default=2, max_length=100, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.ImageField(upload_to='products_image/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар'),
        ),
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='сообщение')),
                ('parents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.coments', verbose_name='родитель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
    ]
