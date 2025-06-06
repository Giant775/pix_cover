# Generated by Django 5.1 on 2025-03-02 18:09

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(default='Joe Ordan', max_length=20)),
                ('username', models.CharField(default='Ydzg6gmYfWzDwmkjmX41drZqBqQIANsxQxdD5AopoMNvyXH1QB', max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default='12345678', max_length=20)),
                ('age', models.IntegerField(default=30)),
                ('gender', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('location1', models.CharField(default='United States of America', max_length=50)),
                ('location2', models.CharField(default='Texas', max_length=50)),
                ('location3', models.CharField(default='Hoston', max_length=50)),
                ('location4', models.CharField(default='2956 Brooke Street', max_length=50)),
                ('skills', models.JSONField(default=list)),
                ('category', models.IntegerField(default=0)),
                ('description', models.CharField(default='I am an organised, efficient and hard working person, and am willing to discover and accept new ideas which can be put into practice effectively. I am a good listener and learner, able to communicate well with a group and on an individual level. I am able to motivate and direct my talents and skills to meet objectives.', max_length=5000)),
                ('followers', models.JSONField(default=list)),
                ('following', models.JSONField(default=list)),
                ('avatar', models.ImageField(default='avatar/sample.jpg', upload_to='avatar/')),
                ('cover', models.ImageField(upload_to='photo/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
