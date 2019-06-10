from django.contrib import admin

# Register your models here.
from .models import Order, Dish, FoodType

admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(FoodType)
