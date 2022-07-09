from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")


class Suppler(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    adress = models.CharField(max_length=200)
    rut = models.IntegerField(max_length=15)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField(default=1)
    code = models.CharField(max_length=10)
    comments = models.CharField(max_length=260)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Suppler, on_delete=models.CASCADE, blank=True, default=""
    )
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    document = models.IntegerField(max_length=15)
    document_type = models.CharField(max_length=20)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")


class Transaction(models.Model):
    total = models.FloatField()
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, default=""
    )
    is_invoice = models.BooleanField()
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")


class TransactionProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")
