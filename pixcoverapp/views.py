from django.shortcuts import redirect, render
from .forms import OrderForm
from .models import Orders
from users.models import Users
from .constants import *
# from pixcoverapp.database import Users
# from pixcoverapp.database import Categories
# from pixcoverapp.database import Skills
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from django.core.files import File
from django_countries.data import COUNTRIES

import json

# Create your views here.
def landingPageView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/index.html'
    context = {'form': form}
    return render(request, template_name, context)

# def signoutView(request):
#     template_name = 'pixcoverapp/signin.html'
#     logout(request)

#     return redirect('signin_url')

# def signinView(request):
#     template_name = 'pixcoverapp/signin.html'

#     if request.method == 'POST':
#         email = request.POST.get("email")
#         password= request.POST.get("password")
#         message = ''
#         if email ==None or len(email) == 0:
#             message = VALIDATIONERROR_EMPTY_FIELD
        
#         exist = Users.objects.filter(email=email).values()
#         if len(exist) < 1:
#             message = EMAIL_NOT_EXIST
#         else:
#             print(exist[0])
#             # Authenticate the user
#             user1 = authenticate(request, username=exist[0]['username'], password=password)
#             if user1 is not None:
#                 login(request, user1, backend='django.contrib.auth.backends.ModelBackend')
#                 return redirect('settings_url')
#             else:
#                 message = EMAIL_PASSWORD_INCORRECT
#                 return render(request, template_name, {'error': 1, 'message': message})
        
#         if message !='':
#             return render(request, template_name, {'error': 1, 'message': message})
        

#     return render(request, template_name, {})

# def signupView(request):
#     template_name = 'pixcoverapp/signup.html'
#     if request.method == 'POST':
#         email = request.POST.get("email")
        
#         password= request.POST.get("password")
#         password1= request.POST.get("password1")
#         message= ''
#         if (password != password1):
#             message = VALIDATIONERROR_PASSWORD_MISMATCH
#         elif len(email) == 0:
#             message = VALIDATIONERROR_EMPTY_FIELD
#         elif len(password) < 6:
#             message = VALIDATIONERROR_LENGTH

#         if message !='':
#             return render(request, template_name, {'error': 1, 'message': message})
#         else:
#             exist = Users.objects.filter(email=email).values()
#             if len(exist) > 0:
#                 message = VALIDATIONERROR_DUPLICATE
#                 return render(request, template_name, {'error': 1, 'message': message})
#             else:
                
#                 usr = Users(email=email, password=password, username=get_random_string(length=50)) # create new model instance
#                 usr.save() #seve to db
#                 # Retrieve the user
#                 user = Users.objects.get(email=email)

#                 # Set the user's password
#                 user.set_password(password)

#                 # Save the user
#                 user.save()
#                 message = REGISTER_SUCCESS
#                 return render(request, template_name, {'error': 2, 'message': message})
        
#     return render(request, template_name, {})

# def settingsView(request):
#     if not request.user.is_authenticated:
#         return redirect('signin_url')
    
#     exist = Users.objects.get(email=request.user.email)
#     exist.skills = json.loads(exist.skills)
#     categories = Categories.objects.filter().values()
#     skills = Skills.objects.filter().values()
    
#     template_name = 'pixcoverapp/work-settings.html'

#     countries = []
#     for key in COUNTRIES:
#         countries.append(COUNTRIES[key])

#     if request.method == 'POST':
#         user_id = request.POST.get("user_id")
#         is_file_upload = request.POST.get("is_file_upload")

#         if is_file_upload and int(is_file_upload) == 1: 
#             print('is file upload')
#             uploaded_file = request.FILES['profile_photo']
#             user = Users.objects.get(id=user_id)
#             user.avatar=uploaded_file
#             user.avatar.name = user_id + "_" + user.avatar.name
#             # Save the user
#             user.save()
#             user1 = user 
#             user1.skills = json.loads(user1.skills)
#             message = SUCCESSFULLY_UPDATED
#             return render(request, template_name, {'countries': countries, 'error':2, message: message, 'user':user1, 'categories': categories, 'skills': skills})
        
#         email = request.POST.get("email")
#         fullname= request.POST.get("fullname")
#         gender = request.POST.get("gender")
#         age = request.POST.get("age")
#         phone = request.POST.get("phone")
#         location1 = request.POST.get("location1")
#         location2 = request.POST.get("location2")
#         location3 = request.POST.get("location3")
#         location4 = request.POST.get("location4")

#         emailRowsValidate = Users.objects.filter(email=email).values()
#         if len(emailRowsValidate) >0:
#             print('emailRows', emailRowsValidate[0]['id'])
#             print('user_id', user_id)
#             if str(emailRowsValidate[0]['id']) != str(user_id):
#                 message = EMAIL_ALREADY_EXIST
#                 error = 1
#                 return render(request, template_name,  {'countries': countries, 'error': error, 'message':message, 'user': exist, 'categories': categories, 'skills': skills})
            
#         user = Users.objects.get(id=user_id)
#         user.fullname = fullname
#         user.email = email
#         user.gender = gender
#         user.age = age
#         user.phone_number = phone
#         # Save the user
#         user.save()
#         message = SUCCESSFULLY_UPDATED
#         error = 2

