from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

def default(request):
  return render(request, 'default/login.html')

def contacts(request):
  return render(request, 'default/contacts.html')

def message(request):
  return render(request, 'default/message.html')

def _login(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)

    if form.is_valid():
      login(request, form.get_user())
      return redirect('videos')
  else:
    form = AuthenticationForm()
  return render(request, 'default/login.html', {'form': form})

def _logout(request):
  if request.method == 'POST':
    logout(request)
    return redirect('default')