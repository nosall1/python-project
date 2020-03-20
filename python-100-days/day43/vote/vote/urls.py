"""vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vote1 import views

urlpatterns = [
    path('',views.show_subjects),
    path('admin/', admin.site.urls),
    path('teachers/',views.show_teachers),
    path('praise/',views.prise_or_criticize),
    path('criticize/',views.prise_or_criticize),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('captcha/',views.get_captcha,name='get_captcha')
]
