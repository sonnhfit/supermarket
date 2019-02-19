from django.contrib import admin
from django.contrib import messages
# Register your models here.

from .models import Category, Product, Variation
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = ('title', 'price', 'active',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def message_user(self, *args):
        pass

    def save_model(self, request, obj, form, change):
        super(CategoryAdmin, self).save_model(request, obj, form, change)
        messages.success(request, 'Bạn vừa thêm loại sản phẩm thành công')


class VariationAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale_price', 'inventory', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
