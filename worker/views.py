from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from .models import Task
from rest_framework.decorators import api_view
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.decorators import login_required


@api_view(http_method_names=['GET', 'POST'])
def log(request):
    message = ''
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            message = 'Неверный логин или пароль'

    return render(request, 'worker/log.html', {'message': message})

@api_view(http_method_names=['GET', 'POST'])
def sign(request):
    if request.method == 'POST':
        serializer_params = {
            'username': request.data['user'],
            'password': request.data['pass']
        }
        user_serializer = UserSerializer(data=serializer_params)
        if user_serializer.is_valid():
            user_serializer.create()
            return redirect('/login')

    return render(request, 'worker/sign.html', {'message': 'Некорректные данные'})

@login_required(login_url='/login')
@api_view(http_method_names=['GET'])
def index(request):
    task_serializer = TaskSerializer(Task.objects.filter(user=request.user), many=True)
    return render(request, 'worker/index.html', {'tasks': task_serializer.data})

@login_required(login_url='/login')
@api_view(http_method_names=['POST'])
def add(request):
    print('tit')
    serializer_params = {
        'name': request.data['name'],
        'link': request.data['link'],
        'user': request.user.id
    }
    serializer = TaskSerializer(data=serializer_params)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)

    return redirect('/')

def out(request):
    logout(request)
    return redirect('/')
