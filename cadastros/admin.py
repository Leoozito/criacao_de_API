from django.contrib import admin
from cadastros.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'placa')
    list_display_links = ('id', 'placa')
    search_fields = ('placa',)
    
admin.site.register(Cliente, Clientes)