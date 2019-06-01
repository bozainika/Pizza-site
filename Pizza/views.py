from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Pizza, Topping, Order
from django.urls import reverse
# Create your views here.
def menu (request):
    context={
        'pizzas': Pizza.objects.all(),
        'toppings': Topping.objects.all(),
        'orders': Order.objects.all().filter(user=request.user),
    }
    return render(request,"Menu/menu.html",context)

def pizza(request,pizza_id):
    context={
        'pizza': Pizza.objects.get(id=pizza_id),
        'toppings': Topping.objects.all(),
        'orders': Order.objects.all()
        .filter(user=request.user),
    }
    return render(request,"Menu/pizza.html",context)

def order(request):
    if not request.method=='POST':
        return HttpResponseRedirect(reverse('menu'))
    try:
        p=Pizza.objects.get(pk=request.POST['pizza'])
        new = Order(user=request.user,
                    size=request.POST['size'],
                    pizza=p,
        )
        new.save()
        toppings=Topping.objects.all().filter(id__in=request.POST['toppings'])
        new.toppings.set(toppings)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponseRedirect(reverse('menu'))
