from django.contrib import admin

from payment.models import ShippingAddress, OrderItem, Order

# Register your models here.

admin.site.register(ShippingAddress)

admin.site.register(OrderItem)

admin.site.register(Order)
