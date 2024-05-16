from django.db import models

# Create your models here.
class Plant(models.Model):
    name=models.CharField(max_length=30)
    species=models.CharField(max_length=50)
    price=models.IntegerField()
    def __str__(self):
        return self.name