from django.db import models

# Create your models here.


class Amigo(models.Model):
    modelo = models.CharField(max_length=100,default="")
    ano_fabricacao = models.IntegerField(default=2023)
    info = models.TextField("Informações", blank=True)
    whatsapp = models.CharField("Whatsapp", max_length=15, blank=True)
    imagens = models.ImageField("Imagens", upload_to="imagens", blank=True, null=True)

    def __str__(self):
        return self.modelo
