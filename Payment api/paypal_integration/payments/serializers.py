from rest_framework import serializers
# payments/serializers.py serializer to handle the payment data:#

class PaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=3, default="USD")