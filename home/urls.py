from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='index')
]

urlpatterns += (
    # urls for Category
    path('home/category/', views.CategoryListView.as_view(), name='home_category_list'),
    path('home/category/create/', views.CategoryCreateView.as_view(), name='home_category_create'),
    path('home/category/detail/<slug:slug>/', views.CategoryDetailView.as_view(), name='home_category_detail'),
    path('home/category/update/<slug:slug>/', views.CategoryUpdateView.as_view(), name='home_category_update'),
)

urlpatterns += (
    # urls for ServiceProvider
    path('home/serviceprovider/', views.ServiceProviderListView.as_view(), name='home_serviceprovider_list'),
    path('home/serviceprovider/create/', views.ServiceProviderCreateView.as_view(), name='home_serviceprovider_create'),
    path('home/serviceprovider/detail/<slug:slug>/', views.ServiceProviderDetailView.as_view(), name='home_serviceprovider_detail'),
    path('home/serviceprovider/update/<slug:slug>/', views.ServiceProviderUpdateView.as_view(), name='home_serviceprovider_update'),
)

urlpatterns += (
    # urls for Service
    path('home/service/', views.ServiceListView.as_view(), name='home_service_list'),
    path('home/service/create/', views.ServiceCreateView.as_view(), name='home_service_create'),
    path('home/service/detail/<slug:slug>/', views.ServiceDetailView.as_view(), name='home_service_detail'),
    path('home/service/update/<slug:slug>/', views.ServiceUpdateView.as_view(), name='home_service_update'),
)

urlpatterns += (
    path('home/form/', views.AddressFormView.as_view(template_name='home/form_1.html'), name='form_1'),
)
