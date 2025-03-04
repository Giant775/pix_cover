from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPageView, name='landing_url'),
    # path('signin/', views.signinView, name='signin_url'),
    # path('signup/', views.signupView, name='signup_url'),
    # path('signout/', views.signoutView, name= 'signout_url'),
    # path('settings/', views.settingsView, name='settings_url'),
    # path('about/', views.aboutView, name='about_url'), 
    # path('reviews/', views.reviewsView, name='reviews_url'),
    path('connections/', views.connectionsView, name='connections_url'),
    path('stats/', views.statsView, name='stats_url'),
    path('profile-search/', views.profileSearchView, name='profile_search_url'),
    path('profile-edit/', views.profileEditView, name='profile_edit_url'),
    # path('profile-visitor/', views.profileVisitorView, name='profile_visitor_url'),
    path('profile-messenger/', views.profileMessengerView, name='profile_messenger_url'),
    path('plans/', views.plansView, name='plans_url'),

    path('ofv/', views.orderFormView, name='order_url'),
    
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
]