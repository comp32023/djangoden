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
    # kateg = categories.objects.filter(id=id)
    televizori = productinformation.objects.all().order_by("id")

    data = {
        #'kateg': kateg,
        'televizori': televizori,
    }
    return render(request, "test.html", data)


def tovar2(request):
    return render(request, "opisanietovara.html")
