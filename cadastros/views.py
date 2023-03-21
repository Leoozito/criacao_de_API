from django.shortcuts import render
from rest_framework import viewsets, generics
from cadastros.models import Cliente
from cadastros.serializer import ClienteSerializer
from django.http import JsonResponse

class ClienteViewSet(viewsets.ModelViewSet):
    """exibindo todos clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteCreateAPIView(generics.CreateAPIView):
    """exibindo todos clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
cliente_create_view = ClienteCreateAPIView.as_view()