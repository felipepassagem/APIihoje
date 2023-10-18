from django.db import models

# Create your models here.
from user.models import CustomUser  # Importe o modelo CustomUser se necessário

class Venue(models.Model):
    id_estabelecimento = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    images = models.TextField()  # Para armazenar várias imagens, pode usar um campo TextField
    description = models.TextField()
    tags = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)  # CNPJ é mantido em português

    def __str__(self):
        return self.name
