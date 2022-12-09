from django.contrib.sitemaps import Sitemap
from .models import Article
 
 
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.article_published
        
    def location(self,obj):
        return '/blog/%s' % (obj.article_slug)
