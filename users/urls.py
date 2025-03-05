from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signinView, name='signin_url'),
    path('signup/', views.signupView, name='signup_url'),
    path('signout/', views.signoutView, name='signout_url'),
    path('settings/', views.settingsView, name='settings_url'),
    path('about/', views.aboutView, name='about_url'),
    path('reviews/<int:user_id>', views.reviewsView, name='reviews_url'),
    path('reviews/<int:user_id>/create/', views.createReviewView, name='create_review_url'),
    path('reviews/<int:user_id>/edit/', views.editReviewView, name='edit_review_url'),
    path('reviews/<int:user_id>/delete/', views.deleteReviewView, name='delete_review_url'),
    path('profile-search/', views.profileSearchView, name='profile_search_url'),
    # path('profile-edit/', views.profileEditView, name='profile_edit_url'),
    # path('profile-visitor/', views.profileVisitorView, name='profile_visitor_url'),
]