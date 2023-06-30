from django.db import models

class Order(models.Model):
    id = models.AutoField()
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    dupe_id = models.ForeignKey("Dupe", on_delete=models.CASCADE)
    status = models.BooleanField()
    order_total = models.DecimalField(max_length=7,decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    