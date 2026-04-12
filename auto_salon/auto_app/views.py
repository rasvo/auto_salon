from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import BrandForm, CarForm
from django.http import HttpRequest


def home(request: HttpRequest):
    brands = Brand.objects.all()
    car = Car.objects.all()

    context = {
        'brands': brands,
         'car': car
    }

    return render(request, 'auto_app/home.html', context)

def about(request):
    return render(request, 'auto_app/about.html')


def brand(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(id=brand_id)
    cars = Car.objects.filter(brand=brand)

    context = {
        'brand': brand,
        'cars': cars

    }

    return render(request, 'auto_app/brand.html', context)

def detail(request: HttpRequest, car_id: int):

    car = Car.objects.get(id=car_id)

    context = {
        'car': car
    }
    return render(request, 'auto_app/detail.html', context)

def add_brand(request: HttpRequest):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BrandForm()
    return render(request, 'auto_app/add_brand.html', {'form': form})

def add_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'auto_app/add_car.html', {'form': form})

