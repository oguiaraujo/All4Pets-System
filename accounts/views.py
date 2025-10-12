from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
  next_page = reverse_lazy('login')

class SignUpView(View):
  def get(self, request):
    form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form' : form})
  
  def post(self, request):
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('login')
    return render(request, 'accounts/signup.html', {'form' : form})