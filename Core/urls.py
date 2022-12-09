"""Core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from Adoration.models import Package

info_dict = {

    'queryset': Package.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', include('Adoration.urls')),
    path('sitemap.xml',sitemap,{'sitemaps': {'blog': GenericSitemap(info_dict, priority = 0.6)}}, name = 'django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


if settings.DEBUG == False:
    urlpatterns += [path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT,}),]



handler404 = 'Adoration.views.handler404'

handler500 = 'Adoration.views.handler500'

handler403 = 'Adoration.views.handler403'

handler400 = 'Adoration.views.handler400'

