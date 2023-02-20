from django.db import models
from django.contrib.auth.models import User

class Topping(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping)
    image = models.ImageField(upload_to='pizza_pics', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

Size = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, choices=Size, default="M")
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.user.username} ordered {self.pizza.name}"
class Sales(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    surname=models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=32)
    address=models.CharField(max_length=32)
    quantity = models.IntegerField(default=1)
    price=models.DecimalField(
     max_digits=7,
     decimal_places=2
    )
    
    def __str__(self):
        return f"{self.name} ordered {self.surname}"    






