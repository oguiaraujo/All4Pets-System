from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('create/', views.products_create, name='products_create'),
    path('edit/<int:id>/', views.products_edit, name='products_edit'),
    path('inactive/', views.products_inactive_list, name='products_inactive_list'),
]
