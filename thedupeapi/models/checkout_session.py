from django.db import models

class CheckoutSession(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    order = models.OneToOneField("Order", on_delete=models.CASCADE)
    payment_details = models.ForeignKey("PaymentType", on_delete=models.CASCADE)
    shipping_details = models.CharField(max_length=55)
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    active_status = models.BooleanField()
