from django.shortcuts import render
from django.shortcuts import redirect
from geopy.geocoders import Nominatim

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

geolocator = Nominatim(user_agent="home")
class ServiceProviderListView(ListView):
    model = ServiceProvider

    def get_queryset(self):
        result = super(ServiceProviderListView, self).get_queryset()
        
        location = geolocator.geocode("175 5th Avenue NYC")
        sesh = self.request.session
        user_location = geolocator.geocode(sesh['address'] + ' '/
                                      sesh['city'] + ' '/
                                      sesh['state'] + ' '/
                                      sesh['zip']
                                      )
        
        return result

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context        
        context = super().get_context_data(**kwargs)
        context['service'] = self.request.GET.get('service')
        context['zip'] = self.request.session['zip']
        context['state'] = self.request.session['state']
        context['sort_distance'] = self.request.session['sort_distance']
        return context


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


STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'Nort Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('home_serviceprovider_list')

    def form_valid(self, form):
        self.request.session['address'] = form.cleaned_data['address']
        self.request.session['city'] = form.cleaned_data['city']
        self.request.session['state'] = form.cleaned_data['state']
        self.request.session['zip'] = form.cleaned_data['zip_code']
        self.request.session['sort_distance'] = form.cleaned_data['sort_distance']
        self.request.session['service'] = self.request.GET.get('service')
        return redirect('home_serviceprovider_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['service'] = self.request.GET.get('service')
        return context
