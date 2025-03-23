from django.db import models
from django.contrib.auth.models import User

class Product (models.Model):
    PRODUCT_TYPE=[
        ("f", "food"),
        ("d", "drink"),
        ("b", "bakery"),
        ("c", "cosmetics"),
        ("h", "hygiene"),

    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE)
    is_homemade = models.BooleanField(default=False)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    def __str__(self):
        return self.street + " " + str(self.street_number)

class Market(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    number_of_markets = models.IntegerField()
    opening_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    working_from = models.TimeField()
    working_to = models.TimeField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ssn_number = models.IntegerField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class MarketProducts(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

