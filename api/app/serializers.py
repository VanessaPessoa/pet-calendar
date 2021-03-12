from rest_framework import serializers
from .models import User, Pet, Vacina, VacinaPet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'telefone']

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'dono', 'nome', 'data_nascimento', 'tipoPet']

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ['id', 'vacina', 'duas_doses', 'tempo_segunda_dose', 'tempo_renovacao']

