from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet
from services.views import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register('services', ServiceViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('api/', include(router.urls)),
    path('services/', include('services.urls')),
    path('api/', include(router.urls)),
]