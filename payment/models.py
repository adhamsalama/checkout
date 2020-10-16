from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
from checkout.models import User

# Create your models here.

class Payment(models.Model):
    source = models.CharField(max_length=64)
    value = models.FloatField(validators=[MinValueValidator(0)])
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="payments")

    def __str__(self):
        return f"{self.source} - {self.value} - {self.date}"
