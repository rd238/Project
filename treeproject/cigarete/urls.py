from cigarete.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', firstpage, name='home'),
    path('register/', RegisterUser.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='log'),
    path('sigaretes/', index, name='sig')
]
