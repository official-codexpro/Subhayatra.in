from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Package(models.Model):
    card_title = models.CharField(max_length=100)
    page_title = models.CharField(max_length=200)

    price = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.8)

    card_image = models.URLField()
    detail_image = models.URLField()

    overview = models.TextField()
    highlights = models.TextField(help_text="One highlight per line")
    itinerary = models.TextField(help_text="One day per line")

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.page_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.card_title


class PageBanner(models.Model):
    PAGE_CHOICES = (
        ("home", "Home Page"),
        ("about", "About Page"),
        ("destinations", "Destinations Page"),
        ("carrental", "Car Rental Page"),
        ("tempotravel", "Tempo Travel Page"),
        ("booking", "Booking Page"),
    )

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)

    title = models.CharField(max_length=100, blank=True, null=True)
    main_title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)

    button1_text = models.CharField(max_length=50, blank=True, null=True)
    button1_link = models.URLField(blank=True, null=True)

    button2_text = models.CharField(max_length=50, blank=True, null=True)
    button2_link = models.URLField(blank=True, null=True)

    desktop_image = models.URLField(blank=True, null=True)
    mobile_image = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Page Banner"
        verbose_name_plural = "Page Banners"

    def __str__(self):
        return f"{self.page} banner"


class TopBarMessage(models.Model):
    text = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Top Bar Message"
        verbose_name_plural = "Top Bar Messages"

    def __str__(self):
        return self.text

#BASE SEO OPTION IN ADMIN
class BaseSEO(models.Model):
    site_name = models.CharField(max_length=100, default="SubhaYatra")

    meta_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160)

    og_image = models.URLField(blank=True)
    favicon = models.URLField(blank=True)

    class Meta:
        verbose_name = "BASE-SEO"
        verbose_name_plural = "BASE-SEO"

    def __str__(self):
        return "Base SEO (Global)"
