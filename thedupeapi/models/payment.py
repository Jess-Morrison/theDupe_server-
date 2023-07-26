from django.db import models

class PaymentType(models.Model):
    payment_type  = models.CharField(max_length=12)
