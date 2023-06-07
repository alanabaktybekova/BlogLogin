from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout



def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



def login_system(request):
    form = CustomAuthLoginForm()
    if request.method == 'POST':
        print('post')
        form = CustomAuthLoginForm(data=request.POST)
        if form.is_valid():
            print('valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            print('login')
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'login.html', {'form': form})

def logout_system(request):
    logout(request)
    return redirect('/')


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'register.html', {'form': form})


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'create_post.html', {'form': form})


def my_posts(request):
    profile = request.user
    posts = Post.objects.filter(user=request.user)
    return render(request, 'my_posts.html', {'profile': profile, 'posts': posts})


def profile_detail(request, id):
    profile = User.objects.get(id=id)
    posts = Post.objects.filter(user__id=id)
    return render(request, 'my_posts.html', {'profile': profile, 'posts': posts})


def like_post(request, id):
    post = Post.objects.get(id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/')
