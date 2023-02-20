from django.contrib import admin
from .models import Topping, Pizza, Order,Sales


admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Sales)

