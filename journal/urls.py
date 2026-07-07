
from django.urls import include, path
from journal import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home,name=''),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout_user', views.logout_users, name='logout_user'),
    
]
