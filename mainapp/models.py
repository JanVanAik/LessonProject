from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

"""
    Для пользователя crud не требуется -  Abstract user  позволяет работать с ним и так. 
    Единственное, что правим - safe delete

     С продуктами и заказами лучше работать через с помощью CBV, для чего уже нужны формы, напишу, когда до них дойдем
"""


# Create your models here.
class BaseUser(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True)
    adress = models.CharField(max_length=300)

    def safe_delete(self):
        self.is_active = False
        self.save()


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    product_datetime = models.DateTimeField(default=now)

    image = models.ImageField(upload_to='products_image', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    total_price = models.PositiveIntegerField(default=0)
    order_datetime = models.DateTimeField(default=now)
    user_id = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
