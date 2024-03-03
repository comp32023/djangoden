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


class productinformation(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Имя продукта')
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank='None')
    sale_product = models.IntegerField()
    image_product = models.ImageField(blank=True, null=True)
    image_product2 = models.ImageField(blank=True, null=True)

    class Meta():
        verbose_name_plural = "Информация о товарах"

    def __str__(self):
        return f"{self.id}, {self.name_product}, Категория продукта - {self.category_id}"

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email


# class sale(models.Model):
#     id_sale = models.IntegerField(primary_key=True)
#     price = models.IntegerField()
#     discounted_price = models.IntegerField(null=True, blank='None')
#     purchase_price = models.IntegerField(null=True, blank='None')
#     provider = models.TextField(null=True, blank='None')
#     note = models.TextField(null=True, blank='None')
#     product = models.OneToOneField(productinformation, on_delete=models.CASCADE)#Связь с другой таблицей
#
#     class Meta():
#         verbose_name_plural = "Цена товаров"
#
#     def __str__(self):
#         return f"{self.id_sale}, {self.price}"


# class photo(models.Model):
#     image = models.ImageField(blank=True, null=True)
#     note = models.TextField(null=True, blank='None')
#
#     class Meta():
#         verbose_name_plural = "Фотографии"
#     def __str__(self):
#         return f"{self.id},{self.note}"
#
# class orders(models.Model):
#     purchase = models.TextField()
#     price = models.IntegerField()
#     purchase_note = models.TextField(null=True, blank='None')
#     date = models.IntegerField()
#     order_status = models.TextField()  # статус заказа(в ожидании, ожидает оплату, подтверждён)
#
#     class Meta():
#         verbose_name_plural = "Категория"
#
#     def __str__(self):
#         return f"{self.id}, {self.purchase}, {self.price},{self.purchase_note},{self.date},{self.order_status}"