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

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

SORT_DISTANCES = (
    ('','Select Distance'),
    ('5', '5 Miles'),
    ('10', '10 Miles'),
    ('20', '20 Miles'),
    ('50', '50 Miles'),
    ('Any', 'Any Distance')
    
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
    sort_distance = forms.ChoiceField(choices=SORT_DISTANCES,label='Sort Distance')
    

