from django.contrib import admin

# Register your models here.
from .models import Pizza, Order, Topping, Dish

admin.site.register(Dish)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Order)
