from django.contrib import admin

from .models import Profile, Category, Subcategory, Listing

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Listing)
