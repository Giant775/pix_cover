from django.shortcuts import redirect, render, get_object_or_404
# from pixcoverapp.database import Users
from .models import Users
# from pixcoverapp.database import Categories
from .models import Categories
# from pixcoverapp.database import Skills
from .models import Skills
from .models import Review
from .forms import ReviewForm
from .forms import OrderForm
from .constants import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django_countries.data import COUNTRIES
from django.db.models import Q

import json

def signinView(request):
    template_name = 'pixcoverapp/signin.html'

    if request.method == 'POST':
        email = request.POST.get("email")
        password= request.POST.get("password")
        message = ''
        if email ==None or len(email) == 0:
            message = VALIDATIONERROR_EMPTY_FIELD
        
        exist = Users.objects.filter(email=email).values()
        if len(exist) < 1:
            message = EMAIL_NOT_EXIST
        else:
            print(exist[0])
            # Authenticate the user
            user1 = authenticate(request, username=exist[0]['username'], password=password)
            if user1 is not None:
                login(request, user1, backend='django.contrib.auth.backends.ModelBackend')
                context = {
                    'user': user1
                }
                # return redirect('settings_url', context)
                return redirect('settings_url')
            else:
                message = EMAIL_PASSWORD_INCORRECT
                return render(request, template_name, {'error': 1, 'message': message})
        
        if message !='':
            return render(request, template_name, {'error': 1, 'message': message})
        
    return render(request, template_name, {})

def signupView(request):
    template_name = 'pixcoverapp/signup.html'
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
                return redirect('settings_url')
                # return render(request, template_name, {'error': 2, 'message': message})
        
    return render(request, template_name, {})

def signoutView(request):
    logout(request)
    return redirect('signin_url')

def settingsView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    
    exist = Users.objects.get(email=request.user.email)
    exist.skills = exist.skills
    categories = Categories.objects.filter().values()
    skills = Skills.objects.filter().values()
    
    template_name = 'pixcoverapp/work-settings.html'

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

def aboutView(request, profile_id = None):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    print('profile id:', profile_id)
    print('request user_id:', request.user.id)
    if profile_id:
        user = Users.objects.get(id=profile_id)
    else:
        user = Users.objects.get(email=request.user.email)
    print(f"This is user Id:{user.id}")
    # user.skills = list(user.skills)
    # user.skills = user.skills
    # Ensure user.skills is a list
    if isinstance(user.skills, str):  # If it's a string, convert to a list
        user.skills = json.loads(user.skills)  
    else:
        user.skills = list(user.skills)  # Ensure it's a list if it's a queryset
    print('user category id:', user.category)
    category = Categories.objects.get(id=user.category)
    # skills = Skills.objects.filter().values()
    skills = list(Skills.objects.values("id", "skill"))
    # print(f"This is the skills:{skills}")
    # print(f"This is user skills:{user.skills}")
    template_name = 'pixcoverapp/about.html'
    context = {'user': user, 'skills': skills, 'mycategory': category}
    return render(request, template_name, context)

# def reviewsView(request):
#     if not request.user.is_authenticated:
#         return redirect('signin_url')
#     form = OrderForm()
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show_url')
#     template_name = 'pixcoverapp/reviews.html'
#     context = {'form': form}
#     return render(request, template_name, context)

def reviewsView(request, user_id):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    user = Users.objects.get(id=user_id)
    template_name = 'pixcoverapp/reviews.html'
    reviewed_user = get_object_or_404(Users, id=user_id)
    reviews = Review.objects.filter(reviewed_user=reviewed_user)
    total_rating = 0
    ave_rating = 0
    for review in reviews:
        total_rating += review.rating
    if reviews.count() > 0:
        ave_rating = total_rating / reviews.count()
    context = {
        'reviews': reviews,
        'reviewed_user': reviewed_user,
        'ave_rating': ave_rating,
        'user': user,
    }
    return render(request, template_name, context)

