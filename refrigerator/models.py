from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    
    def __str__(self):
        return self.name
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    memo = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title