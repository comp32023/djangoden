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


# Каталог товаров - =========================================================================================================================


def lections_detail(request, lecture_id): # lecture_id
    tovar = productinformation.objects.filter(id=lecture_id)
    people = productinformation.objects.filter(category_id=1)
    for person in people:
        print(f"{person.id} - {person.name_product}")
    # people = productinformation.objects.filter(id__range=(1, 12))
    context = {
        'tv': tovar,
        'people': people,
    }
    return render(request, "opisanietovara.html", context)

def televizory(request):
    products = productinformation.objects.filter(category_id=1)

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def cold_storage(request):
    products = productinformation.objects.filter(category_id=2)

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def noytbyki(request):
    products = productinformation.objects.filter(category_id=3)

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)



def kofemashini(request):
    products = productinformation.objects.filter(category_id=4)

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def proektori(request):
    products = productinformation.objects.filter(category_id=5)

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)


def fleshki(request):
    products = productinformation.objects.filter(category_id=6)

    context = {
        'pr': products,
    }

    return render(request, "tovari.html", context)
