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


admin.site.register(Client)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(Supplier)
