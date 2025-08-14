from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('captcha/', include('captcha.urls'))
]
