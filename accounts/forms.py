from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    filds = ('email','first_name','last_name','cpf','telefone','role')

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    filds = ('email','first_name','last_name','cpf','telefone','role','isactive')

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    filds = ('email','first_name','last_name','cpf','telefone','password1','password2')
    
  def save(self, commit = True):
    user = super().save(commit = False)
    user_role = User.Roles.CLIENT
    user.is_staff = False
    if commit:
      user.save()
    return user 