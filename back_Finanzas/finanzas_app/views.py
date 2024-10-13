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

class ResumenFinancieroCompletoView(APIView):
    """
    API personalizada que devuelve:
    1. La suma de 'Costo Total' de todos los proyectos.
    2. La suma de todos los ingresos con 'tipo_ingreso == Recurrente'.
    3. La suma de todos los gastos con 'type == Recurrente'.
    """
    
    def get(self, request, format=None):
        # 1. Suma del costo total en todos los proyectos
        total_costo_proyectos = Proyecto.objects.aggregate(Sum('costo_total'))['costo_total__sum'] or 0
        
        # 2. Suma de todos los ingresos donde 'tipo_ingreso' es Recurrente
        total_ingresos_recurrentes = Ingreso.objects.filter(tipo_ingreso="Recurrente").aggregate(Sum('amount'))['amount__sum'] or 0
        
        # 3. Suma de todos los gastos donde 'type' es Recurrente
        total_gastos_recurrentes = Gasto.objects.filter(type="Recurrente").aggregate(Sum('amount'))['amount__sum'] or 0
        
        return Response({
            'total_costo_proyectos': total_costo_proyectos,
            'total_ingresos_recurrentes': total_ingresos_recurrentes,
            'total_gastos_recurrentes': total_gastos_recurrentes,
        })