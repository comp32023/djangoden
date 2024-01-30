from django.shortcuts import render
from django.http import HttpResponse
# from .models import compcena


def index(request):
    return HttpResponse("<h2>Главная</h2>")

# def vse(request):
#     cena = compcena.objects.filter(id_cena=1)
#     people = compcena.objects.all()
#     data = {'people': people,'cena': cena}
#     return render(request, "comp1.html", data)
#
# def about(request):
#     cena = compcena.objects.filter(id_cena=1)
#     data = {'cena': cena}
#     return render(request, "comp1.html", data)
#
#
# people = compcena.objects.all()
# for person in people:
#     print(f"{person.id_cena} {person.purchase_price} {person.price_for_sale}")



# def about2(request):
#     cena = compcena.objects.filter(id_cena=2)
#     data = {'cena': cena}
#     return render(request, "comp1.html", data)
#
# def about3(request,vse):
#     sv = people
#     cena = compcena.objects.filter(id_cena=3)
#     data = {'cena': cena}
#     return render(request, "comp1.html", data)




# people = compcena.objects.all()
# print(people.query)
# sv = compcena.objects.filter(id_cena = 2)
# print(sv)
# test = people.filter(purchase_price = 2)
# print(test.query)
# tom = people.objects.get(purchase_price = 2)