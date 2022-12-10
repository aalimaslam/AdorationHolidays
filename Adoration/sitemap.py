from django.contrib.sitemaps import Sitemap
from .models import Package
  
class PackageSitemap(Sitemap):
    def items(self):
        return Package.objects.all()
        
    def lastmod(self, obj):
        return obj.lastedit_date