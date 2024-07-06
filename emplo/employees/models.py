from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey('Position', related_name='employees', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
