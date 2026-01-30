from .models import TopBarMessage

def topbar_messages(request):
    return {
        "topbar_messages": TopBarMessage.objects.filter(is_active=True)
    }

#BASE SEO
from .models import BaseSEO

def base_seo(request):
    return {
        "base_seo": BaseSEO.objects.first()
    }
