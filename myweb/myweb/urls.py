"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('Tgoods/',views.Tgoods, name="Tgoods"),    
    path('Tdaily/',views.Tdaily,name="Tdaily"),
    path('Ttransfer/',views.Ttransfer,name="Ttransfer"),
    path('Tclient/',views.Tclient,name='Tclient'),
    path('logout/',views.logout),
    path('regist/',views.regist,name='regist'),
    path('searchGoods/',views.searchGoods,name="searchGoods"),
    path('searchDaily/',views.searchDaily,name="searchDaily"),
    path('searchClient/',views.searchClient,name="searchClient"),
    path('searchTransfer/',views.searchTransfer,name="searchTransfer"),
]


