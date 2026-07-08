
from django.urls import include, path
from journal import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home,name=''),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profle'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('create_thought', views.create_thought, name='create_thought'),
    
]
