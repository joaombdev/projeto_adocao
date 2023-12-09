from django.db import models

# Create your models here.
class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1)
    weight = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    species = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name='pet_breed')
    local = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='pets/', blank=True, null=True) 

    def __str__(self) -> str:
        return self.name