#         # For the second tab
#         about = request.POST.get("about")
#         user = Users.objects.get(id=user_id)
#         user.description = about
#         user.location1 = location1
#         user.location2 = location2
#         user.location3 = location3
#         user.location4 = location4
#         user.category = request.POST.get("category_id")
#         user.skills = []
#         for skill in skills:
#             checkbox_value = request.POST.get("checkbox_" + skill['skill'])
#             if checkbox_value == 'on':
#                 # Checkbox is checked
#                 user.skills.append(skill['id'])
        
        
#         user.skills = json.dumps(user.skills)
#         # Save the user
#         user.save()

#         user = Users.objects.get(id=user_id)
#         user.skills = json.loads(user.skills)
#         return render(request, template_name,  {'countries': countries, 'error': error, 'message':message, 'user': user, 'categories': categories, 'skills': skills})

#     return render(request, template_name, {'countries': countries, 'user':exist, 'categories': categories, 'skills': skills})

# def aboutView(request):
#     if not request.user.is_authenticated:
#         return redirect('signin_url')

#     user = Users.objects.get(email=request.user.email)
#     user.skills = json.loads(user.skills)
#     category = Categories.objects.get(id=user.category)
#     skills = Skills.objects.filter().values()
#     template_name = 'pixcoverapp/about.html'
#     context = {'user': user, 'skills': skills, 'mycategory': category}
#     return render(request, template_name, context)

def reviewsView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/reviews.html'
    context = {'form': form}
    return render(request, template_name, context)

def connectionsView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/connections.html'
    context = {'form': form}
    return render(request, template_name, context)

def statsView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/stats.html'
    context = {'form': form}
    return render(request, template_name, context)

# def profileSearchView(request):
#     if not request.user.is_authenticated:
#         return redirect('signin_url')

#     template_name = 'pixcoverapp/profile-search.html'
#     skills = Skills.objects.filter().values()
#     countries = []
#     for key in COUNTRIES:
#         countries.append(COUNTRIES[key])
#     context = {'profileImgs': ['/static/images/profile-cover-img-01.jpg', 
#             '/static/images/profile-cover-img-02.jpg',
#             '/static/images/profile-cover-img-03.jpg',
#             '/static/images/profile-cover-img-04.jpg',
#             '/static/images/profile-cover-img-05.jpg',
#             '/static/images/profile-cover-img-06.jpg',
#             '/static/images/profile-cover-img-07.jpg',
#             '/static/images/profile-cover-img-08.jpg',
#             '/static/images/profile-cover-img-09.jpg',
#             '/static/images/profile-cover-img-10.jpg',
#             '/static/images/profile-cover-img-11.jpg',
#             '/static/images/profile-cover-img-12.jpg'],
#             'skills': skills,
#             'countries': countries,
#             'search_skills': [],
#             'gender': '0',
#             'country': '0',
#             'user_lists': []}
    
#     if request.method == 'POST':
#         location = request.POST.get("location")
#         gender = request.POST.get("gender")
#         print(location)
#         print(gender)
#         if location == '0':
#             print('location is 0')
        
#         search_skills = []
#         for x in skills:
#             if (request.POST.get("checkbox_" + x['skill']) == "on"):
#                 search_skills.append(x['id'])
        
        
#         print(search_skills)
#         context['search_skills'] = search_skills
#         context['country'] = location
#         context['gender'] = gender

#         user_lists = Users.objects.filter().values()
        
#         fresh_lists = []

#         for user_list in user_lists:
#             if gender == "male":
#                 if (user_list['gender'] == 0):
#                     fresh_lists.append(user_list)
#             elif gender == "female":
#                 if (user_list['gender'] == 1):
#                     fresh_lists.append(user_list)
#             else:
#                 fresh_lists.append(user_list)
            
        
#         fresh_location_lists = []
#         for fresh_list in fresh_lists:
#             if location == "0":
#                 fresh_location_lists.append(fresh_list)
#             else:
#                 if fresh_list['location1'] == location:
#                     fresh_location_lists.append(fresh_list)

#         fresh_category_lists = []
#         for fresh_location_list in fresh_location_lists:
#             fresh_skills = json.loads(fresh_location_list['skills'])
#             exist = False
#             for x1 in fresh_skills:
#                 if x1 in search_skills:
#                     exist = True
#             if exist == True:
#                 fresh_category_lists.append(fresh_location_list)
       
#         print('final list', fresh_category_lists)
#         context['user_lists'] = fresh_category_lists
#         return render(request, template_name, context)

#     return render(request, template_name, context)

def profileEditView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/profile-edit.html'
    context = {'form': form      }
    return render(request, template_name, context)

def profileVisitorView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/profile-visitor.html'
    context = {'form': form}
    return render(request, template_name, context)

def profileMessengerView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/profile-messenger.html'
    context = {'form': form}
    return render(request, template_name, context)

def plansView(request):
    if not request.user.is_authenticated:
        return redirect('signin_url')
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/plans.html'
    context = {'form': form}
    return render(request, template_name, context)

def orderFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def showView(request):
    obj = Orders.objects.all()
    template_name = 'pixcoverapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'pixcoverapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'pixcoverapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
