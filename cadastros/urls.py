from django.urls import path
from  . import views

urlpatterns = [
    path('clientes/', views.cliente_create_view)
]