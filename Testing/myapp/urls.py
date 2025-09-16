from django.urls import path, include
from . import views


# URL configuration for the myapp application

urlpatterns = [
    # API routes
 
    
    # Web routes
    path('', views.home, name='home'),
    path('todos/', views.todo, name='todo'),
    path('signup/', views.authView, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('username-recovery/', views.username_recovery, name='username_recovery'),
    path('profile/', views.profile_view, name='profile'),
    
    
]

