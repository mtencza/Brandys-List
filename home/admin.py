from django.contrib import admin
from django import forms
from .models import Category, ServiceProvider, Service, Address

class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Category, CategoryAdmin)


class ServiceProviderAdminForm(forms.ModelForm):

    class Meta:
        model = ServiceProvider
        fields = '__all__'


class ServiceProviderAdmin(admin.ModelAdmin):
    form = ServiceProviderAdminForm
    list_display = ['name', 'slug', 'id']
    readonly_fields = ['slug', 'id']

admin.site.register(ServiceProvider, ServiceProviderAdmin)


class ServiceAdminForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Service, ServiceAdmin)

class AddressAdmin(admin.ModelAdmin):
    class Meta:
        model = Address
        fields = '__all__'

admin.site.register(Address, AddressAdmin)

