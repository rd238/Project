from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cigarete.forms import RegisterUserViev, LoginUserViev
from cigarete.models import Cigarete


# Create your views here.

def index(request):
    return render(request, 'cigarete/index.html', {'title': 'Сигареты', 'res': Cigarete.objects.all()})


def firstpage(request):
    return render(request, 'cigarete/reglog.html')


class RegisterUser(CreateView):
    form_class = RegisterUserViev
    template_name = 'cigarete/register.html'
    success_url = reverse_lazy('log')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('sig')


class LoginUser(LoginView):
    form_class = LoginUserViev
    template_name = 'cigarete/login.html'

    def get_success_url(self):
        return reverse_lazy('sig')
