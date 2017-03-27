from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MainForm, SignUpForm, ListingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Subcategory, Category, Listing, Profile


def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MainForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('craigslist_app/main')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MainForm()
    #commenting out attempt to get list on user's homepage
    # profile = Profile.objects.get(user_id=request.user.id)
    # listings = Listing.objects.get(owner_id=profile.user_id)
    context = {'username': request.user.username}#'listings': listings
    return render(request, "craigslist_app/home.html", context)


def main(request):
    return render(request, "craigslist_app/main.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('craigslist_app/home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()


def new_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            picture = form.cleaned_data.get('picture')
            owner = Profile.objects.get(pk=1)
            subcategory = Subcategory.objects.get(pk=1)
            city = form.cleaned_data.get('city')
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
