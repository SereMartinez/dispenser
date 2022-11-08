from django.db import models
# from .models import Tarea

# Create your models here.
class Estado(models.Model):
    id_estado= models.BigAutoField(primary_key=True),
    nombre= models.CharField(max_length= 150),
    def __str__(self):
        return self.nombre

