from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _

# Create your models here.
class Carrier(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=13, decimal_places=2, blank=True, null=True)
    delivery_text = models.CharField(_("Delivery Text"), max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='uploads/carriers/logo/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "carriers"
    
# @admin.register(Carriers)
# class CarriersAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price','delivery_text']