from django.db import models


# Create your models here.
class Semestre(models.Model):
    codigo = models.CharField(max_length=5)
    descricao = models.CharField(max_length=25)

    def __str__(self):
        return self.descricao
