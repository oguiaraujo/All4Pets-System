from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = User
  list_display = ('email','first_name','role','is_staff','is_active')
  list_filter = ('role','is_staff','is_active')
  fieldsets = (
      (None, {'fields': ('email','password')}),
      ('Informações pessoais', {'fields': ('first_name','last_name','cpf','telefone','cargo')}),
      ('Permissões', {'fields': ('is_active','is_staff','is_superuser','groups')}),
      ('Datas', {'fields': ('last_login','date_joined')})
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email','first_name','password1','password2','role','is_staff','is_active')
      }),
  )
  search_fields = ('email','first_name','cpf')
  ordering = ('email',)

admin.site.register(User, CustomUserAdmin)