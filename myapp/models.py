from django.db import models

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

    def __str__(self):
        return f"{self.title} - {self.proyect}"