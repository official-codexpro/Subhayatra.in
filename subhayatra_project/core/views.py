from django.shortcuts import render, get_object_or_404
from .models import Post, Package, HomeHero


# HOME PAGE → ONLY 8 CARDS
def home(request):
    hero = HomeHero.objects.filter(is_active=True).first()
    packages = Package.objects.all()[:8]   # 👈 LIMIT HERE
    posts = Post.objects.all()

    return render(request, "index.html", {
        "hero": hero,
        "packages": packages,
        "posts": posts,
    })


# PACKAGE DETAIL PAGE
def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    return render(request, "package_detail.html", {
        "package": package
    })


# DESTINATIONS PAGE → ALL CARDS
def destinations(request):
    packages = Package.objects.all()   # 👈 NO LIMIT
    return render(request, "destinations.html", {
        "packages": packages
    })

from django.shortcuts import render

def about(request):
    return render(request, "about.html")

def carrental(request):
    return render(request, "carrental.html")

def tempotravel(request):
    return render(request, "tempotravel.html")

def booking(request):
    return render(request, "booking.html")
