from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name='menu'),
    path("<int:pizza_id>/",views.pizza, name='pizza'),
    path("order/", views.order, name='order'),
]
