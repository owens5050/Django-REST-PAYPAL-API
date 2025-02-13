from django.urls import path
from .views import PayPalPaymentView, ExecutePaymentView

urlpatterns = [
    path('paypal/payment/', PayPalPaymentView.as_view(), name='paypal-payment'),
    path('paypal/execute/', ExecutePaymentView.as_view(), name='paypal-execute'),
]
