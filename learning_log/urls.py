"""learning_log URL Configuration

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

# 系统admin端的配置
urlpatterns = [
    path('admin/', admin.site.urls), 
]

# 配置learning_logs 的路径
from django.urls import include
urlpatterns += [
    path('learning_logs/', include("learning_logs.urls") ),
    # path('users/', include("users.urls"))
]

# 配置默认跳转到/learning_logs
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/learning_logs/', permanent=True)),
]
