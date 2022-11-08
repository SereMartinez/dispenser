from django.db import models
from .models import Estado

# Create your models here.
class Tarea(models.Model):
    id_tarea = models.BigAutoField(primary_key=True),
    fecha = models.DateField,
    descripcion = models.TextField,
    # estatus = models.ForeignKey(Estado,on_delete=models.CASCADE),