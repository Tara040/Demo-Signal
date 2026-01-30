from django.urls import path
from demo_app.views import *

urlpatterns = [
    path('test-sync-thread/', test_sync_and_thread),
    path('test-transaction/', test_transaction),
]
