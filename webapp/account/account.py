from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from steam import Steam

STEAM_API_KEY = getattr(settings, 'STEAM_API_KEY', None)
steam = Steam(STEAM_API_KEY)
User = get_user_model()

def process(steamid):
    if steamid is None:
        # login failed
        return None
    # login success
    user = get_user(steamid)
    user.last_login = models.DateTimeField(timezone.now)
    return user

def get_user(steamid):
        try:
            return User.objects.get(steamid=steamid)
        except User.DoesNotExist:
            return new_user(steamid)

def new_user(steamid):
    player = steam.users.get_user_details(steamid).get('player') # Web API call
    
    user = User.objects.create_user(steamid=steamid, password=None)
    user.communityvisibilitystate = player.get('communityvisibilitystate')
    user.profilestate = player.get('profilestate') # not retrived
    user.personaname = player.get('personaname')
    user.profileurl = player.get('profileurl')
    user.avatar = player.get('avatar')
    user.avatarmedium = player.get('avatarmedium')
    user.avatarfull = player.get('avatarfull')
    user.lastlogoff = player.get('lastlogoff') # not retrived
    user.personastate = player.get('personastate')
    user.commentpermission = player.get('commentpermission') # not retrived

    user.save()

    return user
