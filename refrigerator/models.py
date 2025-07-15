from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    complete = models.IntegerField(verbose_name="完了フラグ",default=0)
    
    def __str__(self):
        return self.name