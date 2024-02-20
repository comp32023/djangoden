from django.contrib import admin
from .models import *

@admin.register(categories)
class PersonAdmin(admin.ModelAdmin):
    pass
#
@admin.register(productinformation)
class PersonAdmin(admin.ModelAdmin):
    pass
