from django.contrib import admin
from .models import Post, Package, PageBanner

# Admin branding
admin.site.site_header = "SubhaYatra.in"
admin.site.site_title = "SubhaYatra Admin"
admin.site.index_title = "Website Control Panel"


# Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)


# Package
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("card_title", "price", "rating")
    prepopulated_fields = {"slug": ("page_title",)}


# 🔥 BANNER (ONLY ONE SYSTEM)
@admin.register(PageBanner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("page", "is_active")
    list_editable = ("is_active",)
    list_filter = ("page",)

    fieldsets = (
        ("Page Settings", {
            "fields": ("page", "is_active"),
        }),
        ("Banner Content", {
            "fields": ("title", "main_title", "subtitle", "paragraph"),
        }),
        ("Buttons", {
            "fields": (
                ("button1_text", "button1_link"),
                ("button2_text", "button2_link"),
            ),
        }),
        ("Images", {
            "fields": ("desktop_image", "mobile_image"),
        }),
    )
