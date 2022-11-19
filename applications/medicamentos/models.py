from django.db import models

# Create your models here.

id_medicamentos= models.AutoField(primary_key=True)
nombre_medicamentos=models.TextField
unidad= models.DecimalField