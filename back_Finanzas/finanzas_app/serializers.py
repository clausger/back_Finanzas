from rest_framework import serializers
from .models import Ingreso, Gasto, IngresoProyectado, Proyecto

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'

class IngresoProyectadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngresoProyectado
        fields = ['anio', 'monto']

class ProyectoSerializer(serializers.ModelSerializer):
    ingresos_proyectados = IngresoProyectadoSerializer(many=True)

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'costo_total', 'duracion', 'ingresos_proyectados', 'roi', 'payback', 'total_ingresos']

    def create(self, validated_data):
        ingresos_data = validated_data.pop('ingresos_proyectados', [])
        proyecto = Proyecto.objects.create(**validated_data)

        for ingreso_data in ingresos_data:
            ingreso = IngresoProyectado.objects.create(**ingreso_data)  # Crea cada IngresoProyectado
            proyecto.ingresos_proyectados.add(ingreso)  # Agrega el ingreso al proyecto

        return proyecto
