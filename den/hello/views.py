from django.shortcuts import render
from django.http import HttpResponse
from .models import compcena


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    cena = compcena.objects.filter(id_cena=1)
    data = {'cena': cena}
    return render(request, "comp1.html", data)

def about2(request):
    cena = compcena.objects.filter(id_cena=2)
    data = {'cena': cena}
    return render(request, "comp1.html", data)

def about3(request):
    cena = compcena.objects.filter(id_cena=3)
    data = {'cena': cena}
    return render(request, "comp1.html", data)