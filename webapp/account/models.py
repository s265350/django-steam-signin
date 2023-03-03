from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class SteamUserManager(BaseUserManager):
    def _create_user(self, steamid, password, **extra_fields):
        """
        Creates and saves a User with the given steamid and password.
        """
        try:
            # python social auth provides an empty email param, which cannot be used here
            del extra_fields['email']
        except KeyError:
            pass
        if not steamid:
            raise ValueError('The given steamid must be set')
        user = self.model(steamid=steamid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, steamid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(steamid, password, **extra_fields)

    def create_superuser(self, steamid, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(steamid, password, **extra_fields)

class SteamUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'steamid'
    REQUIRED_FIELDS = []

    # Public data
    steamid = models.CharField(_('Steam ID'), max_length=17, unique=True)
    communityvisibilitystate = models.IntegerField(_('Visibility'), choices=[(i, i) for i in range(1, 6)], default=1) # 1 - Private, 2 - Friends only, 3 - Friends of Friends, 4 - Users Only, 5 - Public
    profilestate = models.BooleanField(_('Profile completed'), default=False, null=True) # not retrived
    personaname = models.CharField(_('Name'), max_length=255, default='')
    profileurl = models.CharField(_('URL'), max_length=300, default='')
    avatar = models.CharField(_('Avatar'), max_length=255, default='')
    avatarmedium = models.CharField(_('Avatar medium'), max_length=255, default='')
    avatarfull = models.CharField(_('Avatar full'), max_length=255, default='')
    lastlogoff = models.DateTimeField(_('Last log off'), default=timezone.now, null=True) # UNIX timestamp # not retrived
    personastate = models.IntegerField(_('Persona State'), choices=[(i, i) for i in range(7)], default=1) # 0 - Offline, 1 - Online, 2 - Busy, 3 - Away, 4 - Snooze, 5 - Looking to trade, 6 - Looking to play
    commentpermission = models.BooleanField(_('Comment permission'), default=False, null=True) # not retrived

    # Private data
    # realname = models.CharField(max_length=255, default='')
    # primaryclanid = models.CharField(max_length=255, default='') # player's primary group, as configured in their Steam Community profile
    # timecreated = models.DateTimeField(default=timezone.now) # UNIX timestamp
    # loccountrycode = models.CharField(max_length=2, default='') # (if set) user's country of residence, 2-character ISO country code
    # locstatecode = models.CharField(max_length=2, default='') # (if set) user's state of residence
    # loccityid = models.CharField(max_length=2, default='') # (if set) internal code indicating the user's city of residence (a future update will provide this data in a more useful way)

    # Add the other fields that can be retrieved from the Web-API if required

    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('Last login'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = SteamUserManager()

    def __str__(self):
        return self.steamid+' - '+self.personaname

    def get_short_name(self):
        return self.personaname

    def get_full_name(self):
        return self.personaname
