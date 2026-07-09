
from django.urls import include, path
from journal import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home,name=''),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile_management, name='profile'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('create_thought', views.create_thought, name='create_thought'),
    path('my-thoughts', views.my_thoughts, name='my-thoughts'),
    path('delete_thought', views.delete_thought, name='delete_thought'),
    path('view_thought/<int:id>', views.view_thought, name='view_thought'),
]
