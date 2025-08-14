# sso_client/client_login/views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from pathlib import Path
from simple_sso.sso_client.client import Client

@login_required
def home(request):
    return render(request, "home.html")


def custom_login_view(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('home')
    next_url = request.GET.get('next') or '/'
    # Redirect to SSO server login
    login_url = f"http://127.0.0.1:8000/sso/login/?next={next_url}"
    return redirect(login_url)

    