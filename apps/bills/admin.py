from django.contrib import admin
from apps.bills.models import BillDetail, Bills
# Register your models here.

admin.site.register(Bills)
admin.site.register(BillDetail)
