from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name='menu'),
    path("<int:dish_id>/",views.pizza, name='dish'),
    path("order/", views.order, name='order'),
]
