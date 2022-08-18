from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def registration_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.password = make_password(data.password)
            data.save()
            return redirect('index')
    request.title = 'Registration'
    return render(request, 'registration.html', context={
        'form': form
    })
