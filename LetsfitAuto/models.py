from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

