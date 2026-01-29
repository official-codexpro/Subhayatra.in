from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("destinations/", views.destinations, name="destinations"),
    path("package/<slug:slug>/", views.package_detail, name="package_detail"),
    path("about.html", views.about, name="about"),
    path("carrental.html", views.carrental, name="carrental"),
    path("tempotravel.html", views.tempotravel, name="tempotravel"),
    path("booking.html", views.booking, name="booking"),
]
