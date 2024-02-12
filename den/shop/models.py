from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class product_information(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_product = models.CharField(200)
    category_id = models.IntegerField(null=True)
    weight = models.TextField(null=True)
    description = models.TextField(null=True)
    structure_goods = models.TextField(null=True)
    possibleboundaries = models.TextField(null=True)

class categories(models.Model):
    id_category = models.IntegerField(primary_key=True)
    category_name = models.TextField()

class sale(models.Model):
    id_sale = models.IntegerField(primary_key=True)
    name_sale = models.CharField(200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(null=True)
    purchase_price = models.IntegerField(null=True)
    provider = models.TextField(null=True)
    note = models.TextField(null=True)

class orders(models.Model):
    id_purchase = models.IntegerField(primary_key=True)
    purchase = models.TextField()
    price = models.IntegerField()
    purchase_note = models.TextField(null=True)
    date = models.IntegerField()
    order_status = models.TextField() # статус заказа(в ожидании, ожидает оплату, подтверждён)


class photo(models.Model):
    id_photo = models.CharField(max_length=150)
    id_product = models.CharField(200)
    imagep = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
