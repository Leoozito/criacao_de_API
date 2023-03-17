from rest_framework import serializers
from estacionamento.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','placa','nome','rg']