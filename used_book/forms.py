# forms.py
from django import forms
from .models import UsedBook 

class MultiFileInput(forms.ClearableFileInput):
    template_name = 'multi_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['multiple'] = True
        return context

class UsedBookForm(forms.ModelForm):
    detail_images = forms.FileField(widget=MultiFileInput, required=False)

    class Meta:
        model = UsedBook
        fields = ['title', 'author', 'description', 'price', 'image', 'category','detail_images']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='검색어')

class UsedBookCategoryForm(forms.ModelForm):
    class Meta:
        model = UsedBook
        fields = ['category']

