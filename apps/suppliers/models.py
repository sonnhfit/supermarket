from django.db import models

# Create your models here.


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200, verbose_name='tên nhà cung cấp', null=False)
    supplier_address = models.CharField(max_length=200, verbose_name='địa chỉ nhà cung cấp', null=True)
    supplier_phone = models.CharField(max_length=200, verbose_name='số điện thoại', null=True)
    supplier_description = models.TextField(verbose_name='mô tả nhà cung cấp', null=True)

    def __str__(self):
        return self.supplier_name

    class Meta:
        verbose_name_plural = "Nhà cung cấp"
