from django.shortcuts import render
from rest_framework import viewsets
from estacionamento.models import Cliente
from estacionamento.serializer import ClienteSerializer
from django.http import JsonResponse
class ClienteViewSet(viewsets.ModelViewSet):
    """exibindo todos clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer