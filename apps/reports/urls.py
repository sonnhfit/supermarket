from django.urls import path
from .views import ViewReport
app_name = 'reports'
urlpatterns = [
    path('view/', ViewReport.as_view(), name='view_report')
]
