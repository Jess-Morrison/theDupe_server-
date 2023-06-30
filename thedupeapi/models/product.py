from django.db import models

class Product(models.Model):
    id = models.AutoField()
    company_id = models.ForeignKey("Company", on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    price = models.DecimalField(max_length=7,decimal_places=2)
    """Future Feature"""
    #product_type = models.ForeignKey("Type", on_delete=models.CASCADE)
