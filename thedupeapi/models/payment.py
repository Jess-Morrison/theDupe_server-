from django.db import models

class PaymentType(models.Model):
    id = models.AutoField()
    payment_type  = models.CharField(max_length=12)
