from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SignUpView

urlpatterns = [
    path('login/', CustomLoginView, name='login'),
    path('logout/', CustomLogoutView, name='logout'),
    path('signup/', SignUpView, name='signup'),
]
