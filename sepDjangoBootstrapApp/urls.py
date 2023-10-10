"""
URL configuration for sepDjangoBootstrapApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views as osmeen_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', osmeen_views.home, name='nyumbani'),
    path('about/', osmeen_views.about, name='kuhusu'),
    path('gallery/', osmeen_views.gallery, name='mapicha'),
    path('Register/', osmeen_views.Register, name='jisajili'),
    path('login/', osmeen_views.login, name='ingia'),

]
