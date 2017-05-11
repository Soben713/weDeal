# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView, View

from mainapp.forms import LoginForm, RegistrationForm
from django.template import RequestContext


def home_view(request):
    return redirect('deals')


class AddDeal(TemplateView):
    template_name = "add_deal.html"


@csrf_exempt
def authentication_view(request):
    template_name = "login.html"
    login_form = LoginForm
    registration_form = RegistrationForm

    if request.method == 'POST':
        login_form = login_form(request.POST, prefix="login")
        register = registration_form(request.POST, prefix="register")

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('auth')

        elif register.is_valid():
            User.objects.create_user(
                username=register.cleaned_data['username'],
                password=register.cleaned_data['password1']
            )
            return redirect('home')
    else:
        context = {}

        login_form = login_form(prefix="login")
        context['login'] = login_form

        register_form = registration_form(prefix="register")
        context['register'] = register_form

        return render(request, template_name, context)


@login_required
def deals_view(request):
    return render(request, 'deals.html', {})


class ItemView(TemplateView):
    template_name = "view_item.html"


def logout_view(request):
    logout(request)
    return redirect('auth')
