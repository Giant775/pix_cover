from django import forms
from .models import Review
from .models import Orders

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min':1, 'max':5, 'class': 'review_form'}),
            'comment': forms.Textarea(attrs={'rows':3, 'class': 'form-control', 'placeholder': 'Write your review here...'})
        }
        labels = {
            'rating': 'Rating (1 - 5)',
            'comment': 'Your Review',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname' : 'First Name',
            'lname' : 'Last Name.' ,
            'price' : 'Price' ,
            'mail' : 'Email ID',
            'addr' : 'Address' ,
        }

        widgets  ={
            'oid' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'eg. Prosenjeet'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'eg. Shil'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
            'mail' : forms.EmailInput(attrs={'placeholder': 'eg. abc@xyz.com'}),
            'addr' : forms.Textarea(attrs={'placeholder': 'eg. IN'}),
        }