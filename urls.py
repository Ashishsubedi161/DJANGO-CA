# myapp/urls.py
from django.urls import path
from .views import logout

from . import views

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
     path('logout/', logout, name='logout'),
    path('main/', views.main_view, name='main'),
    path('profile/', views.profile, name='profile'),
  
]
