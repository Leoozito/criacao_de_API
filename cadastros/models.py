from django.db import models

class Cliente(models.Model):
    placa = models.CharField(max_length=8, unique=True, null=True)
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.placa