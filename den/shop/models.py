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

    class Meta():
        verbose_name = "Информация о товарах"
        verbose_name_plural = "Информация о товарах"

    def __str__(self):
        return f"{self.id_product}, {self.name_product}, Категория продукта - {self.category_id}, Описание - {self.description}"

class categories(models.Model):
    id_category = models.IntegerField(primary_key=True)
    category_name = models.TextField()

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return f"{self.id_category}, {self.category_name}"


class sale(models.Model):
    id_sale = models.IntegerField(primary_key=True)
    name_sale = models.CharField(200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(null=True)
    purchase_price = models.IntegerField(null=True)
    provider = models.TextField(null=True)
    note = models.TextField(null=True)

    class Meta():
        verbose_name = "Цену товаров"
        verbose_name_plural = "Цена товаров"

    def __str__(self):
        return f"{self.id_sale}, {self.name_sale}, {self.price}"


class orders(models.Model):
    id_purchase = models.IntegerField(primary_key=True)
    purchase = models.TextField()
    price = models.IntegerField()
    purchase_note = models.TextField(null=True)
    date = models.IntegerField()
    order_status = models.TextField()  # статус заказа(в ожидании, ожидает оплату, подтверждён)

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return f"{self.id_purchase}, {self.purchase}, {self.price},{self.purchase_note},{self.date},{self.order_status}"


class photo(models.Model):
    id_photo = models.IntegerField(primary_key=True)
    id_product = models.CharField(200)
    nazv_product = models.CharField(300)
    ph_image = models.ImageField(blank=True, null=True)

    class Meta():
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"
    def __str__(self):
        return f"{self.id}, Айди продукта - {self.id_product}, Название продукта - {self.nazv_product}"
