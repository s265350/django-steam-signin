from django.shortcuts import redirect
from steamauth import *
from django.contrib.auth import login, logout
from .account import process
from django.conf import settings

USE_SSL = bool(getattr(settings, 'USE_SSL', False))

# Create your views here.
def signin(request): # GET /login
    return auth('/account/callback', use_ssl=USE_SSL)

def callback(request): # GET /process
    steam_uid = get_uid(request.GET)
    user = process(steam_uid)
    if user is None:
        # login failed
        return redirect('/')
    # login success
    login(request, user)
    return redirect('/')

def signout(request): # GET /logout
    logout(request)
    return redirect('/')
