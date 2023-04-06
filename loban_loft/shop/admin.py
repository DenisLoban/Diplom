
from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem, Reviews, About, Application, Profile


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Application)
class ApplicatiomAdmin(admin.ModelAdmin):
    pass



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # колоны которые будут отображаться
    list_filter = ('category',)  # фильтрация
    list_editable = ('title', 'description')  # атрибуты доступны для редактирования
    search_fields = ('title', 'description')  # поиск
    prepopulated_fields = {'slug': ('title',)}  # для генерации слага по имени
    actions = ['make_published', 'make_unpublished']  # снять с публикации



    def make_published(self, request, queryset):
        row_update = queryset.update(is_published=True)
        if row_update == 1:
            message_bit = '1 запись добавлена в публикации'
        else:
            message_bit = f'{row_update} записей были опубликованы'
        self.message_user(request, f'{message_bit}')



    def make_unpublished(self, request, queryset):
        row_update = queryset.update(is_published=False)
        if row_update == 1:
            message_bit = '1 запись снята с публикации'
        else:
            message_bit = f'{row_update} записей сняты с публикации'
        self.message_user(request, f'{message_bit}')

    make_published.short_description = 'выставить на продажу'
    make_published.allowed_permission = ('change',)

    make_unpublished.short_description = 'снять с продажи'
    make_unpublished.allowed_permission = ('change',)