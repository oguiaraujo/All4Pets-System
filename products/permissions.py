from rest_framework import permissions

class IsAdminGroupOrReadOnly(permissions.BasePermission):
    """
    Permite:
    1. Acesso de leitura (GET) apenas para Funcionarios ou Administradores.
    2. Acesso de escrita (POST, PATCH, DELETE) apenas para Administradores.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False 
        if request.method in permissions.SAFE_METHODS:
            
            is_employee = user.groups.filter(name='Funcionarios').exists()
            is_admin = user.groups.filter(name='Administrador').exists()
            return is_employee or is_admin or user.is_superuser
        return user.groups.filter(name='Administrador').exists() or user.is_superuser