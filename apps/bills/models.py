from django.db import models
from apps.products import models as product_models
from django.contrib.auth.models import User
# Create your models here.


class Bills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='người tạo hóa đơn')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo hóa đơn')

    bill_description = models.TextField(verbose_name='Mô tả hóa đơn', default='', null=True, blank=True)

    def __str__(self):
        return 'hóa đơn số %s'%self.id

    class Meta:
        verbose_name_plural = "Hóa đơn"


class BillDetail(models.Model):
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE,
                                    verbose_name='Hóa đơn', null=True, default=None, blank=True)
    product = models.ForeignKey(product_models.Variation, on_delete=models.CASCADE, verbose_name='sản phẩm')
    quantity = models.IntegerField(default=0, verbose_name='số lượng')

    class Meta:
        verbose_name_plural = "Chi tiết hóa đơn"
