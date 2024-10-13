from rest_framework import viewsets
from .models import Ingreso, Gasto, Proyecto
from .serializers import IngresoSerializer, GastoSerializer, ProyectoSerializer
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response 

class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

# Vista personalizada para obtener las sumas de ingresos y gastos
class ResumenFinancieroView(APIView):
    """
    API personalizada que devuelve la suma total de ingresos y gastos.
    """
    def get(self, request, format=None):
        total_ingresos = Ingreso.objects.aggregate(Sum('monto'))['monto__sum'] or 0
        total_gastos = Gasto.objects.aggregate(Sum('monto'))['monto__sum'] or 0
        return Response({
            'ingresos': total_ingresos,
            'gastos': total_gastos,
        })