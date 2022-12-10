from django.urls import path
from Adoration import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import PackageSitemap
urlpatterns = [
    path('',views.Main,name = 'Main'),
    
    path('packages/<int:pk>/',views.packageDetails,name = 'PackageDetails'),
    path('sitemap.xml', sitemap, {'sitemaps': {'article' : PackageSitemap}},
     name='django.contrib.sitemaps.views.sitemap')
]
