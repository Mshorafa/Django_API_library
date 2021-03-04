from django.db import models


# Create your models here.


class Expense(models.Model):
    amount = models.FloatField(max_length=255)
    merchent = models.CharField(max_length=255)
    decreption = models.CharField(max_length=255, blank=True, null=True)
    categroy = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_created = models.DateTimeField(auto_now=True)
