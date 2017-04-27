from django.contrib import admin

from .models import Category, Subcategory, Listing

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Listing)
