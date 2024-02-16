from django.shortcuts import render
from django.http import HttpResponse
from .models import productinformation, sale, photo


def index(request):
    return render(request, "index.html")


def page_dostavka(request):
    return render(request, "dostavka.html")


def catalog(request):
    return render(request, "katalog.html")


def order2(request):
    return render(request, "korzina.html")


#
#
# Каталог товаров - =========================================================================================================================
def televizory(request):
    name_tovar = productinformation.objects.filter(id=1)
    price = sale.objects.filter(id_sale=1)
    image = photo.objects.filter(id=1)
    name_tovar2 = productinformation.objects.filter(id=2)
    price2 = sale.objects.filter(id_sale=2)
    image2 = photo.objects.filter(id=2)
    name_tovar3 = productinformation.objects.filter(id=3)
    price3 = sale.objects.filter(id_sale=3)
    image3 = photo.objects.filter(id=3)
    name_tovar4 = productinformation.objects.filter(id=4)
    price4 = sale.objects.filter(id_sale=4)
    image4 = photo.objects.filter(id=4)

    data = {
        'name_tovar': name_tovar,
        'price': price,
        'image': image,
        'name_tovar2': name_tovar2,
        'price2': price2,
        'image2': image2,
        'name_tovar3': name_tovar3,
        'price3': price3,
        'image3': image3,
        'name_tovar4': name_tovar4,
        'price4': price4,
        'image4': image4,
    }
    return render(request, "tovari.html", data)


#
#
#
def cold_storage(request):
    return render(request, "tovari.html")


def noytbyki(request):
    return render(request, "tovari.html")


def kofemashini(request):
    return render(request, "tovari.html")


def proektori(request):
    return render(request, "tovari.html")


def fleshki(request):
    return render(request, "tovari.html")


# # Товары, их описание - =========================================================================================================================
def tovar(request):
    return render(request, "opisanietovara.html")


def tovar2(request):
    return render(request, "opisanietovara.html")

# people = productinformation.objects.filter(id__range=(1, 3))
# print(people)
#
# #
# # def test(request):
# #     id = product_information.objects.filter(id_product=1)
# #     price = sale.objects.filter(id_sale=1)
# #
# #     data = {
# #         'id': id,
# #         'price': price,
# #
# #     }
# #     return render(request, "tovar-televizor.html", data)
# #
# # def test2(request):
# #     id = product_information.objects.filter(id_product=2)
# #     price = sale.objects.filter(id_sale=2)
# #     data = {
# #         'id': id,
# #         'price': price,
# #     }
# #     return render(request, "tovar-televizor.html", data)
# #
# # def testcar(request):
# #     cart = photo.objects.filter(id=2)
# #     data = {
# #         'cart': cart,
# #     }
# #     return render(request, "test.html", data)
