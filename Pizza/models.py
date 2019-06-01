from django.db import models
from django.contrib.auth.models import User

class Topping(models.Model):
    type=models.CharField(max_length=32)
    def __str__(self):
        return f"{self.type}"

class Pizza(models.Model):
    type=models.CharField(max_length=64)
    def __str__(self):
        return self.type

class Order(models.Model):
    SMALL="small"
    LARGE="large"
    SIZE_CHOICES=(
        (SMALL, 'small'),
        (LARGE, 'large'),
    )
    STATE=(
        ('pending','pending'),
        ('processed','processed')
    )
    user=models.ForeignKey(
                User,
                blank=False,
                related_name="orders",
                on_delete=models.CASCADE
    )
    size=models.CharField(
                max_length=5,
                choices=SIZE_CHOICES,
                blank=False
    )
    pizza=models.ForeignKey(
                Pizza,
                blank=False,
                on_delete=models.CASCADE,
    )
    toppings=models.ManyToManyField(
                    Topping,
                    blank=True,
    )
    status=models.CharField(
                max_length=10,
                choices=STATE,
                blank=False,
                default="pending"
    )
    def __str__(self):
        toppings=self.toppings.all()
        return f"{self.user}: {self.size} {self.pizza} with {toppings} ({self.status})"

    def process(self):
        try:
            self.status="processed"
        except Exception:
            return 111
        return None
