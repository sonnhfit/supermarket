from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Report(models.Model):
    report_name = models.CharField(max_length=200, verbose_name='Tên báo cáo')
    report_time = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo báo cáo')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Người tạo báo cáo')
    tienhang = models.IntegerField(default=0, verbose_name='Tổng tiền hàng')
    thu = models.IntegerField(default=0, verbose_name='Tổng số tiền đã thu')
    chi = models.IntegerField(default=0, verbose_name='Tổng số tiền đã chi')

    def __str__(self):
        return 'báo cáo số %s'%self.id

    class Meta:
        verbose_name_plural = "Báo cáo"

