from django.contrib import admin
from apps.bills.models import BillDetail, Bills
from django.contrib import messages
# Register your models here.


class BillsAdmin(admin.ModelAdmin):

    list_display = ('user', 'time_created', 'bill_description',)

    def message_user(self, *args):
        pass

    def save_model(self, request, obj, form, change):
        super(BillsAdmin, self).save_model(request, obj, form, change)
        messages.success(request, 'Bạn vừa thêm sản phẩm thành công')


class BillsDetailAdmin(admin.ModelAdmin):

    list_display = ('bill', 'product', 'quantity',)

    def message_user(self, *args):
        pass

    def save_model(self, request, obj, form, change):
        super(BillsDetailAdmin, self).save_model(request, obj, form, change)
        messages.success(request, 'Bạn vừa thêm sản phẩm thành công')


admin.site.register(Bills, BillsAdmin)
admin.site.register(BillDetail, BillsDetailAdmin)
