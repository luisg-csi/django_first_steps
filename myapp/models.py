from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyect(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(auto_now_add=False)
    important= models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
                             

    def __str__(self):
        return f"{self.title} - {self.proyect}"