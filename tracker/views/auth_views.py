from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request, next='/'):
    if 'next' in request.GET:
        next = request.GET['next']
    if request.method == 'POST':
        next = request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password == "":
            messages.warning(request, 'your login data are incorrect.')
            return redirect(next)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.warning(request, 'your login data are incorrect.')
        return redirect(next)
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html', {'next': next})


def logout_view(request):
    messages.success(request, 'successfully logout.')
    logout(request)

    response = HttpResponseRedirect('/')
    return response
