from django.db import models


# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Pet(models.Model):
    dono = models.ForeignKey("User", on_delete=models.CASCADE, related_name='pets')
    data_nascimento = models.DateField(null=False, blank=False)
    tipo_pet = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.user.nome


class Vacina(models.Model):
    vacina = models.CharField(max_length=100, unique=True)
    duas_doses = models.BooleanField(default=False)
    tempo_segunda_dose = models.IntegerField()
    tempo_renovacao = models.IntegerField()

    def __str__(self):
        return self.vacina


class VacinaPet(models.Model):
    vacina = models.ForeignKey("Vacina", on_delete=models.CASCADE, related_name='vacinas')
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name='pets')
    data_dose = models.DateField(null=False, blank=False)
