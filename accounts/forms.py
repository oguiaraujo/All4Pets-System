from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    filds = ('email','first_name','last_name','cpf','telefone','role')