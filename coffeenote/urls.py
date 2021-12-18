"""coffeenote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
import main.views 
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('main/', main.views.index, name = 'index'),
    path('sign-up/', accounts.views.sign_up, name = 'sign-up'),
    path('login/', accounts.views.login, name = 'login'),
    path('logout/', accounts.views.logout, name = 'logout'),


    #### urls.py 걸열님 시작 ####
    #### urls.py 걸열님 끝 ####

    ### 효수님 시작 ###
    path('MY-COFFEE-NOTE/', main.views.hsp, name = 'hsp'),
    path('COFFEE-NOTE-DETAIL-1/', main.views.coffeenote_datail1, name = 'detail1'),
    ### 효수님 끝 ###

    path('COFFEE-NOTE-DETAIL-2/', main.views.coffeenote_datail2, name = 'detail2'),
    path('COFFEE-NOTE-DETAIL-3/', main.views.coffeenote_datail3, name = 'detail3'),
    
]
