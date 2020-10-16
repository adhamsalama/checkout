from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    balance = models.FloatField()

class Category(models.Model):
    name = models.CharField(max_length=64, default="None")
    def __str__(self):
        return self.name.title()

class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    seller = models.CharField(max_length=64, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.name} - {self.user}"



