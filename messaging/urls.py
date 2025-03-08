from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileMessengerView, name='profile_messenger_url'),
    path('<int:user_id>', views.profileMessengerView, name='profile_messenger_partner_url'),
]