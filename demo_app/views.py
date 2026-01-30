import threading
from django.http import HttpResponse
from django.db import transaction
from .models import Order
import demo_app.signals as signals


# ✅ Question 1 + Question 2
def test_sync_and_thread(request):
    signals.TEST_MODE = "sync"

    print("Before save")
    print("View thread ID:", threading.get_ident())

    Order.objects.create(name="Sync Test Order")

    print("After save")
    return HttpResponse("Q1 & Q2 tested")


# ✅ Question 3
def test_transaction(request):
    signals.TEST_MODE = "transaction"

    try:
        with transaction.atomic():
            Order.objects.create(name="Transaction Test Order")
    except Exception as e:
        print("Exception caught in view:", e)

    exists = Order.objects.filter(name="Transaction Test Order").exists()
    print("Order exists in DB:", exists)

    return HttpResponse("Q3 tested")
