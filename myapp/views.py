from rest_framework import generics
from .pet import Pet
from .serializers import PetSerializer

# Create your views here.
class PetList(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer