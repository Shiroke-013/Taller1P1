from django.db import models
import uuid

class Temphum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    latitude = models.IntegerField(verbose_name='Latitud')
    length = models.IntegerField(verbose_name='Longitud')
    land  = models.CharField(verbose_name='Terreno', max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# Create your models here.
