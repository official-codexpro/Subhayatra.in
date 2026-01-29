from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post),

from .models import Package
admin.site.register(Package),

from django.contrib import admin
admin.site.site_header = "SubhaYatra.in"
from django.contrib import admin
from .models import HomeHero

from django.contrib import admin
from .models import HomeHero

from django.contrib import admin
from .models import HomeHero

@admin.register(HomeHero)
class HomeHeroAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_editable = ("is_active",)

    fieldsets = (
        ("Text Content", {
            "fields": ("title", "main_title", "subtitle", "paragraph"),
        }),
        ("Buttons", {
            "fields": (
                ("button1_text", "button1_link"),
                ("button2_text", "button2_link"),
            ),
        }),
        ("Images", {
            "fields": ("image", "mobile_image"),
        }),
        ("Settings", {
            "fields": ("is_active",),
        }),
    )

