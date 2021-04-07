from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
# the model for the operation is created here.

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    added_on=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()
    objects=models.Manager()

    def __str__(self):
        return self.name