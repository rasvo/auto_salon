from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=202)
    country = models.CharField(max_length=202)
    founded_year = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to='brand/image/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f" nomi -> {self.name}"

class Car(models.Model):
    name = models.CharField(max_length=202)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.CharField(max_length=101)
    year = models.IntegerField(default=2020)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    probeg = models.IntegerField(default=0)
    image = models.ImageField(upload_to='car/image/', null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f" nomi -> {self.name}"


