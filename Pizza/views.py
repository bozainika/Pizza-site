from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Order, Dish, FoodType
from django.urls import reverse
from django.core import serializers
# Create your views here.
def menu (request):
    context={
        'pizza_names': Dish.get_dish_names('Pizza'),
        'salad_names': Dish.get_dish_names('Salad'),
        'Pizzas': Dish.objects.filter(type=FoodType.objects.get(type="Pizza")).all(),
        'Salads':Dish.objects.filter(type=FoodType.objects.get(type="Salad")).all(),
        'orders': Order.objects.all().filter(user=request.user),
    }

    return render(request,"Menu/menu.html",context)

def pizza(request,dish_id):
    context={
        'dish': Dish.objects.get(id=dish_id),
        'orders': Order.objects.all()
        .filter(user=request.user),
    }
    return render(request,"Menu/pizza.html",context)

def order(request):
    if not request.method=='POST':
        return HttpResponseRedirect(reverse('menu'))
    try:
        dish=Dish.objects.get(pk=request.POST['pizza'])
        toppings=Topping.objects.all().filter(id__in=request.POST['toppings'])
        serialized_toppings=serializers.serialize('json', [toppings])
        new = Pizza(user=request.user,
                    size=request.POST['size'],
                    pizza=dish,
                    toppings=serialized_toppings,
        )
    except Exception as e:
        return HttpResponse(e)
    return HttpResponseRedirect(reverse('menu'))
