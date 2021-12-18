from django.urls import path
from . import views
import main.views

app_name = 'accounts'
urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('main/', main.views.index, name='index'),
]