from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sso/login/', views.custom_login_view, name='server_login'),
]