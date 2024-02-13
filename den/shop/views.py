from django.shortcuts import render
from django.http import HttpResponse
from .models import product_information, sale, photo



def index(request):
    return HttpResponse("<h2>Главная</h2>")

def test(request):
    id = product_information.objects.filter(id_product=1)
    price = sale.objects.filter(id_sale=1)

    data = {
        'id': id,
        'price': price,

    }
    return render(request, "tovar-televizor.html", data)

def test2(request):
    id = product_information.objects.filter(id_product=2)
    price = sale.objects.filter(id_sale=2)
    data = {
        'id': id,
        'price': price,
    }
    return render(request, "tovar-televizor.html", data)

def testcar(request):
    cart = photo.objects.filter(id=2)
    data = {
        'cart': cart,
    }
    return render(request, "test.html", data)

