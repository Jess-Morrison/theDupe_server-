from django.db import models

class CheckoutSession(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    payment_details = models.ForeignKey("PaymentType", on_delete=models.CASCADE)
    shipping_details = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    active_status = models.BooleanField()
