from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def home(request):
    return render(request, 'accessControl/home.html')

def loginView(request):

    context = {}
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('usr'), password = request.POST.get('pwd'))
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') if request.GET.get('next') else '/')
        else:
            context['error'] = 'Usuario o contraseña incorrectos'
    
    return render(request, 'accessControl/login.html', context)