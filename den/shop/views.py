from django.shortcuts import render
from django.http import HttpResponse
from .models import productinformation, categories


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



# def cold_storage(request):
#     return render(request, "tovari.html")
#
#
# def noytbyki(request):
#     return render(request, "tovari.html")
#
#
# def kofemashini(request):
#     return render(request, "tovari.html")
#
#
# def proektori(request):
#     return render(request, "tovari.html")
#
#
# def fleshki(request):
#     return render(request, "tovari.html")


# # Товары, их описание - =========================================================================================================================
def testcar(request):
    kateg = categories.objects.filter(id=id)
    televezori = productinformation.object.fiter(categories=id)
    data = {
        'kateg': kateg,
        'televezori': televezori,
    }
    return render(request, "test.html",data)


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
