from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test 
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Products 
from .serializers import ProductsSerializer
from .permissions import IsAdminGroupOrReadOnly
from .forms import ProductForm

def is_admin_check(user):
    return user.groups.filter(name='Administrador').exists()

class ProductsViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminGroupOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = {
        'preco': ['exact', 'lt', 'gt', 'lte', 'gte'],
        'data_validade': ['exact', 'lt', 'gt'],
        'categoria': ['exact'],
    }

    search_fields = ['nome', 'categoria', 'codigo', 'data_validade']
    ordering_fields = ['preco', 'data_validade', 'nome']
    
    def get_queryset(self):
        queryset = Products.objects.all()

        if self.action == 'list':
            ativo_param = self.request.query_params.get('ativo')
            
            if ativo_param == 'false':
                if is_admin_check(self.request.user):
                    return queryset.filter(ativo=False)
                return queryset.none()
            
            return queryset.filter(ativo=True)
        
        return queryset
    
    def perform_destroy(self, instance):
        instance.ativo = False
        instance.save()

def products_list(request):
    is_admin = request.user.groups.filter(name = 'Administrador').exists()
    produtos = Products.objects.filter(ativo=True)
    context ={
        'produtos': produtos,
        'is_admin': is_admin
    }
    return render(request, 'products/products.html', context)

@login_required
@user_passes_test(is_admin_check)
def products_inactive_list(request):
    context = {
        'is_admin': True
    }
    return render(request, 'products/inactive.html', context)

def products_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list') 
    else:
        form = ProductForm()
    
    return render(request, 'products/create.html', {'form': form})

def products_edit(request, id):
    return render(request, 'products/edit.html', {'id': id})