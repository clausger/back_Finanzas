from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import IngresoViewSet, GastoViewSet
from . import views

# router = DefaultRouter()
# router.register(r'ingresos', IngresoViewSet)
# router.register(r'gastos', GastoViewSet)

urlpatterns = [
    path('ingresos/', views.IngresoListCreate.as_view(), name="ingreso-list"),
    path("gastos/", views.GastoListCreate.as_view(), name="gastos-list"),
    path("proyectos/", views.ProyectoListCreate.as_view(), name="proyectos-list")
]
