import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

# Controls which test is running
TEST_MODE = None   # "sync", "transaction"

@receiver(post_save, sender=Order)
def order_signal(sender, instance, **kwargs):
    print("Signal started")
    print("Signal thread ID:", threading.get_ident())

    # Q1: Synchronous proof
    if TEST_MODE == "sync":
        time.sleep(5)

    # Q3: Transaction rollback proof
    if TEST_MODE == "transaction":
        print("Raising exception inside signal")
        raise Exception("Signal failure")

    print("Signal finished")
