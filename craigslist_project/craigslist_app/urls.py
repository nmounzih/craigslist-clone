from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^main', views.main, name='main'),
    url(r'^create_listing', views.new_listing, name='create_listing'),
    url(r'^pets', views.pets_subcategory_view, name='pets'),
    url(r'^lost_and_found', views.lost_subcategory_view, name='lost_and_found'),
    url(r'^coachella_tickets', views.ticket_subcategory_view, name='coachella_tickets'),
    url(r'^books', views.books_subcategory_view, name='books'),
]
