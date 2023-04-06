from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='название',
        unique=True,
        null=False,
        blank=False
    )

    # slug = models.SlugField(verbose_name='Транслит', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'категория товара'
        verbose_name_plural = 'категориии товаров'

    # def __unicode__(self):
    #     return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='название товара',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='описание товара',
        max_length=4096,
        null=True,
        blank=True
    )
    descr = models.TextField(
        verbose_name='информация о товаре',
        max_length=4096,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='product/',
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='цена',
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )


    def get_absolute_url(self):
        return reverse('shop_product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class About(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='заглавная стока',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='вспомогательный текст',
        max_length=4096,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'о нас'
        verbose_name_plural = 'о нас'


class Application(models.Model):
    name = models.CharField('имя', max_length=32)
    number = models.CharField('номер телефона', max_length=17)
    message = models.CharField('Сообщение', max_length=5000)
    slug = models.SlugField(verbose_name='URL', unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'


class ProductImage(models.Model):
    title = models.CharField('Заголовок', max_length=100, null=False, blank=False)
    images = models.ImageField('Изображение', upload_to='products_image/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фото к товару'
        verbose_name_plural = 'фото к товару'


class Reviews(models.Model):
    # email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('сообщение', max_length=5000)
    parents = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return f'Order{self.pk}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'OrderItem{self.order} Product {self.product}'


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)


    def __str__(self):
        return str(self.user)