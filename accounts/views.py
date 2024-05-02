from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):

    if request.method == "POST":
        usuario = request.POST['username']
        senha = request.POST['password']

        verificarUsuario = auth.authenticate(request, username=usuario, password=senha)
        
        if verificarUsuario != None:
            auth.login(request, verificarUsuario)
            return redirect('index')
        else:
            return redirect('login')


        return render(request, 'pages/login.html')


    else:
        return render(request, 'pages/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')