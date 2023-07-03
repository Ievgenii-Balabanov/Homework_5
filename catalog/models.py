from django.contrib import admin
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self):
        return f"City name: {self.name}, Country: {self.country}"


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    manufacturer = models.CharField(max_length=30)
    price = models.IntegerField(default=None)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return f"Product name: {self.product_name}, Country: {self.manufacturer}, Price: {self.price}"


class Client(models.Model):
    client_city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    client_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    purchased_product = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        return (
            f"Client name: {self.client_name}, "
            f"Phone Number: {self.phone_number}, "
            f"Email: {self.email}, "
            f"Purchased products: {self.purchased_product}"
        )


class Supplier(models.Model):
    company_name = models.CharField(max_length=30)
    address = models.OneToOneField(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "supplier"
        verbose_name_plural = "suppliers"

    def __str__(self):
        return f"Company name: {self.company_name}, Address: {self.address}"


class Person(models.Model):  # noqa: DJ10,DJ11
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Logging(models.Model):  # noqa:DJ10,DJ11
    METHOD_CHOICES = [
        ("GET", "GET"),
        ("POST", "POST"),
    ]

    path = models.URLField(max_length=200)
    method = models.CharField(max_length=5, choices=METHOD_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    query_data = models.CharField(max_length=200, default=None)
    body_data = models.CharField(max_length=200, default=None)
    json_data = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.path
