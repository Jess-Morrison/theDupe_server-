from django.db import models

class Company(models.Model):
    id = models.AutoField()
    company_name = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
