from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Car
from .forms import BrandForm, CarForm
from django.http import HttpRequest
from .models import Car


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


# -----------------------------


def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('home')
    context = {'car': car}

    return render(request, 'auto_app/car_delete.html', context)



def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.delete()
        return redirect('home')
    context = {'brand': brand}
    return render(request, 'auto_app/brand_confirm_delete.html',context )


def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'auto_app/update_brand.html', {'form': form, 'brand': brand})



def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('detail', car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'auto_app/update_car.html', {'form': form, 'car': car})