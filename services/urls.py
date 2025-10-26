from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ServiceListView

router = DefaultRouter()
router.register('services', ServiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', ServiceListView.as_view(), name='service_list'),
]