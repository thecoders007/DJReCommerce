from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    dealer = models.CharField(max_length=100)

    def __str__(self):
        return str(self.company)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_detail = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category_name)


class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.IntegerField()
    photo = models.ImageField()
    avaiblity = models.IntegerField()
    tag = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    warranty = models.IntegerField()
    average_rating = models.IntegerField()
    size = models.CharField(max_length=100)

    def __str__(self):
        return str(self.product_id)


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    validity = models.DateField()
    percent_discount = models.IntegerField()
    promocode = models.CharField(max_length=100)

    def __str__(self):
        return str(self.percent_discount)
