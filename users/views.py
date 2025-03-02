from django.shortcuts import redirect, render
from pixcoverapp.database import Users
from pixcoverapp.database import Categories
from pixcoverapp.database import Skills
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from django_countries.data import COUNTRIES

import json
from .models import Users

def signinView(request):
    template_name = 'pixcoverapp/signin.html'

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        message = ''
        if email is None or len(email) == 0:
            message = VALIDATIONERROR_EMPTY_FIELD
        
        exist = Users.objects.filter(email=email).values()
        if len(exist) < 1:
            message = EMAIL_NOT_EXIST
        else:
            user1 = authenticate(request, username=exist[0]['username'], password=password)
            if user1 is not None:
                login(request, user1, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('settings_url')
            else:
                message = EMAIL_PASSWORD_INCORRECT
                return render(request, template_name, {'error': 1, 'message': message})
        
        if message != '':
            return render(request, template_name, {'error': 1, 'message': message})
        
    return render(request, template_name, {})

def signupView(request):
    template_name = 'users/signup.html'
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        message = ''
        if password != password1:
            message = VALIDATIONERROR_PASSWORD_MISMATCH
        elif len(email) == 0:
            message = VALIDATIONERROR_EMPTY_FIELD
        elif len(password) < 6:
            message = VALIDATIONERROR_LENGTH

        if message != '':
            return render(request, template_name, {'error': 1, 'message': message})
        else:
            exist = Users.objects.filter(email=email).values()
            if len(exist) > 0:
                message = VALIDATIONERROR_DUPLICATE
                return render(request, template_name, {'error': 1, 'message': message})
            else:
                usr = Users(email=email, password=password, username=get_random_string(length=50))
                usr.save()
                user = Users.objects.get(email=email)
                user.set_password(password)
                user.save()
                message = REGISTER_SUCCESS
                return render(request, template_name, {'error': 2, 'message': message})
        
    return render(request, template_name, {})

def signoutView(request):
    logout(request)
    return redirect('signin_url')

def settingsView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    
    exist = Users.objects.get(email=request.user.email)
    exist.skills = json.loads(exist.skills)
    categories = Categories.objects.filter().values()
    skills = Skills.objects.filter().values()
    
    template_name = 'users/settings.html'

    countries = []
    for key in COUNTRIES:
        countries.append(COUNTRIES[key])

    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        is_file_upload = request.POST.get("is_file_upload")

        if is_file_upload and int(is_file_upload) == 1: 
            uploaded_file = request.FILES['profile_photo']
            user = Users.objects.get(id=user_id)
            user.avatar = uploaded_file
            user.avatar.name = user_id + "_" + user.avatar.name
            user.save()
            user1 = user 
            user1.skills = json.loads(user1.skills)
            message = SUCCESSFULLY_UPDATED
            return render(request, template_name, {'countries': countries, 'error': 2, 'message': message, 'user': user1, 'categories': categories, 'skills': skills})
        
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        location1 = request.POST.get("location1")
        location2 = request.POST.get("location2")
        location3 = request.POST.get("location3")
        location4 = request.POST.get("location4")

        emailRowsValidate = Users.objects.filter(email=email).values()
        if len(emailRowsValidate) > 0 and str(emailRowsValidate[0]['id']) != str(user_id):
            message = EMAIL_ALREADY_EXIST
            error = 1
            return render(request, template_name, {'countries': countries, 'error': error, 'message': message, 'user': exist, 'categories': categories, 'skills': skills})
            
        user = Users.objects.get(id=user_id)
        user.fullname = fullname
        user.email = email
        user.gender = gender
        user.age = age
        user.phone_number = phone
        user.save()
        message = SUCCESSFULLY_UPDATED
        error = 2

        about = request.POST.get("about")
        user.description = about
        user.location1 = location1
        user.location2 = location2
        user.location3 = location3
        user.location4 = location4
        user.category = request.POST.get("category_id")
        user.skills = []
        for skill in skills:
            checkbox_value = request.POST.get("checkbox_" + skill['skill'])
            if checkbox_value == 'on':
                user.skills.append(skill['id'])
        
        user.skills = json.dumps(user.skills)
        user.save()

        user = Users.objects.get(id=user_id)
        user.skills = json.loads(user.skills)
        return render(request, template_name, {'countries': countries, 'error': error, 'message': message, 'user': user, 'categories': categories, 'skills': skills})

    return render(request, template_name, {'countries': countries, 'user': exist, 'categories': categories, 'skills': skills})