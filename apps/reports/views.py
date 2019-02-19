from django.shortcuts import render
from django.views import View
from .models import Report
# Create your views here.


class ViewReport(View):

    def get(self, request):
        Report.objects.create()
        return render(request, 'admin/create_report.html')
