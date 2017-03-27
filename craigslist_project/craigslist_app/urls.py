from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^main', views.main, name='main'),
    url(r'^create_listing', views.new_listing, name='create_listing'),
    url(r'^subcategory', views.subcategory_view, name='subcategory'),
]