def createReviewView(request, user_id):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    reviewed_user = get_object_or_404(Users, id=user_id)
    template_name = 'pixcoverapp/review_form.html'
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_vaild():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewed_user = reviewed_user
            review.save()
            return redirect('reviews_url', user_id=user_id)
        else:
            form = ReviewForm()
        return render(request, template_name, {'reviewed_user': reviewed_user})
    
def editReviewView(request, review_id):
    review = get_object_or_404(Review, id=review_id, reviewer=request.user)
    template_name = 'pixcoverapp/review_form.html'
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews_url', user_id=review.reviewed_user.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, template_name, {'form': form, 'review': review})

def deleteReviewView(request, review_id):
    review = get_object_or_404(Review, id=review_id, reviewer=request.user)
    template_name = 'pixcoverapp/review_confirm_delete.html'
    if request.method == 'POST':
        review.delete()
        return redirect('reviews_url', user_id=review.reviewed_user.id)
    return render(request, template_name, {'review': review})

def profileSearchView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')

    template_name = 'pixcoverapp/profile-search.html'
    skills = Skills.objects.filter().values()
    categories = Categories.objects.filter().values()
    countries = []
    for key in COUNTRIES:
        countries.append(COUNTRIES[key])
    context = {'profileImgs': ['/static/images/profile-cover-img-01.jpg', 
            '/static/images/profile-cover-img-02.jpg',
            '/static/images/profile-cover-img-03.jpg',
            '/static/images/profile-cover-img-04.jpg',
            '/static/images/profile-cover-img-05.jpg',
            '/static/images/profile-cover-img-06.jpg',
            '/static/images/profile-cover-img-07.jpg',
            '/static/images/profile-cover-img-08.jpg',
            '/static/images/profile-cover-img-09.jpg',
            '/static/images/profile-cover-img-10.jpg',
            '/static/images/profile-cover-img-11.jpg',
            '/static/images/profile-cover-img-12.jpg'],
            'skills': skills,
            'countries': countries,
            'country': '0',
            'categories': categories,
            'category': 0,
            'search_skills': [],
            'gender': '0',
            'user_lists': []}
        
    if request.method == 'POST':
        location = request.POST.get("location")
        gender = request.POST.get("gender")
        category = request.POST.get('category')

        search_skills = []
        for x in skills:
            if (request.POST.get("checkbox_" + x['skill']) == "on"):
                search_skills.append(x['id'])
        
        
        context['search_skills'] = search_skills
        context['country'] = location
        context['gender'] = gender
        if category:
            context['category'] = category

        user_lists = Users.objects.exclude(id=request.user.id)  # Exclude current user

        # Apply gender filter
        if gender == "male":
            user_lists = user_lists.filter(gender=0)
        elif gender == "female":
            user_lists = user_lists.filter(gender=1)

        # Apply location filter
        if location != "0":
            user_lists = user_lists.filter(location1=location)

        # Convert QuerySet to list of dictionaries
        user_lists = list(user_lists.values())

        # Filter users based on skills
        fresh_skill_lists = []
        for user in user_lists:
            fresh_skills = user['skills']
            if isinstance(fresh_skills, str):  
                fresh_skills = json.loads(fresh_skills)  # Ensure skills are in list format
            
            # Check if search_skills exist in fresh_skills
            if not search_skills or set(fresh_skills) & set(search_skills):
                fresh_skill_lists.append(user)

        # Filter users by category
        fresh_category_lists = [user for user in fresh_skill_lists if int(user['category']) == int(category)]

        context['user_lists'] = fresh_category_lists
        return render(request, template_name, context)

    return render(request, template_name, context)


def profileDetailView(request, profile_id):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    print('user id:', request.user.id)
    print('profile id:', profile_id)
    form = OrderForm()
    profile = Users.objects.get(id=profile_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/profile-visitor.html'
    context = {'form': form, 'user': profile, 'logged_in_user': request.user}
    return render(request, template_name, context)