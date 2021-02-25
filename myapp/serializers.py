from rest_framework import serializers
from .pet import Pet

class PetSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pet
        fields = ('dono', 'pet', 'idade', 'raca')
