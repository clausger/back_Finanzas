from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BalanceViewSet, IngresoViewSet, GastoViewSet, InversionViewSet, ProyectoViewSet, ResumenFinancieroCompletoView

router = DefaultRouter()
router.register(r'balance', BalanceViewSet)
router.register(r'inversiones', InversionViewSet)
router.register(r'ingresos', IngresoViewSet)
router.register(r'gastos', GastoViewSet)
router.register(r'proyectos',ProyectoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('resumen/', ResumenFinancieroCompletoView.as_view(), name='resumen-financiero-completo'),
]
