from django.shortcuts import render, get_object_or_404
from .models import Post, Package, PageBanner


# Helper: page-wise banner
def get_banner(page_name):
    return PageBanner.objects.filter(page=page_name, is_active=True).first()


# HOME PAGE → ONLY 8 CARDS
def home(request):
    hero = get_banner("home")
    packages = Package.objects.all()[:8]
    posts = Post.objects.all()

    return render(request, "index.html", {
        "hero": hero,
        "packages": packages,
        "posts": posts,
    })


# PACKAGE DETAIL PAGE
def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    hero = get_banner("package")  # optional banner for detail page

    return render(request, "package_detail.html", {
        "hero": hero,
        "package": package
    })


# DESTINATIONS PAGE → ALL CARDS
def destinations(request):
    hero = get_banner("destinations")
    packages = Package.objects.all()

    return render(request, "destinations.html", {
        "hero": hero,
        "packages": packages
    })


def about(request):
    hero = get_banner("about")
    return render(request, "about.html", {"hero": hero})


def carrental(request):
    hero = get_banner("carrental")
    return render(request, "carrental.html", {"hero": hero})


def tempotravel(request):
    hero = get_banner("tempotravel")
    return render(request, "tempotravel.html", {"hero": hero})


def booking(request):
    hero = get_banner("booking")
    return render(request, "booking.html", {"hero": hero})
