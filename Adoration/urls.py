from django.urls import path
from Adoration import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import PackageSitemap
from django.views.generic.base import TemplateView
urlpatterns = [
    path('',views.Main,name = 'Main'),
    
    path('packages/<int:pk>/',views.packageDetails,name = 'PackageDetails'),
    path('sitemap.xml', sitemap, {'sitemaps': {'article' : PackageSitemap}},
     name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain" )),

     
]
