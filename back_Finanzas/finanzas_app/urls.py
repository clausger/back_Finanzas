from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngresoViewSet, GastoViewSet

router = DefaultRouter()
router.register(r'ingresos', IngresoViewSet)
router.register(r'gastos', GastoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
