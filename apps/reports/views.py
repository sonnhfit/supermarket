from django.shortcuts import render
from django.views import View
# Create your views here.


class ViewReport(View):

    def get(self, request):
        return render(request, 'admin/create_report.html')
