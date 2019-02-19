from django.urls import path
from .views import CreateBills

app_name = 'bills'
urlpatterns = [
    path('create/', CreateBills.as_view(), name='create_bills')
]
