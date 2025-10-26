from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Service
from .serializers import ServiceSerializer
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = 'services/list.html'
    context_object_name = 'services'

    def get_queryset(self):
        queryset = Service.objects.filter(status=True)

        search = self.request.GET.get('search')   # filtro de busca
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search | Q(description__icontais=search))
            )

        return queryset


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

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
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)