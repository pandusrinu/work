# from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Product(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(null=False)
    item_cost = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(default=0)
    volume = models.PositiveIntegerField(blank=True, null=False)


class Meta:
        Product = ['Name', 'item_cost', 'stock_quantity', 'volume']