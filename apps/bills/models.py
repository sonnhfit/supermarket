from django.db import models
from apps.products import models as product_models
from django.contrib.auth.models import User
# Create your models here.


class BillDetail(models.Model):
    product = models.ForeignKey(product_models.Variation, on_delete=models.CASCADE, verbose_name='sản phẩm')
    quantity = models.IntegerField(default=0, verbose_name='số lượng')

    class Meta:
        verbose_name_plural = "Chi tiết hóa đơn"


class Bills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='người tạo hóa đơn')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo hóa đơn')
    bill_detail = models.ForeignKey(BillDetail, on_delete=models.CASCADE, verbose_name='chi tiết hóa đơn')
    bill_description = models.TextField(verbose_name='Mô tả hóa đơn')

    def __str__(self):
        return 'hóa đơn số %s'%self.id

    class Meta:
        verbose_name_plural = "Hóa đơn"
