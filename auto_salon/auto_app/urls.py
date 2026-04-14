from django.urls import path
from .views import home, detail, brand, about, add_car, add_brand
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('brand/<int:brand_id>/', brand, name='brand'),
    path('about/', about, name='about'),
    path('car/<int:car_id>/', detail, name='detail'),
    path('add-car/', views.add_car, name='add_car'),
    path('add-brand/', views.add_brand, name='add_brand'),
    path('car-delete/<int:car_id>/', views.car_delete, name='car_delete'),

    path('brand-delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
]