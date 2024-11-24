from rest_framework import viewsets
from .models import Ingreso, Gasto, Proyecto
from .serializers import IngresoSerializer, GastoSerializer, ProyectoSerializer
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response 
from django.http import JsonResponse

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

La suma de 'Costo Total' de todos los proyectos.
La suma de todos los ingresos.
La suma de todos los gastos.
"""


    def get(self, request, format=None):
        total_costo_proyectos = Proyecto.objects.aggregate(Sum('costo_total'))['costo_total__sum'] or 0

        total_ingresos = Ingreso.objects.aggregate(Sum('amount'))['amountsum'] or 0

        total_gastos = Gasto.objects.aggregate(Sum('amount'))['amountsum'] or 0

        balance = total_ingresos - total_gastos

        return Response({
            'total_costo_proyectos': total_costo_proyectos,
            'total_ingresos_recurrentes': total_ingresos,
            'total_gastos_recurrentes': total_gastos,
            'total_balance': balance,
        })

def ping(request):
    return JsonResponse({'message': 'Pong'})