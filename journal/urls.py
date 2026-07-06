
from django.urls import include, path
from journal import views

urlpatterns = [
    path('home', views.home),
    path('', views.home),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    
]
