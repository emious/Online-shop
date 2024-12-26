from django import forms
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['title', 'comment', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your review'}),
            'rating': forms.Select(choices=[(i, f'{i} Star') for i in range(1, 6)], attrs={'class': 'form-control'}),
        }