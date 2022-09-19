from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
            form.add_error('password', 'Username yoki parol noto\'g\'ri')
    request.title = 'Login'
    return render(request, 'login.html', context={
        'form': form
    })


def registration_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.password = make_password(data.password)
            data.save()
            return redirect('login')
    request.title = 'Registration'
    return render(request, 'registration.html', context={
        'form': form
    })
