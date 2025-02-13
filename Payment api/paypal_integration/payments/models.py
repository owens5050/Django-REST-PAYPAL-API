from django.db import models

class Payment(models.Model):
    payment_id = models.CharField(max_length=128)
    payer_id = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
