from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet
from products.views import ProductsViewSet

from services.views import ServiceViewSet
from pets.views import PetViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'products', ProductsViewSet, basename='product')
router.register(r'pets', PetViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    #path("products/", include("products.urls")),
    path('api/', include(router.urls)),
]
