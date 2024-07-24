from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15,null=True,blank=True,default="")
    email = models.EmailField(null=True,blank=True,default="")
    resumo = models.TextField(null=True,blank=True,default="")

    def __str__(self):
        return self.nome