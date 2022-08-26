# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name', 'item_cost', 'stock_quantity', 'volume']


admin.site.register(Product, ProductAdmin)