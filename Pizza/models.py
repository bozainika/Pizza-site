from django.db import models
from django.contrib.auth.models import User

class Topping(models.Model):
    type=models.CharField(max_length=32)
    def __str__(self):
        return f"{self.type}"

class Dish(models.Model):
    type=models.CharField(max_length=64)
    def __str__(self):
        return self.type

class Pizza(models.Model):
    SMALL="small"
    LARGE="large"
    SIZE_CHOICES=(
        (SMALL, 'small'),
        (LARGE, 'large'),
    )

    size=models.CharField(
                max_length=5,
                choices=SIZE_CHOICES,
                blank=False
    )
    pizza=models.ForeignKey(
                Dish,
                blank=False,
                on_delete=models.CASCADE,
    )
    toppings=models.ManyToManyField(
                    Topping,
                    blank=True,
    )
    def __str__(self):
        toppings=self.toppings.all()
        return f"{self.size} {self.pizza} with {toppings}"

class Order(models.Model):
    STATE=(
        ('pending','pending'),
        ('processed','processed'),
    )
    pizza=models.ForeignKey(
                Pizza,
                blank=False,
                related_name="ordered",
                on_delete=models.CASCADE,
    )
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
    def __str__(self):
        toppings=self.pizza.toppings.all()
        return f"{self.user.pk}: {self.pizza} ({self.status})"

    def process(self):
        try:
            self.status="processed"
        except Exception:
            return 111
        return None
