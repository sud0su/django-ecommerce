from django.contrib import admin
from .models import Orders, OrderStatus, OrderProduct, OrderHistory

admin.site.register([Orders, OrderProduct, OrderStatus, OrderHistory])
