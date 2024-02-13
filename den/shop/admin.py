from django.contrib import admin
from .models import *

@admin.register(photo)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(categories)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(product_information)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(sale)
class PersonAdmin(admin.ModelAdmin):
    pass

#login - danil
#password - 123



