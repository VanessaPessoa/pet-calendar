from django.db import models
import uuid

class Pet(models.Model):

    class Meta:

        db_table = 'pet'

    pet = models.CharField(max_length=200)
    dono = models.CharField(max_length=200)
    raca = models.CharField(max_length = 200)
    idade = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    