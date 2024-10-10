from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Ingreso, Gasto, Proyecto
from .serializers import IngresoSerializer, GastoSerializer, UserSerializer, ProyectoSerializer
from django.shortcuts import render
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class IngresoListCreate(generics.ListCreateAPIView):
    serializer_class = IngresoSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Ingreso.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors) 
    
    
class GastoListCreate(generics.ListCreateAPIView):
    serializer_class = GastoSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Gasto.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors) 

class ProyectoListCreate(generics.ListCreateAPIView):
    serializer_class = ProyectoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Proyecto.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# class IngresoViewSet(viewsets.ModelViewSet):
#     queryset = Ingreso.objects.all()
#     serializer_class = IngresoSerializer

# class GastoViewSet(viewsets.ModelViewSet):
#     queryset = Gasto.objects.all()
#     serializer_class = GastoSerializer
