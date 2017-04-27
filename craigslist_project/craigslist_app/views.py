from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MainForm, SignUpForm, ListingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Subcategory, Category, Listing
from django.db import transaction


def home(request, user_id=''):
    user_id = request.user.id
    listings = Listing.objects.filter(owner_id=user_id)
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            return redirect('craigslist_app/main')
    else:
        form = MainForm()
    context = {'username': request.user.username, 'listings': listings}
    return render(request, "craigslist_app/home.html", context)


def main(request):
    return render(request, "craigslist_app/main.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()


def new_listing(request, subcategory='', user_id=''):
    user_id = request.user.id
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            picture = form.cleaned_data.get('picture')
            owner = User.objects.get(id=user_id)
            subcategory = form.cleaned_data.get('subcategory')
            city = form.cleaned_data.get('city')
            print(name, description, picture, owner, subcategory, city)
            listing = Listing(name=name, description=description, picture=picture, owner=owner, subcategory=subcategory, city=city)
            listing.save()
            return redirect('/craigslist_app/home')
    else:
        form = MainForm()
    return render(request, 'listing.html', {'form': form})


def pets_subcategory_view(request, subcategory=1):
    listings = Listing.objects.filter(subcategory_id=subcategory)
    context = {'listings': listings}
    return render(request, 'craigslist_app/subcategory.html', context)


def lost_subcategory_view(request, subcategory=2):
    listings = Listing.objects.filter(subcategory_id=subcategory)
    context = {'listings': listings}
    return render(request, 'craigslist_app/subcategory.html', context)


def ticket_subcategory_view(request, subcategory=3):
    listings = Listing.objects.filter(subcategory_id=subcategory)
    context = {'listings': listings}
    return render(request, 'craigslist_app/subcategory.html', context)


def books_subcategory_view(request, subcategory=4):
    listings = Listing.objects.filter(subcategory_id=subcategory)
    context = {'listings': listings}
    return render(request, 'craigslist_app/subcategory.html', context)


def view_listing(request, id):
    context = {'listing': Listing.objects.get(id=id)}
    return render(request, 'craigslist_app/view_listing.html', context)
