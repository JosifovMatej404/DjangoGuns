from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    brand = models.CharField(max_length=100, default="Someones Guns")

    def __str__(self):
        return self.brand

class Gun(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    price = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    year_built = models.IntegerField()

    def is_old_timer(self):
        return self.year_built < 1940

    def __str__(self):
        return self.name
