from django.db import models

# Create your models here.
class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5000)
    
    def __str__(self):
        return f'{self.category}'
    