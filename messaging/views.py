from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from django.core.files import File
from django_countries.data import COUNTRIES
from django.db.models import Q
from django.db.models import Subquery, OuterRef
import json

from .models import Message
from users.models import Users
from users.models import Categories


def profileMessengerView(request, user_id=None):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    
    logged_in_user = request.user
    
    #Fetch unique chat partners
    chat_partners = Users.objects.filter(
        Q(message_sender__receiver=logged_in_user) | Q(message_receiver__sender=logged_in_user)
    ).distinct()
    # Default chat user (most recent conversation)
    if user_id:
        chat_user = get_object_or_404(Users, id=user_id)
    else:
        last_message = Message.objects.filter(Q(sender=logged_in_user) | Q(receiver=logged_in_user)).order_by('timestamp').first()
        chat_user = last_message.sender if last_message and last_message.sender != logged_in_user else last_message.receiver if last_message else None

    # Fetch messages with the selected chat user
    messages = []
    if chat_user:
        messages = Message.objects.filter(
            Q(sender=logged_in_user, receiver=chat_user) | Q(sender=chat_user, receiver=logged_in_user)
        ).order_by('timestamp')

    # Fetch the most recent message for each chat partner
    last_messages = {
        partner.id: Message.objects.filter(
            Q(sender=logged_in_user, receiver=partner) | Q(sender=partner, receiver=logged_in_user)
        ).order_by('timestamp').first()
        for partner in chat_partners
    }
    
    template_name = 'pixcoverapp/profile-messenger.html'

    context = {
        'logged_in_user': logged_in_user,
        'messages': messages,
        'last_messages': last_messages,
        'chat_user': chat_user if user_id else None,
        'chat_partners': chat_partners
    }
    return render(request, template_name, context)