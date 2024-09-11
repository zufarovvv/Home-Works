from django.db import models

# Create your models here.


class IceCream(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

class Child(models.Model):
    name = models.CharField(max_length=255)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)

class Parrent(models.Model):
    name = models.CharField(max_length=255)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)