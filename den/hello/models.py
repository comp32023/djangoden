from django.db import models

class product_information(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_product = models.CharField(200)
    category_id = models.IntegerField()
    weight = models.TextField(default=0)
    description = models.TextField(default=0)
    structure_goods = models.TextField(default=0)
    possibleboundaries = models.TextField(default=0)

class categories(models.Model):
    id_category = models.IntegerField(primary_key=True)
    category_name = models.TextField()

class sale(models.Model):
    id_sale = models.IntegerField(primary_key=True)
    name_sale = models.CharField(200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    purchase_price = models.IntegerField(default=0)
    provider = models.TextField(default=0)
    note = models.TextField(default=0)
class orders(models.Model):
    id_purchase = models.IntegerField(primary_key=True)
    purchase = models.TextField()
    price = models.IntegerField()
    purchase_note = models.TextField(default=0)
    date = models.IntegerField()
    order_status = models.TextField() # статус заказа(в ожидании, ожидает оплату, подтверждён)


