from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class FoodType(models.Model):
    type=models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return f"{self.type}"

class Dish(models.Model):
    SMALL="Small"
    LARGE="Large"
    SIZE_CHOICES=(
        (SMALL, 'Small'),
        (LARGE, 'Large'),
    )
    size=models.CharField(
                max_length=5,
                choices=SIZE_CHOICES,
                blank=False
    )
    type=models.ForeignKey(FoodType, blank=False, on_delete=models.CASCADE)
    name=models.CharField(
                max_length=64,
                blank=False,
    )
    toppings=models.CharField(
                max_length=64,
                blank=False
    )
    price=models.FloatField(blank=False)

    def __str__(self):
        return f"{self.size} {self.name} with {self.toppings} - " + "{0:.2f}".format(self.price)
    def get_dish_names(type_name):
        dish_names=[]
        food_type=FoodType.objects.get(type=type_name)
        for dish in Dish.objects.filter(type=food_type).all():
            if not dish.name in dish_names:
                dish_names.append(dish.name)
        return dish_names

class Order(models.Model):
    STATE=(
        ('pending','pending'),
        ('processed','processed'),
    )
    items=models.ForeignKey(Dish, on_delete=models.CASCADE)
    user=models.ForeignKey(
                User,
                blank=False,
                related_name="orders",
                on_delete=models.CASCADE,
    )
    status=models.CharField(
                max_length=10,
                choices=STATE,
                blank=False,
                default="pending",
    )
    time=models.DateTimeField(auto_now_add=True)
    processed_on=models.DateTimeField(null=True,blank=True)
    end_sum=models.FloatField(blank=True, null=True, default=0)
    def __str__(self):
        items=", ".join(self.items.all().values_list('dish', flat=True))
        return f"{self.user}: {items} ({self.status}) - {self.end_sum}"

    def add_item(self, id):
        item=Dish.objects.get(pk=id)
        self.items.add(item)
        self.sum=self.sum + item.price

    def process(self):
        try:
            self.status="processed"
            self.processed_on=datetime.now()
        except Exception:
            return 111
        return None
