from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import JsonResponse

def log(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        if user and user.is_active == True:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'worker/log.html', {'message': 'Неверный логин или пароль'})

    return render(request, 'worker/log.html')


def sign(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(username=request.POST['user'], password=request.POST['pass'])
            user.save()
        except:
            pass

        return redirect('/')

    return render(request, 'worker/sign.html')

def index(request):
    if '_auth_user_id' not in request.session.keys():
        return redirect('/login')

    return render(request, 'worker/index.html')


def out(request):
    logout(request)
    return redirect('/')


