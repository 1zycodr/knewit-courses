from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UserRegisterForm


def index(request):
    context = {
        'courses' : Course.objects.filter(is_active=True)
    }

    if request.user.is_authenticated:
        try:
            should_pass_test = not request.user.profile.passed_test
        except User.profile.RelatedObjectDoesNotExist:
            should_pass_test = True

        context['should_pass_test'] = should_pass_test

    return render(request, 'index.html', context)


def courses(request):
    return render(request, 'courses.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Неверное имя пользователя или пароль')
                return render(request, 'login.html')

        return render(request, 'login.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Аккаунт {username} был создан!')
                return redirect('login')

        context = {
            "form" : form
        }

        return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def ajax_test_result(request):
    username = request.GET.get('username', None)
    test_result = request.GET.get('test_result', None)

    if username and test_result:
        user = User.objects.get(username=username)

        try:
            user.profile.passed_test = True
        except User.profile.RelatedObjectDoesNotExist:
            user.profile = Profile.objects.create(user=user)
            user.profile.passed_test = True
        finally:
            user.profile.test_result = test_result
            user.profile.save()

    else:
        return JsonResponse({"is_saved": False, "detail": "username and test_result fields are required"}, safe=False)
    return JsonResponse({"is_saved": True}, safe=False)