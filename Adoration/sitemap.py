from django.contrib.sitemaps import Sitemap
from .models import Package
  
class PackageSitemap(Sitemap):
    changefreq = "weekl"
    priority = 0.8
    
    def items(self):
        return Package.objects.all()
        
    def lastmod(self, obj):
        return obj.lastedit_date