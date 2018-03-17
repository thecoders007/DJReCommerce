from django.db import models
from django.contrib.auth.models import User
from Seller.models import Product

# Create your models here.


class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.IntegerField()

    def __str__(self):
        return str(self.user_type)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    bill_no = models.CharField(max_length=100)

    def __str__(self):
        return str(self.bill_no)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    invoice = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.invoice)


class Forum(models.Model):
    comment = models.CharField(max_length=10000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

    def __str__(self):
        return str(self.comment)


class Rating(models.Model):
    rate = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.rate)
