from cadastros.views import cliente_create_view, ClienteViewSet
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/clientes/', include('cadastros.urls'))
]
