from django.db import models

class User(models.Model):
    username  = models.CharField(max_length=12)
    first_name  = models.CharField(max_length=55)
    last_name  = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now=True)  
