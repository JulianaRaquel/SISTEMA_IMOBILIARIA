from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.messages import constants
import re
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
            return redirect('/cadastro')

        if not re.search('[A-Z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
            return redirect('/cadastro')

        if not re.search('[a-z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
            return redirect('/cadastro')

        if not re.search('[1-9]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
            return redirect('/cadastro')

        if len(usuario.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Usuário, e-mail ou senha não podem estar em branco')
            return redirect('/cadastro')

        usuario = User.objects.filter(username=usuario)
        if usuario:
            messages.add_message(request, constants.ERROR, 'Esse usuário já existe')
            return redirect('/cadastro')

        email = User.objects.filter(email=email)
        if email:
            messages.add_message(request, constants.ERROR, 'Esse endereço de e-mail já está cadastrado')
            return redirect('/cadastro')

        try:
            user = User.objects.create_user(username=usuario,
                                            email=email,
                                            password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !!!')
            return redirect('/cadastro')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=usuario, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/login')
        else:
            auth.login(request, usuario)
            return redirect('/home')

def sair(request):
    auth.logout(request)
    return redirect('/login')

def pagina_inicial(request):
    return redirect('/cadastro')
