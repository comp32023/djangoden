from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime


class categories(models.Model):
    category_name = models.TextField()

    class Meta():
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.id}, {self.category_name}"
class product_information(models.Model):
    id = models.IntegerField(verbose_name='ID')
    name_product = models.CharField(max_length=150, verbose_name='Имя продукта')
    category = models.OneToOneField(categories, on_delete=models.CASCADE, primary_key=True)
    weight = models.TextField(null=True, blank='None')
    description = models.TextField(null=True, blank='None')
    structure_goods = models.TextField(null=True, blank='None')
    possibleboundaries = models.TextField(null=True, blank='None')

    class Meta():
        verbose_name_plural = "Информация о товарах"

    def __str__(self):
        return f"{self.id}, {self.name_product}, Категория продукта - {self.category_id}, Описание - {self.description}"


class sale(models.Model):
    id_sale = models.IntegerField(primary_key = True)
    price = models.IntegerField()
    discounted_price = models.IntegerField(null=True, blank='None')
    purchase_price = models.IntegerField(null=True, blank='None')
    provider = models.TextField(null=True, blank='None')
    note = models.TextField(null=True, blank='None')
    product = models.ForeignKey(product_information, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = "Цена товаров"

    def __str__(self):
        return f"{self.id_sale}, {self.price}"


class orders(models.Model):
    purchase = models.TextField()
    price = models.IntegerField()
    purchase_note = models.TextField(null=True, blank='None')
    date = models.IntegerField()
    order_status = models.TextField()  # статус заказа(в ожидании, ожидает оплату, подтверждён)

    class Meta():
        verbose_name_plural = "Категория"

    def __str__(self):
        return f"{self.id}, {self.purchase}, {self.price},{self.purchase_note},{self.date},{self.order_status}"


class photo(models.Model):
    image = models.ImageField(blank=True, null=True)
    note = models.TextField(null=True, blank='None')

    class Meta():
        verbose_name_plural = "Фотографии"
    def __str__(self):
        return f"{self.id},{self.note}"