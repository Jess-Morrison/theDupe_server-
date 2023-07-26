from django.db import models

class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    dupe = models.ForeignKey("Dupe", on_delete=models.CASCADE)
    status = models.BooleanField()
    order_total = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    