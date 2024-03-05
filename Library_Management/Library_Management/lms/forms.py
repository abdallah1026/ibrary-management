from django import forms
from .models import Book, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }



class LMSForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_photo',
            'author_photo',
            'pages',
            'price',
            'rented_price',
            'rented_period',
            'total_rented',
            'status',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'author_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rented_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rented_price'}),
            'rented_period': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rented_period'}),
            'total_rented': forms.NumberInput(attrs={'class': "form-control", 'id': 'total_rented'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }