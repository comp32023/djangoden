from django.db import models

class compcena(models.Model):
    id_cena = models.IntegerField(primary_key=True)
    purchase_price = models.IntegerField()
    price_for_sale = models.IntegerField()
    date_of_purchase = models.DateField()
    info = models.TextField(default=0)
    info2 = models.IntegerField(default=0)