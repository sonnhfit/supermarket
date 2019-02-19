from .models import BillDetail


def total_price_bills(bill_id):
    item_bills = BillDetail.objects.filter(bill_id=bill_id)
    price_count = 0
    for it in item_bills:
        price_count += (it.product.price*it.quantity)

    return price_count
