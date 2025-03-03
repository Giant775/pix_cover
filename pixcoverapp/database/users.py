# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.crypto import get_random_string

# # Create your models here.
# class Users(AbstractUser):
#     id =  models.AutoField(primary_key=True)
#     fullname = models.CharField(max_length=20, default = 'Joe Ordan')
#     username = models.CharField(max_length=20, default=get_random_string(length=50), unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=20, default='12345678')
#     age = models.IntegerField(default=30)
#     gender = models.IntegerField(default=0) # 0 - male, 1- female, 2- middle
#     type = models.IntegerField(default = 0)  # 0 - freelancer, 1 - client
#     location1 = models.CharField(max_length=50, default="United States of America")
#     location2 = models.CharField(max_length=50 , default =  "Texas")
#     location3 = models.CharField(max_length=50, default= "Hoston")
#     location4 = models.CharField(max_length=50, default="2956 Brooke Street")
#     skills = models.JSONField(default="[]")
#     category = models.IntegerField(default=0)
#     description = models.CharField(max_length=5000, default="I am an organised, efficient and hard working person, and am willing to discover and accept new ideas which can be put into practice effectively. I am a good listener and learner, able to communicate well with a group and on an individual level. I am able to motivate and direct my talents and skills to meet objectives.")
#     followers = models.JSONField(default="[]")
#     following = models.JSONField(default="[]")
#     avatar = models.ImageField(upload_to='avatar/', default='avatar/sample.jpg')
#     cover = models.ImageField(upload_to='photo/')
#     def __str__(self):
#         return f'{self.fullname}'
#     class Meta:
#         swappable = 'AUTH_USER_MODEL'

# Users._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
# Users._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'