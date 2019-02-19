from django.shortcuts import render
from django.views import View
from .models import Bills, BillDetail
from apps.products.models import Variation
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class CreateBills(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        bill = Bills.objects.create(user=request.user)
        bill_item_list = BillDetail.objects.filter(bill_id=bill.id)
        context = {
            'bill_id': bill.id,
            'bill_item_list': bill_item_list
        }

        return render(request, 'admin/create_bill.html', context)

    def post(self, request):
        bill_id = request.POST['bill_id']
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']

        try:
            variation = Variation.objects.get(id=product_id)
        except ObjectDoesNotExist:
            messages.error(request, 'Mã sản phẩm không tồn tại')
            bill_item_list = BillDetail.objects.filter(bill_id=bill_id)
            context = {
                'bill_id': bill_id,
                'bill_item_list': bill_item_list
            }

            return render(request, 'admin/create_bill.html', context)

        BillDetail.objects.create(product=variation, quantity=quantity, bill_id=bill_id)
        bill_item_list = BillDetail.objects.filter(bill_id=bill_id)
        context = {
            'bill_id': bill_id,
            'bill_item_list': bill_item_list
        }

        return render(request, 'admin/create_bill.html', context)
