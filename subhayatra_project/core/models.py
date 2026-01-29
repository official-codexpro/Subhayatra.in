from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
from django.db import models
from django.utils.text import slugify


class Package(models.Model):
    # Titles
    card_title = models.CharField(max_length=100)     # home card
    page_title = models.CharField(max_length=200)     # detail page

    # Pricing & rating
    price = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.8)

    # Images
    card_image = models.URLField()
    detail_image = models.URLField()

    # Content
    overview = models.TextField()
    highlights = models.TextField(
        help_text="One highlight per line"
    )
    itinerary = models.TextField(
        help_text="One day per line (Day 1: ..., Day 2: ...)"
    )

    # SEO / URL
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.page_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.card_title

#hero section image change feature here
from django.db import models

class HomeHero(models.Model):
    # Text content
    title = models.CharField(max_length=100, blank=True, null=True)
    main_title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)

    # Buttons
    button1_text = models.CharField(max_length=50, blank=True, null=True)
    button1_link = models.URLField(blank=True, null=True)

    button2_text = models.CharField(max_length=50, blank=True, null=True)
    button2_link = models.URLField(blank=True, null=True)

    # Images
    image = models.URLField(help_text="Desktop hero image", blank=True, null=True)
    mobile_image = models.URLField(help_text="Mobile hero image", blank=True, null=True)

    # Settings
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "HomeBanner"
        verbose_name_plural = "HomeBanner"

    def __str__(self):
        return self.title or f"HomeBanner #{self.id}"


