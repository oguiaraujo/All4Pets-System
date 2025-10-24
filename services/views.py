from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Service
from .serializers import ServiceSerializer

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Service.objects.all()
        else:
            return Service.objects.filter(status=True)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]