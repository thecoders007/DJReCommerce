
from django.contrib import admin
from .models import Seller, Category, Product, Discount

# Register your models here.
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
