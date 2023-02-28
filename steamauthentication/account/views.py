from django.shortcuts import redirect
from steamauth import *
from django.contrib.auth import login, logout
from .account import process

# Create your views here.
def signin(request): # GET /login
    #return auth('/accounts/callback') # if does support ssl
    return auth('/account/callback', use_ssl=False) # if does not support ssl

def signout(request): # GET /logout
    logout(request)
    return redirect('/')

def callback(request): # GET /process
    steam_uid = get_uid(request.GET)
    user = process(steam_uid)
    if user is None:
        # login failed
        return redirect('/')
    # login success
    login(request, user)
    return redirect('/')
