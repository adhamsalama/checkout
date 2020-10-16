from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
from checkout.models import User

# Create your models here.

class Wishlist(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(validators=[MinValueValidator(0)])
    link = models.CharField(max_length=512, null=True, blank=True)
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")

    def __str__(self):
        return f"{self.name} - {self.user}"