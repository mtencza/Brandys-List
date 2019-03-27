from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request,'home/index.html',context)

from django.views.generic import DetailView, ListView, UpdateView, CreateView, FormView
from .models import Category, ServiceProvider, Service
from .forms import CategoryForm, ServiceProviderForm, ServiceForm, AddressForm
from django.urls import reverse_lazy

class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm


class ServiceProviderListView(ListView):
    model = ServiceProvider


class ServiceProviderCreateView(CreateView):
    model = ServiceProvider
    form_class = ServiceProviderForm


class ServiceProviderDetailView(DetailView):
    model = ServiceProvider


class ServiceProviderUpdateView(UpdateView):
    model = ServiceProvider
    form_class = ServiceProviderForm


class ServiceListView(ListView):
    model = Service


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm


class ServiceDetailView(DetailView):
    model = Service

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm

class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('success')
