from rest_framework import serializers
from .models import Empresa, Videojuego

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = '__all__'
