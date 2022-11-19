from django.db import models
# Create your models here.

class Medico (models.Model):
    id_medico=models.AutoField(primary_key=True)
    nombre_medico=models.TextField
    mp=models.TextField