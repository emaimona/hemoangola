"""hemoangola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from client.views import home, find, about, regist, v404, login_user, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('about/', about, name='url_about'),
    path('find/', find, name='url_find'),
    path('regist/', regist, name='url_regist'),
    path('404/', v404, name='url_v404'),
    path('login/', login_user, name='url_login'),
    path('login/', logout_user, name='url_logout'),
]
