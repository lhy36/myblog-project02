from django import forms
from .models import BookAdd

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookAdd
        fields = ['bookName', 'author','publisher','publicationYear','volume','remarks','price','isbn']


