from rest_framework import serializers
from .models import Ingreso, Gasto, FuenteFinanciacion, IngresoProyectado, Proyecto

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'

class FuenteFinanciacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteFinanciacion
        fields = ['tipo', 'monto', 'tasa_interes', 'plazo']

class IngresoProyectadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngresoProyectado
        fields = ['anio', 'monto']

class ProyectoSerializer(serializers.ModelSerializer):
    fuentes_financiacion = FuenteFinanciacionSerializer(many=True)
    ingresos_proyectados = IngresoProyectadoSerializer(many=True)

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'costo_total', 'duracion', 'fecha_inicio', 'fuentes_financiacion', 'ingresos_proyectados']

    def create(self, validated_data):
        fuentes_data = validated_data.pop('fuentes_financiacion')
        ingresos_data = validated_data.pop('ingresos_proyectados')
        proyecto = Proyecto.objects.create(**validated_data)

        for fuente_data in fuentes_data:
            FuenteFinanciacion.objects.create(proyecto=proyecto, **fuente_data)

        for ingreso_data in ingresos_data:
            IngresoProyectado.objects.create(proyecto=proyecto, **ingreso_data)

        return proyecto