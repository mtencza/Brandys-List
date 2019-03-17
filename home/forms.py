from django import forms
from .models import Category, ServiceProvider, Service


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name', 'id', 'services']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'Category']