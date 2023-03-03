# Generated by Django 4.1.7 on 2023-03-03 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteamUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('steamid', models.CharField(max_length=17, unique=True, verbose_name='Steam ID')),
                ('communityvisibilitystate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, verbose_name='Visibility')),
                ('profilestate', models.BooleanField(default=False, null=True, verbose_name='Profile completed')),
                ('personaname', models.CharField(default='', max_length=255, verbose_name='Name')),
                ('profileurl', models.CharField(default='', max_length=300, verbose_name='URL')),
                ('avatar', models.CharField(default='', max_length=255, verbose_name='Avatar')),
                ('avatarmedium', models.CharField(default='', max_length=255, verbose_name='Avatar medium')),
                ('avatarfull', models.CharField(default='', max_length=255, verbose_name='Avatar full')),
                ('lastlogoff', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Last log off')),
                ('personastate', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1, verbose_name='Persona State')),
                ('commentpermission', models.BooleanField(default=False, null=True, verbose_name='Comment permission')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
