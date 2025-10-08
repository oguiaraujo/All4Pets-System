from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    filds = ('email','first_name','last_name','cpf','telefone','role')

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    filds = ('email','first_name','last_name','cpf','telefone','role', 'isactive')