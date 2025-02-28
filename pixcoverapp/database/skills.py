from django.db import models

# Create your models here.
class Skills(models.Model):
    id = models.IntegerField(primary_key=True)
    skill = models.CharField(max_length=5000)
    
    def __str__(self):
        return f'{self.skill}'
    