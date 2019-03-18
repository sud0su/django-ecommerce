from django.contrib import admin
from .models import Carrier
# Register your models here.

class CarriersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','delivery_text']
    # list_filter = ('name', 'price')

admin.site.register(Carrier, CarriersAdmin)