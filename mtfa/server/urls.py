from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from .views import sso_server

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.custom_login_view, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]