from django.db import models


class dummy(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)


class In_Product(models.Model):
    barcode_number = models.CharField(max_length=200,primary_key=True)
    product_item = models.CharField(max_length=200)
    product_price = models.IntegerField()
    Receipt_date = models.DateField()
    Expected_delivery_date = models.DateField(null=True)
    destination = models.CharField(max_length=200)
    etc = models.CharField(max_length=200,null=True)

class Out_Product(models.Model):
    barcode_number = models.CharField(max_length=200,primary_key=True)
    product_item = models.CharField(max_length=200)
    product_price = models.IntegerField()
    Receipt_date = models.DateField()
    Expected_delivery_date = models.DateField()
    destination = models.CharField(max_length=200)
    etc = models.CharField(max_length=200,null=True)


class Price_tag(models.Model):
    product_item = models.CharField(max_length=200)
    product_price = models.IntegerField()

class Master_table(models.Model):
    barcode_number = models.CharField(max_length=200,primary_key=True)
    product_item = models.CharField(max_length=200)
    product_price = models.IntegerField()
    Receipt_date = models.DateField()
    Expected_delivery_date = models.DateField()
    destination = models.CharField(max_length=200)
    etc = models.CharField(max_length=200,null=True)