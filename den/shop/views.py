from django.shortcuts import render
from django.http import HttpResponse
from .models import productinformation

def index(request):
    return render(request, "index.html")

def page_dostavka(request):
    return render(request, "dostavka.html")

def catalog(request):
    return render(request, "katalog.html")

def order2(request):
    return render(request, "korzina.html")

# def message(request):
#     return render(request, "message.html")



# Каталог товаров - =========================================================================================================================

def lections_detail(request, lecture_id): # lecture_id
    tovar = productinformation.objects.filter(id=lecture_id)

    context = {
        'tv': tovar,
    }
    return render(request, "opisanietovara.html", context)

def televizory(request):
    products = productinformation.objects.filter(category_id=1).order_by('id').values()


    for item in products:
        print(item['id'], item['name_product'])


    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def cold_storage(request):
    products = productinformation.objects.filter(category_id=2).order_by('id').values()

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def noytbyki(request):
    products = productinformation.objects.filter(category_id=3).order_by('id').values()

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)



def kofemashini(request):
    products = productinformation.objects.filter(category_id=4).order_by('id').values()

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def proektori(request):
    products = productinformation.objects.filter(category_id=5).order_by('id').values()

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def fleshki(request):
    products = productinformation.objects.filter(category_id=6).order_by('id').values()

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)
