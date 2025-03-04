from django import forms
from .models import Review

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